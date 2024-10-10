from django.urls import path
from Team_FAQ.views import index_view

app_name = 'index'
urlpatterns = [
    path('', index_view, name='index'),
]