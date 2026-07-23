from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Barang


from django.http import HttpResponse
from django.db.models import Sum
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from .models import Penyewaan

from reportlab.lib.units import cm
from datetime import datetime, date

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

def detail_barang(request):
    return render(request, 'penyewaan/detail_barang.html')

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
# DETAIL PENYEWAAN
# ======================

def detail_penyewaan(request, id):
    return render(request, 'penyewaan/detail_penyewaan.html')

# ======================
# EDIT PENYEWAAN
# ======================

def edit_penyewaan(request, id):
    return render(request, 'penyewaan/edit_penyewaan.html')


def hapus_penyewaan(request, id):
    return render(request, 'penyewaan/hapus_penyewaan.html')


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
# DATA DUMMY LAPORAN
# ======================

def get_data_laporan():

    return [
        {
            'penyewa': 'Fatma Auliya',
            'acara': 'Pernikahan',
            'barang': 'Tenda VIP',
            'jumlah': 1,
            'tanggal_sewa': date(2026, 7, 20),
            'tanggal_kembali': date(2026, 7, 22),
            'total_harga': 2500000,
            'status_transaksi': 'Sedang Disewa',
        },

        {
            'penyewa': 'Najwa',
            'acara': 'Seminar Kampus',
            'barang': 'Sound System',
            'jumlah': 1,
            'tanggal_sewa': date(2026, 7, 18),
            'tanggal_kembali': date(2026, 7, 20),
            'total_harga': 1200000,
            'status_transaksi': 'Selesai',
        },

        {
            'penyewa': 'Reva',
            'acara': 'Acara Organisasi',
            'barang': 'Kursi Futura',
            'jumlah': 50,
            'tanggal_sewa': date(2026, 7, 17),
            'tanggal_kembali': date(2026, 7, 21),
            'total_harga': 750000,
            'status_transaksi': 'Menunggu',
        },
    ]


# ======================
# LAPORAN
# ======================

def laporan(request):

    data_laporan = get_data_laporan()


    # FILTER TANGGAL
    tanggal_awal = request.GET.get('tanggal_awal')
    tanggal_akhir = request.GET.get('tanggal_akhir')


    if tanggal_awal and tanggal_akhir:

        tanggal_awal = datetime.strptime(
            tanggal_awal,
            "%Y-%m-%d"
        ).date()


        tanggal_akhir = datetime.strptime(
            tanggal_akhir,
            "%Y-%m-%d"
        ).date()


        data_laporan = [
            item for item in data_laporan
            if tanggal_awal <= item['tanggal_sewa'] <= tanggal_akhir
        ]


    # CARD STATISTIK

    total_barang = 15

    total_penyewaan = len(data_laporan)


    total_pendapatan = sum(
        item['total_harga']
        for item in data_laporan
    )


    belum_kembali = len([
        item for item in data_laporan
        if item['status_transaksi'] == "Sedang Disewa"
    ])


    context = {

        'laporan': data_laporan,

        'total_barang': total_barang,

        'total_penyewaan': total_penyewaan,

        'total_pendapatan': total_pendapatan,

        'belum_kembali': belum_kembali,

        'tanggal_awal': request.GET.get('tanggal_awal'),

        'tanggal_akhir': request.GET.get('tanggal_akhir'),

    }


    return render(
        request,
        'penyewaan/laporan.html',
        context
    )



# ======================
# EXPORT PDF
# ======================

def export_pdf(request):

    penyewaan = get_data_laporan()


    total_transaksi = len(penyewaan)


    total_pendapatan = sum(
        item['total_harga']
        for item in penyewaan
    )


    response = HttpResponse(
        content_type='application/pdf'
    )


    response['Content-Disposition'] = (
        'attachment; filename="laporan_penyewaan.pdf"'
    )


    doc = SimpleDocTemplate(
        response,
        pagesize=landscape(A4)
    )


    styles = getSampleStyleSheet()

    judul = styles['Heading1']

    judul.alignment = TA_CENTER


    elements = []


    elements.append(
        Paragraph(
            "<font size=18><b>LAPORAN PENYEWAAN EVENTRENT</b></font>",
            judul
        )
    )


    elements.append(
        Spacer(1,0.5*cm)
    )


    elements.append(
        Paragraph(
            f"Tanggal Cetak : {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )


    elements.append(
        Paragraph(
            f"Total Transaksi : {total_transaksi}",
            styles["Normal"]
        )
    )


    elements.append(
        Paragraph(
            f"Total Pendapatan : Rp {total_pendapatan:,}",
            styles["Normal"]
        )
    )


    elements.append(
        Spacer(1,0.7*cm)
    )


    data = [[
        "No",
        "Penyewa",
        "Acara",
        "Barang",
        "Jumlah",
        "Tanggal Sewa",
        "Tanggal Kembali",
        "Total",
        "Status"
    ]]


    for i,item in enumerate(penyewaan,start=1):

        data.append([

            str(i),

            item['penyewa'],

            item['acara'],

            item['barang'],

            str(item['jumlah']),

            item['tanggal_sewa'].strftime('%d-%m-%Y'),

            item['tanggal_kembali'].strftime('%d-%m-%Y'),

            f"Rp {item['total_harga']:,}",

            item['status_transaksi']

        ])



    table = Table(
        data,
        colWidths=[
            1*cm,
            3.5*cm,
            4*cm,
            3.5*cm,
            2*cm,
            3*cm,
            3*cm,
            3*cm,
            3.5*cm
        ]
    )


    table.setStyle(
        TableStyle([

            ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#0d6efd')),

            ('TEXTCOLOR',(0,0),(-1,0),colors.white),

            ('GRID',(0,0),(-1,-1),0.5,colors.grey),

            ('ALIGN',(0,0),(-1,-1),'CENTER'),

        ])
    )


    elements.append(table)


    doc.build(elements)


    return response