from django.shortcuts import render, redirect
from django.http import HttpResponse
from openpyxl import Workbook

from .models import Penyewaan, Barang
from django.contrib.auth.models import User
from django.db.models import Sum



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

        # Mengambil semua data penyewaan
    data = Penyewaan.objects.select_related(
        'penyewa',
        'barang'
    ).order_by('-tanggal_sewa')

    # Mengambil input tanggal dari form
    tanggal_awal = request.GET.get('tanggal_awal')
    tanggal_akhir = request.GET.get('tanggal_akhir')

    # Filter berdasarkan tanggal jika kedua input diisi
    if tanggal_awal and tanggal_akhir:
        data = data.filter(
            tanggal_sewa__range=[tanggal_awal, tanggal_akhir]
        )

    # Statistik berdasarkan hasil filter
    total_penyewaan = data.count()

    total_pendapatan = (
        data.aggregate(total=Sum('total_harga'))['total'] or 0
    )

    total_barang = Barang.objects.count()

    total_pelanggan = User.objects.count()

    belum_kembali = data.exclude(
        status_transaksi="Selesai"
    ).count()

    context = {
        'laporan': data,
        'total_penyewaan': total_penyewaan,
        'total_pendapatan': total_pendapatan,
        'total_barang': total_barang,
        'total_pelanggan': total_pelanggan,
        'belum_kembali': belum_kembali,
        'tanggal_awal': tanggal_awal,
        'tanggal_akhir': tanggal_akhir,
    }

    return render(
        request,
        'penyewaan/laporan.html',
        context
    )
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

    # Mengambil data dari database
    data_laporan = Penyewaan.objects.select_related(
        'penyewa',
        'barang'
    )

    nomor = 1

    for item in data_laporan:

        worksheet.append([
            nomor,
            item.penyewa.username,
            item.barang.nama_barang,
            item.tanggal_sewa.strftime("%d-%m-%Y"),
            item.tanggal_kembali.strftime("%d-%m-%Y"),
            item.total_harga,
            item.status_transaksi,
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