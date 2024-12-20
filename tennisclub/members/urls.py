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
    path('select_member_to_edit/', views.select_member_to_edit, name='select_member_to_edit'),
    path('edit_member/<int:id>/', views.edit_member, name='edit_member'),
    path('delete_members/', views.delete_members, name='delete_members'),
    path('testing/', views.testing, name='testing'),
]
