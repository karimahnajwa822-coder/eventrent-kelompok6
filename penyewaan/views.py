from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date

from .models import (
    ProfilPengguna,
    Barang,
    Penyewaan,
    Denda,
)
# ======================
# LOGIN
# ======================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            profil = ProfilPengguna.objects.get(user=user)

            if profil.status_akun != "Aktif":

                messages.error(
                    request,
                    "Akun Anda masih menunggu persetujuan Operator."
                )

                return redirect("login")

            login(request, user)

            print("Username:", user.username)
            print("Role:", profil.role)

            if profil.role == "Administrator":
                return redirect("dashboard")

            elif profil.role == "Operator":
                return redirect("dashboard_operator")

            elif profil.role == "Dosen":
                return redirect("dashboard_dosen")

        else:

            messages.error(
                request,
                "Username atau Password salah."
            )

    return render(request, "penyewaan/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
# ======================
# REGISTER
# ======================

def register_view(request):
    if request.method == "POST":
        return redirect('login')

    return render(request, 'penyewaan/register.html')

# ======================
# REGISTER DOSEN
# ======================

def register_dosen(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        no_hp = request.POST.get("no_hp")
        alamat = request.POST.get("alamat")

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username sudah digunakan."
            )

            return redirect("register_dosen")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        ProfilPengguna.objects.create(
            user=user,
            no_hp=no_hp,
            alamat=alamat,
            role="Dosen",
            status_akun="Menunggu Persetujuan"
        )

        messages.success(
            request,
            "Registrasi berhasil. Silakan tunggu persetujuan Operator."
        )

        return redirect("login")

    return render(
        request,
        "penyewaan/register_dosen.html"
    )

# ======================
# PERSETUJUAN DOSEN
# ======================

def persetujuan_dosen(request):

    data_dosen = ProfilPengguna.objects.filter(
        role="Dosen",
        status_akun="Menunggu Persetujuan"
    )

    return render(
        request,
        "penyewaan/persetujuan_dosen.html",
        {
            "data_dosen": data_dosen
        }
    )

# ======================
# SETUJUI DOSEN
# ======================

def setujui_dosen(request, id):

    profil = ProfilPengguna.objects.get(id=id)

    profil.status_akun = "Aktif"

    profil.save()

    messages.success(
        request,
        "Dosen berhasil disetujui."
    )

    return redirect("dashboard_operator")
# ======================
# TOLAK DOSEN
# ======================

def tolak_dosen(request, id):

    profil = ProfilPengguna.objects.get(id=id)

    profil.status_akun = "Ditolak"

    profil.save()

    return redirect("dashboard_operator")

# ======================
# TAMBAH OPERATOR
# ======================

def tambah_operator(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        no_hp = request.POST.get("no_hp")
        alamat = request.POST.get("alamat")

        if User.objects.filter(username=username).exists():

            messages.error(request, "Username sudah digunakan.")

            return redirect("tambah_operator")

        user = User.objects.create_user(

            username=username,
            email=email,
            password=password

        )

        ProfilPengguna.objects.create(

            user=user,
            no_hp=no_hp,
            alamat=alamat,
            role="Operator",
            status_akun="Aktif"

        )

        messages.success(request, "Operator berhasil ditambahkan.")

        return redirect("tambah_operator")

    return render(request, "penyewaan/tambah_operator.html")

# ======================
# DASHBOARD
# ======================

def dashboard(request):
    return render(request, 'penyewaan/dashboard.html')

# ======================
# DASHBOARD DOSEN
# ======================

def dashboard_dosen(request):
    return render(request, 'penyewaan/dashboard_dosen.html')

# ======================
# DASHBOARD OPERATOR
# ======================

def dashboard_operator(request):

    dosen_pending = ProfilPengguna.objects.filter(
        role="Dosen",
        status_akun="Menunggu Persetujuan"
    )


    context = {

        "dosen_pending": dosen_pending

    }


    return render(
        request,
        "penyewaan/dashboard_operator.html",
        context
    )

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
    barang_list = Barang.objects.all()

    context = {
        'barang_list': barang_list,
    }

    return render(
        request,
        'penyewaan/barang.html',
        context
    )

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

    daftar_barang = Barang.objects.filter(status="Tersedia")

    if request.method == "POST":

        barang = Barang.objects.get(
            id=request.POST.get("barang")
        )

        Penyewaan.objects.create(
            penyewa=request.user,
            nama_acara=request.POST.get("nama_acara"),
            tanggal_sewa=request.POST.get("tanggal_sewa"),
            tanggal_kembali=request.POST.get("tanggal_kembali"),
            barang=barang,
            jumlah=request.POST.get("jumlah"),
            lokasi=request.POST.get("lokasi"),
            catatan=request.POST.get("catatan"),
            status_transaksi="Menunggu Persetujuan"
        )

        messages.success(
            request,
            "Pengajuan peminjaman berhasil dikirim."
        )

        return redirect("dashboard_dosen")

    return render(
        request,
        "penyewaan/form_penyewaan.html",
        {
            "barang": daftar_barang
        }
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

# ======================
# HAPUS PENYEWAAN
# ======================

def hapus_penyewaan(request, id):

    sewa = Penyewaan.objects.get(id=id)

    sewa.delete()

    messages.success(
        request,
        "Data penyewaan berhasil dihapus."
    )

    return redirect("penyewaan")
# ======================
# KERANJANG
# ======================

def keranjang(request):

    keranjang_data = request.session.get(
        "keranjang",
        {}
    )

    context = {
        "keranjang": keranjang_data,
    }

    return render(
        request,
        "penyewaan/keranjang.html",
        context
    )


# ======================
# LAPORAN
# ======================
def laporan(request):
    return render(request, 'penyewaan/laporan.html')

# ======================
# PERSETUJUAN PEMINJAMAN
# ======================

def persetujuan_peminjaman(request):

    data = Penyewaan.objects.filter(
        status_transaksi="Menunggu Persetujuan"
    )

    return render(
        request,
        "penyewaan/persetujuan_peminjaman.html",
        {
            "data": data
        }
    )
# ======================
# SETUJUI PEMINJAMAN
# ======================

def setujui_peminjaman(request, id):

    sewa = Penyewaan.objects.get(id=id)

    barang = sewa.barang

    # kurangi stok
    barang.stok -= sewa.jumlah

    # jika stok habis
    if barang.stok <= 0:
        barang.stok = 0
        barang.status = "Dipinjam"

    barang.save()

    # ubah status peminjaman
    sewa.status_transaksi = "Disetujui"
    sewa.save()

    messages.success(
        request,
        "Peminjaman berhasil disetujui."
    )

    return redirect("persetujuan_peminjaman")
# ======================
# TOLAK PEMINJAMAN
# ======================

def tolak_peminjaman(request, id):

    sewa = Penyewaan.objects.get(id=id)

    sewa.status_transaksi = "Ditolak"

    sewa.save()

    messages.success(
        request,
        "Peminjaman ditolak."
    )

    return redirect("persetujuan_peminjaman")

# ======================
# UPLOAD BUKTI PEMBAYARAN
# ======================

def upload_bukti(request, id):

    sewa = Penyewaan.objects.get(id=id)

    if request.method == "POST":

        sewa.bukti_bayar = request.FILES.get("bukti")

        sewa.status_transaksi = "Menunggu Verifikasi"

        sewa.save()

        messages.success(
            request,
            "Bukti pembayaran berhasil dikirim."
        )

        return redirect("dashboard_dosen")

    return render(
        request,
        "penyewaan/upload_bukti.html",
        {
            "sewa": sewa
        }
    )

# ======================
# VERIFIKASI PEMBAYARAN
# ======================

def verifikasi_pembayaran(request):

    data = Penyewaan.objects.filter(
        status_transaksi="Menunggu Verifikasi"
    )

    return render(
        request,
        "penyewaan/verifikasi_pembayaran.html",
        {
            "data": data
        }
    )
# ======================
# SETUJUI PEMBAYARAN
# ======================

def setujui_pembayaran(request, id):

    sewa = Penyewaan.objects.get(id=id)

    sewa.status_transaksi = "Sedang Disewa"

    sewa.barang.status = "Dipinjam"

    sewa.barang.save()

    sewa.save()

    messages.success(
        request,
        "Pembayaran berhasil diverifikasi."
    )

    return redirect("verifikasi_pembayaran")
# ======================
# TOLAK PEMBAYARAN
# ======================

def tolak_pembayaran(request, id):

    sewa = Penyewaan.objects.get(id=id)

    sewa.status_transaksi = "Disetujui"

    sewa.bukti_bayar = None

    sewa.save()

    messages.error(
        request,
        "Bukti pembayaran ditolak."
    )

    return redirect("verifikasi_pembayaran")
# ======================
# PENGEMBALIAN BARANG
# ======================
def pengembalian_barang(request):

    data = Penyewaan.objects.filter(
        status_transaksi="Sedang Disewa"
    )

    return render(
        request,
        "penyewaan/pengembalian_barang.html",
        {
            "data": data
        }
    )
# ======================
# PROSES PENGEMBALIAN
# ======================

def proses_pengembalian(request, id):

    sewa = Penyewaan.objects.get(id=id)

    hari_ini = date.today()

    terlambat = (hari_ini - sewa.tanggal_kembali).days

    denda = 0

    if terlambat > 0:

        biaya = Denda.objects.first()

        if biaya:

            denda = terlambat * biaya.biaya_per_hari

    sewa.barang.stok += sewa.jumlah
    sewa.barang.status = "Tersedia"

    sewa.barang.save()

    messages.success(
        request,
        f"Barang berhasil dikembalikan. Total denda: Rp {denda:,}"
    )

    return redirect("pengembalian_barang")