from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('penyewaan/', views.penyewaan, name='penyewaan'),
    path('penyewaan/tambah/', views.form_penyewaan, name='form_penyewaan'),
=======
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
>>>>>>> e43f98125f5d66dea1767357b9d875f11f76b2c0
]