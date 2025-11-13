from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.aboutpage, name='about'),
    path('contact/', views.contact, name='contact')
]