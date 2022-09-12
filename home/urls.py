from django.urls import path

from home import views

home_extra_patterns = [
    path('', views.index, name='index'),
]
