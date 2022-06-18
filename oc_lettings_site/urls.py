from django.contrib import admin
from django.urls import path, include

from lettings.urls import lettings_extra_patterns
from profiles.urls import profiles_extra_patterns

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(lettings_extra_patterns)),
    path('profiles/', include(profiles_extra_patterns)),
    path('admin/', admin.site.urls),
]
