from django.urls import path
from . import views

urlpatterns = [

    # LOGIN
    path('', views.login_view, name='login'),

    # REGISTER
    path('register/', views.register_view, name='register'),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),

    # KATEGORI
    path('kategori/', views.kategori, name='kategori'),

    # BARANG
    path('barang/', views.barang, name='barang'),

    # DETAIL BARANG
    path(
        'detail-barang/',
        views.detail_barang,
        name='detail_barang'
    ),

    # MASUKKAN BARANG KE KERANJANG
    path(
        'sewa/<int:barang_id>/',
        views.sewa_barang,
        name='sewa_barang'
    ),

    # PENYEWAAN
    path(
        'penyewaan/',
        views.penyewaan,
        name='penyewaan'
    ),

    path(
        'penyewaan/tambah/',
        views.form_penyewaan,
        name='form_penyewaan'
    ),

    # KERANJANG
    path(
        'keranjang/',
        views.keranjang,
        name='keranjang'
    ),

    # LAPORAN
    path(
        'laporan/',
        views.laporan,
        name='laporan'
    ),
]