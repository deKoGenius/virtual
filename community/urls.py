from django.urls import path

from . import views

urlpatterns = [
    path('', views.User, name='user'),
    # path('a', views.Input, name='input'),
]