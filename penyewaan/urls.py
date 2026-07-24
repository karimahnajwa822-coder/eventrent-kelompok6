from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('register/', views.register_view, name='register'),
    path('register-dosen/', views.register_dosen, name='register_dosen'),
    path(
        'persetujuan-dosen/',
        views.persetujuan_dosen,
        name='persetujuan_dosen'
    ),

    path(
        'setujui-dosen/<int:id>/',
        views.setujui_dosen,
        name='setujui_dosen'
    ),

    path(
    'tolak-dosen/<int:id>/',
    views.tolak_dosen,
    name='tolak_dosen'
),

    path(
        'tambah-operator/',
        views.tambah_operator,
        name='tambah_operator'
    ),

    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'dashboard-dosen/',
        views.dashboard_dosen,
        name='dashboard_dosen'
    ),

    path(
        'dashboard-operator/',
        views.dashboard_operator,
        name='dashboard_operator'
    ),

    path('kategori/', views.kategori, name='kategori'),
    path('kategori/tambah/', views.form_kategori, name='form_kategori'),
    path('kategori/detail/<int:id>/', views.detail_kategori, name='detail_kategori'),
    path('kategori/edit/<int:id>/', views.edit_kategori, name='edit_kategori'),
    path('kategori/hapus/<int:id>/', views.hapus_kategori, name='hapus_kategori'),

    path('barang/', views.barang, name='barang'),
    path('barang/detail/', views.detail_barang, name='detail_barang'),

    path('penyewaan/', views.penyewaan, name='penyewaan'),
    path('form-penyewaan/', views.form_penyewaan, name='form_penyewaan'),

    path('detail-penyewaan/<int:id>/', views.detail_penyewaan, name='detail_penyewaan'),
    path('edit-penyewaan/<int:id>/', views.edit_penyewaan, name='edit_penyewaan'),
    path('hapus-penyewaan/<int:id>/', views.hapus_penyewaan, name='hapus_penyewaan'),

    path('keranjang/', views.keranjang, name='keranjang'),
    path('laporan/', views.laporan, name='laporan'),
    path(
        'persetujuan-peminjaman/',
        views.persetujuan_peminjaman,
        name='persetujuan_peminjaman'
    ),

    path(
        'setujui-peminjaman/<int:id>/',
        views.setujui_peminjaman,
        name='setujui_peminjaman'
    ),

    path(
        'tolak-peminjaman/<int:id>/',
        views.tolak_peminjaman,
        name='tolak_peminjaman'
    ),

    path(
        'upload-bukti/<int:id>/',
        views.upload_bukti,
        name='upload_bukti'
    ),

    path(
        'verifikasi-pembayaran/',
        views.verifikasi_pembayaran,
        name='verifikasi_pembayaran'
    ),

    path(
        'setujui-pembayaran/<int:id>/',
        views.setujui_pembayaran,
        name='setujui_pembayaran'
    ),

    path(
        'tolak-pembayaran/<int:id>/',
        views.tolak_pembayaran,
        name='tolak_pembayaran'
    ),
    path(
        'pengembalian-barang/',
        views.pengembalian_barang,
        name='pengembalian_barang'
    ),

    path(
        'proses-pengembalian/<int:id>/',
        views.proses_pengembalian,
        name='proses_pengembalian'
    ),
]