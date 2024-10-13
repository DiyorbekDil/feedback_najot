from django.urls import path
from team_faq.views import index_view, _404_page_view

app_name = 'index'
urlpatterns = [
    path('404/', _404_page_view, name='404'),
    path('', index_view, name='index')
]
