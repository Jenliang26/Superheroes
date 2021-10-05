from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name = 'heroes'
urlpatterns = [
    path('index', views.index, name='index')
]