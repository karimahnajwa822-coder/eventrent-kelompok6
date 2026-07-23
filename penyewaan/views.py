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
from datetime import datetime


def login_view(request):
    if request.method == "POST":
        return redirect('dashboard')
    return render(request, 'penyewaan/login.html')


def register_view(request):
    if request.method == "POST":
        return redirect('login')
    return render(request, 'penyewaan/register.html')


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
# BARANG (hanya SATU fungsi ini!)
# ======================

    context = {
        'barang_list': barang_list,
    }

    return render(request, 'penyewaan/barang.html', context)

    


def barang(request):
    barang_list = Barang.objects.all()
    context = {'barang_list': barang_list}
    return render(request, 'penyewaan/barang.html', context)


def sewa_barang(request, barang_id):
    barang = get_object_or_404(Barang, id=barang_id)

    keranjang = request.session.get('keranjang', {})
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

    return redirect('keranjang')   # <-- diubah ke 'keranjang', bukan 'detail_barang'


def detail_barang(request):
    return render(request, 'penyewaan/detail_barang.html')


# ======================
# PENYEWAAN
# ======================

def penyewaan(request):
    return render(request, 'penyewaan/penyewaan.html')


def form_penyewaan(request):
    return render(request, 'penyewaan/form_penyewaan.html')


def detail_penyewaan(request, id):
    return render(request, 'penyewaan/detail_penyewaan.html')


def edit_penyewaan(request, id):
    return render(request, 'penyewaan/edit_penyewaan.html')


def hapus_penyewaan(request, id):
    return render(request, 'penyewaan/hapus_penyewaan.html')


def keranjang(request):
    keranjang_data = request.session.get('keranjang', {})
    context = {'keranjang': keranjang_data}
    return render(request, 'penyewaan/keranjang.html', context)


def laporan(request):

    return render(request, 'penyewaan/laporan.html')

    return render(
        request,
        'penyewaan/laporan.html'
    )
def export_pdf(request):
    
    print("Jumlah data:", Penyewaan.objects.count())
# ======================
# DATA DUMMY UNTUK PDF
# ======================

    penyewaan = [
        {
            'penyewa': 'Fatma Auliya',
            'acara': 'Pernikahan',
            'barang': 'Tenda VIP',
            'jumlah': 1,
            'tanggal_sewa': '20-07-2026',
            'tanggal_kembali': '22-07-2026',
            'total': 'Rp 2.500.000',
            'status': 'Sedang Disewa',
        },
        {
            'penyewa': 'Najwa',
            'acara': 'Seminar Kampus',
            'barang': 'Sound System',
            'jumlah': 1,
            'tanggal_sewa': '18-07-2026',
            'tanggal_kembali': '20-07-2026',
            'total': 'Rp 1.200.000',
            'status': 'Selesai',
        },
        {
            'penyewa': 'Reva',
            'acara': 'Acara Organisasi',
            'barang': 'Kursi Futura',
            'jumlah': 50,
            'tanggal_sewa': '17-07-2026',
            'tanggal_kembali': '21-07-2026',
            'total': 'Rp 750.000',
            'status': 'Menunggu',
        },
    ]

    # Statistik dummy
    total_transaksi = len(penyewaan)
    total_pendapatan = 'Rp 4.450.000'

    # Response PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="laporan_penyewaan.pdf"'

    # Dokumen
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

    elements.append(Spacer(1, 0.5 * cm))

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
            f"Total Pendapatan : {total_pendapatan}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 0.7 * cm))

    # Header tabel
    data = [[
        "No",
        "Penyewa",
        "Nama Acara",
        "Barang",
        "Jumlah",
        "Tanggal Sewa",
        "Tanggal Kembali",
        "Total",
        "Status"
    ]]

    # Isi tabel
    for i, item in enumerate(penyewaan, start=1): data.append([ str(i), item['penyewa'], item['acara'], item['barang'], str(item['jumlah']), item['tanggal_sewa'], item['tanggal_kembali'], item['total'], item['status'], ])

    # Membuat tabel
    table = Table(data, colWidths=[
    1*cm,
    3.5*cm,
    4*cm,
    3.5*cm,
    2*cm,
    3*cm,
    3*cm,
    3*cm,
    3.5*cm
])

    table.setStyle(TableStyle([

    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d6efd')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 10),

    ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),

    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),

    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

    ('BOTTOMPADDING', (0,0), (-1,0), 10),
    ('TOPPADDING', (0,0), (-1,-1), 6),

]))

    elements.append(table)

    doc.build(elements)
    elements.append(Spacer(1, 1 * cm))

    elements.append(
        Paragraph(
            "<font size=9 color='grey'>Dokumen ini dibuat secara otomatis oleh sistem EventRent.</font>",
            styles["Normal"]
        )
    )
    return response
    

