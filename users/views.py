from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages

from conf import settings
from users.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from users.token import email_verification_token


def warning_view(request):
    return render(request, 'warning_page.html')


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    if user is not None and email_verification_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(reverse_lazy('user:login'))
    else:
        return render(request, 'email_not_verified.html')


def send_email_verification(request, user):
    token = email_verification_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    verification_url = reverse('user:verify_email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current_site.domain}{verification_url}"

    text_content = render_to_string(
        'verify_email.html',
        {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject='Verification email',
        body=text_content,
        to=[user.email],
        from_email=settings.EMAIL_HOST_USER,
    )
    message.attach_alternative(text_content, 'text/html')
    message.send()


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            # verify email
            send_email_verification(request, user)
            return redirect(reverse_lazy('user:warning_page'))
        else:
            errors = form.errors
            return render(request, 'main/auth/register/register.html', {'form': form, 'errors': errors})
    else:
        return render(request, 'main/auth/register/register.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('user:success_page'))
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'main/auth/login/login.html')
    else:
        return render(request, 'main/auth/login/login.html')


def success_view(request):
    return render(request, 'main/success/success.html')
