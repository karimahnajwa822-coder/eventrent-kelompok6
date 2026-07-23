from django.urls import path
from . import views

urlpatterns = [

    # LOGIN
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),

    # KATEGORI
    path('kategori/', views.kategori, name='kategori'),
    path('kategori/tambah/', views.form_kategori, name='form_kategori'),
    path('kategori/detail/<int:id>/', views.detail_kategori, name='detail_kategori'),
    path('kategori/edit/<int:id>/', views.edit_kategori, name='edit_kategori'),
    path('kategori/hapus/<int:id>/', views.hapus_kategori, name='hapus_kategori'),

    # BARANG
    path('barang/', views.barang, name='barang'),
    path('detail-barang/', views.detail_barang, name='detail_barang'),
    path('sewa/<int:barang_id>/', views.sewa_barang, name='sewa_barang'),

    # PENYEWAAN
    path('penyewaan/', views.penyewaan, name='penyewaan'),
    path('penyewaan/tambah/', views.form_penyewaan, name='form_penyewaan'),
    path('detail-penyewaan/<int:id>/', views.detail_penyewaan, name='detail_penyewaan'),
    path('edit-penyewaan/<int:id>/', views.edit_penyewaan, name='edit_penyewaan'),
    path('hapus-penyewaan/<int:id>/', views.hapus_penyewaan, name='hapus_penyewaan'),

    # KERANJANG
    path('keranjang/', views.keranjang, name='keranjang'),

    # LAPORAN
    path('laporan/', views.laporan, name='laporan'),
    
]