from django.urls import path
from . import views


urlpatterns = [
    path('', views.svaz, name='svaz'),
]