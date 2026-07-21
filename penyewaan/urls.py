from django.urls import path
from . import views

urlpatterns = [

    # Login
    path('', views.login_view, name='login'),

    # Register
    path('register/', views.register_view, name='register'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Master Data
    path('kategori/', views.kategori, name='kategori'),
    path('barang/', views.barang, name='barang'),

    # Penyewaan
    path('penyewaan/', views.penyewaan, name='penyewaan'),
    path('penyewaan/tambah/', views.form_penyewaan, name='form_penyewaan'),

    # Keranjang
    path('keranjang/', views.keranjang, name='keranjang'),

    # Laporan
    path('laporan/', views.laporan, name='laporan'),
]