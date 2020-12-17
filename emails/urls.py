from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='emails-home'),
    path('registro/', views.register, name='emails-register'),
    path('success/', views.success, name='emails-success'),
]
