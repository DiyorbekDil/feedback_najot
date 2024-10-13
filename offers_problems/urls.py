from django.urls import path

from offers_problems import views
from offers_problems import pagination

app_name = 'offers_problems'

urlpatterns = [
    path('show-off-prob/', pagination.index_view, name='show_off_prob'),
    path('offer/', views.create_offer_view, name='offer'),
    path('problems/', views.create_problem_view, name='problem'),
    path('submit/', views.submit, name='submit'),
]
