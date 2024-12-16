from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('clubmembers/', views.clubmembers, name='clubmembers'),
    path('clubmembers/memberdetails/<int:id>', views.details, name='memberdetails'),
    path('testing/', views.testing, name='testing'),
]