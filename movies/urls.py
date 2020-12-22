# movies/urls.py
from django.urls import path

from . import views

urlpatterns = [
  path('answer', views.answer, name='answer'),
  path('choose-language', views.choose_language, name='choose-language'), 
  path('choose-service', views.choose_service, name='choose-service'),
  ]
