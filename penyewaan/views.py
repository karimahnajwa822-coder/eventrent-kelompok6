from django.shortcuts import render, redirect
from django.http import HttpResponse
from openpyxl import Workbook

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

# ======================
# EXPORT EXCEL LAPORAN
# ======================

def export_excel(request):

    # Membuat workbook baru
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Laporan Penyewaan"

    # Header kolom
    worksheet.append([
        "No",
        "Nama Pelanggan",
        "Peralatan",
        "Tanggal Pinjam",
        "Tanggal Kembali",
        "Total Bayar",
        "Status"
    ])

    # ======================
    # DATA SEMENTARA (Dummy)
    # Nanti bisa diganti dengan data database
    # ======================

    data_laporan = [
        ["Andi", "Sound System", "20-07-2026", "22-07-2026", 500000, "Selesai"],
        ["Budi", "Tenda", "21-07-2026", "23-07-2026", 750000, "Dipinjam"],
        ["Sinta", "Kursi", "22-07-2026", "24-07-2026", 300000, "Selesai"],
        ["Rina", "Meja", "23-07-2026", "24-07-2026", 200000, "Dipinjam"],
    ]

    nomor = 1

    for item in data_laporan:
        worksheet.append([
            nomor,
            item[0],
            item[1],
            item[2],
            item[3],
            item[4],
            item[5],
        ])
        nomor += 1

    # Membuat response download
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="Laporan_Penyewaan.xlsx"'
    )

    workbook.save(response)

    return response