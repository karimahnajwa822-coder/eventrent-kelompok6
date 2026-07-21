from django.urls import path
from . import views

urlpatterns = [
    path('detail-barang/', views.detail_barang, name='detail_barang'),
    path('sewa/<int:barang_id>/', views.sewa_barang, name='sewa_barang'),
    path('keranjang/', views.keranjang, name='keranjang'),
]