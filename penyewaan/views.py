from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

def barang(request):
    barang_list = Barang.objects.all()

    context = {
        'barang_list': barang_list,
    }

    return render(request, 'penyewaan/barang.html', context)

   

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

    # Mengambil semua data penyewaan
    data = Penyewaan.objects.select_related(
        'penyewa',
        'barang'
    ).order_by('-tanggal_sewa')


    tanggal_awal = request.GET.get('tanggal_awal')
    tanggal_akhir = request.GET.get('tanggal_akhir')


    if tanggal_awal and tanggal_akhir:
        data = data.filter(
            tanggal_sewa__range=[
                tanggal_awal,
                tanggal_akhir
            ]
        )


    total_penyewaan = data.count()

    total_pendapatan = (
        data.aggregate(
            total=Sum('total_harga')
        )['total'] or 0
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

    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = "Laporan Penyewaan"


    worksheet.append([
        "No",
        "Nama Pelanggan",
        "Peralatan",
        "Tanggal Pinjam",
        "Tanggal Kembali",
        "Total Bayar",
        "Status"
    ])


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


    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


    response["Content-Disposition"] = (
        'attachment; filename="Laporan_Penyewaan.xlsx"'
    )


    workbook.save(response)

    return response