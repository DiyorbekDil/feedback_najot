from users.views import *
from django.urls import path


app_name = 'user'
urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('verify_url/<uidb64>/<token>/', verify_email, name="verify_email"),
    path('warning_page/', warning_view, name="warning_page"),
    path('success_page/', success_view, name="success_page"),
]