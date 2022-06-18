from django.urls import path

from profiles.views import profiles_index, profile

profiles_extra_patterns = [
    path('', profiles_index, name='profiles_index'),
    path('<str:username>/', profile, name='profile'),
]
