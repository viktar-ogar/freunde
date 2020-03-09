from django.urls import path
from . import views as home_views

urlpatterns = [
    path('', home_views.index),
    path('about/', home_views.about),
    path('contacts/', home_views.contacts),
]