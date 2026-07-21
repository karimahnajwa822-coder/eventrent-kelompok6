from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Barang


# ======================
# LOGIN
# ======================

def login_view(request):
    if request.method == "POST":
        return redirect('dashboard')

    return render(request, 'penyewaan/login.html')


# ======================
# REGISTER
# ======================

def register_view(request):
    if request.method == "POST":
        return redirect('login')

    return render(request, 'penyewaan/register.html')


# ======================
# DASHBOARD
# ======================

def dashboard(request):
    return render(request, 'penyewaan/dashboard.html')


# ======================
# KATEGORI
# ======================

def kategori(request):
    return render(request, 'penyewaan/kategori.html')


# ======================
# BARANG
# ======================

def barang(request):
    return render(request, 'penyewaan/barang.html')


# ======================
# DETAIL BARANG
# ======================

def detail_barang(request):
    barang_list = Barang.objects.all()

    context = {
        'barang_list': barang_list,
    }

    return render(
        request,
        'penyewaan/detail_barang.html',
        context
    )


# ======================
# SEWA BARANG
# ======================

def sewa_barang(request, barang_id):
    """
    Menambahkan 1 barang ke keranjang.
    Data keranjang disimpan di session.
    """

    barang = get_object_or_404(
        Barang,
        id=barang_id
    )

    keranjang = request.session.get(
        'keranjang',
        {}
    )

    key = str(barang_id)

    if key in keranjang:

        keranjang[key]['jumlah'] += 1

    else:

        keranjang[key] = {
            'nama_barang': barang.nama_barang,
            'kode_barang': barang.kode_barang,
            'harga_sewa': str(barang.harga_sewa),
            'jumlah': 1,
        }

    request.session['keranjang'] = keranjang

    messages.success(
        request,
        f'"{barang.nama_barang}" berhasil ditambahkan ke keranjang.'
    )

    return redirect('detail_barang')


# ======================
# PENYEWAAN
# ======================

def penyewaan(request):
    return render(
        request,
        'penyewaan/penyewaan.html'
    )


def form_penyewaan(request):
    return render(
        request,
        'penyewaan/form_penyewaan.html'
    )


# ======================
# KERANJANG
# ======================

def keranjang(request):
    keranjang_data = request.session.get(
        'keranjang',
        {}
    )

    context = {
        'keranjang': keranjang_data,
    }

    return render(
        request,
        'penyewaan/keranjang.html',
        context
    )


# ======================
# LAPORAN
# ======================

def laporan(request):
    return render(
        request,
        'penyewaan/laporan.html'
    )