from django.shortcuts import render
from django.urls import path
from . import views


# Url Patterns
urlpatterns = [
    path('', views.main, name='index'),
    path('members/', views.member, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('create_member/', views.create_member, name='create_member'),
    path('success_member_registration/',
         lambda request: render(request, 'success_member_registration.html'),
         name='success_member_registration'),
    path('testing/', views.testing, name='testing'),
]
