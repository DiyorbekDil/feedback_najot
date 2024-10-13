from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from offers_problems.forms import ProblemModelForm, OfferForm
from offers_problems.models import OfferModel


def submit(request):
    return render(request, 'success-submit.html')


def create_problem_view(request):
    if request.method == 'POST':
        form = ProblemModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('offers_problems:submit'))
    else:
        form = ProblemModelForm()
        return render(request, 'main/forms/offer/offer-form.html', {'form': form})


def create_offer_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OfferForm(request.POST, request.FILES)
            if form.is_valid():
                OfferModel.objects.create(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    user_id=request.user
                )
                return redirect(reverse_lazy('offers_problems:submit'))
            else:
                print(form.errors)
        else:
            form = OfferForm()
            return render(request, 'main/forms/offer/offer-form.html', {'form': form})
    else:
        return redirect(reverse_lazy('user:login'))
