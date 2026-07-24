from django.contrib import admin
from .models import ProfilPengguna, Kategori, Barang, Penyewaan, Denda


admin.site.register(ProfilPengguna)
admin.site.register(Kategori)
admin.site.register(Barang)
admin.site.register(Penyewaan)
admin.site.register(Denda)