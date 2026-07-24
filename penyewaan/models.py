from django.db import models
from django.contrib.auth.models import User


# ==========================================
# PROFIL PENGGUNA
# ==========================================

class ProfilPengguna(models.Model):

    STATUS_PILIHAN = [
        ('Menunggu Persetujuan', 'Menunggu Persetujuan'),
        ('Aktif', 'Aktif'),
        ('Ditolak', 'Ditolak'),
    ]

    ROLE_PILIHAN = [
        ('Administrator', 'Administrator'),
        ('Operator', 'Operator'),
        ('Dosen', 'Dosen'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_hp = models.CharField(max_length=15)
    alamat = models.TextField()

    status_akun = models.CharField(
        max_length=25,
        choices=STATUS_PILIHAN,
        default='Menunggu Persetujuan'
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_PILIHAN,
        default='Dosen'
    )

    def __str__(self):
        return self.user.username


# ==========================================
# KATEGORI
# ==========================================

class Kategori(models.Model):

    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kategori


# ==========================================
# BARANG / PERALATAN
# ==========================================

class Barang(models.Model):

    STATUS_BARANG = [
        ('Tersedia', 'Tersedia'),
        ('Dipinjam', 'Dipinjam'),
    ]

    kategori = models.ForeignKey(
        Kategori,
        on_delete=models.CASCADE
    )

    nama_barang = models.CharField(max_length=100)

    gambar = models.ImageField(
        upload_to='barang/'
    )

    stok = models.IntegerField()

    harga_hari = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_BARANG,
        default='Tersedia'
    )

    def __str__(self):
        return self.nama_barang


# ==========================================
# PENYEWAAN
# ==========================================

class Penyewaan(models.Model):

    STATUS_TX = [
        ('Menunggu Persetujuan', 'Menunggu Persetujuan'),
        ('Ditolak', 'Ditolak'),
        ('Disetujui', 'Disetujui'),
        ('Menunggu Verifikasi', 'Menunggu Verifikasi'),
        ('Lunas', 'Lunas'),
        ('Sedang Disewa', 'Sedang Disewa'),
        ('Selesai', 'Selesai'),
    ]

    penyewa = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    barang = models.ForeignKey(
        Barang,
        on_delete=models.CASCADE
    )

    nama_acara = models.CharField(max_length=150)

    tanggal_sewa = models.DateField()

    tanggal_kembali = models.DateField()

    jumlah = models.IntegerField()

    lokasi = models.TextField()

    catatan = models.TextField(
        blank=True,
        null=True
    )

    total_harga = models.IntegerField(
        blank=True,
        null=True
    )

    status_transaksi = models.CharField(
        max_length=30,
        choices=STATUS_TX,
        default='Menunggu Persetujuan'
    )

    bukti_bayar = models.ImageField(
        upload_to='bukti_tf/',
        blank=True,
        null=True
    )

    kondisi_kembali = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nama_acara} - {self.penyewa.username}"

# ==========================================
# DENDA
# ==========================================

class Denda(models.Model):

    nama = models.CharField(
        max_length=100,
        default="Denda Keterlambatan"
    )

    biaya_per_hari = models.IntegerField()

    def __str__(self):
        return self.nama