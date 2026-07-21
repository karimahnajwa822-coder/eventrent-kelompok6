from django.db import models


class Barang(models.Model):
    KONDISI_CHOICES = [
        ('Baik', 'Baik'),
        ('Sangat Baik', 'Sangat Baik'),
        ('Rusak', 'Rusak'),
    ]

    kode_barang = models.CharField(max_length=10, unique=True, verbose_name="ID")
    nama_barang = models.CharField(max_length=100)
    merk = models.CharField(max_length=100)
    stok = models.PositiveIntegerField(default=0)
    harga_sewa = models.DecimalField(max_digits=12, decimal_places=2)
    kondisi = models.CharField(max_length=20, choices=KONDISI_CHOICES, default='Baik')
    gambar = models.ImageField(upload_to='img/', blank=True, null=True)

    class Meta:
        ordering = ['kode_barang']

    def __str__(self):
        return f"{self.kode_barang} - {self.nama_barang}"