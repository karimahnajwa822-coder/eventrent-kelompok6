from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('kategori/', views.kategori, name='kategori'),
    path('barang/', views.barang, name='barang'),
    path('detail-barang/', views.detail_barang, name='detail_barang'),
    path('sewa/<int:barang_id>/', views.sewa_barang, name='sewa_barang'),
    path('penyewaan/', views.penyewaan, name='penyewaan'),
    path('penyewaan/tambah/',views.form_penyewaan, name='form_penyewaan'),
    path('keranjang/', views.keranjang, name='keranjang'),
    path('laporan/', views.laporan, name='laporan'),
    path('laporan/export/excel/', views.export_excel, name='export_excel'),
]