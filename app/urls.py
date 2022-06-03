from urllib.parse import urlencode
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    
]