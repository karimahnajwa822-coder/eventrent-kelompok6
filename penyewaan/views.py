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

def form_kategori(request):
    return render(request, 'penyewaan/form_kategori.html')

def detail_kategori(request, id):
    return render(request, 'penyewaan/detail_kategori.html')

def edit_kategori(request, id):
    return render(request, 'penyewaan/edit_kategori.html')

def hapus_kategori(request, id):
    return redirect('kategori')

# ======================
# BARANG
# ======================

def barang(request):
    return render(request, 'penyewaan/barang.html')

def detail_barang(request):
    return render(request, 'penyewaan/detail_barang.html')

# ======================
# PENYEWAAN
# ======================

def penyewaan(request):
    return render(request, 'penyewaan/penyewaan.html')

def form_penyewaan(request):
    return render(request, 'penyewaan/form_penyewaan.html')

# ======================
# DETAIL PENYEWAAN
# ======================

def detail_penyewaan(request, id):
    return render(request, 'penyewaan/detail_penyewaan.html')

# ======================
# EDIT PENYEWAAN
# ======================

def edit_penyewaan(request, id):
    return render(request, 'penyewaan/edit_penyewaan.html')

# ======================
# HAPUS PENYEWAAN
# ======================

def hapus_penyewaan(request, id):
    return render(request, 'penyewaan/hapus_penyewaan.html')

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