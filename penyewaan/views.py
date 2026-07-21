from django.shortcuts import render, redirect


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
# PENYEWAAN
# ======================

def penyewaan(request):
    return render(request, 'penyewaan/penyewaan.html')


def form_penyewaan(request):
    return render(request, 'penyewaan/form_penyewaan.html')


# ======================
# KERANJANG
# ======================

def keranjang(request):
    return render(request, 'penyewaan/keranjang.html')


# ======================
# LAPORAN
# ======================

def laporan(request):
    return render(request, 'penyewaan/laporan.html')