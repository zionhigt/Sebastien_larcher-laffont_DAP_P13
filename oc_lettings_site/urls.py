from django.contrib import admin
from django.urls import path, include

from lettings.urls import lettings_extra_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(lettings_extra_patterns)),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
