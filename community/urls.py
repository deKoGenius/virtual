from django.urls import path

from . import views

urlpatterns = [
    path('', views.question_create, name='user'),
]