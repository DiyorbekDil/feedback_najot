from django.urls import path

from offers_problems import views

app_name = 'offers_problems'

urlpatterns = [
    path('offer/', views.create_offer_view, name='offer'),
    path('problems/', views.create_problem_view, name='problem'),
    path('submit/', views.submit, name='submit'),
]
