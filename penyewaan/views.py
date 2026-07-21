from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Barang


def detail_barang(request):
    barang_list = Barang.objects.all()
    context = {
        'barang_list': barang_list,
    }
    return render(request, 'penyewaan/detail_barang.html', context)


def sewa_barang(request, barang_id):
    """Tambahkan 1 barang ke keranjang (disimpan di session)."""
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
    messages.success(request, f'"{barang.nama_barang}" berhasil ditambahkan ke keranjang.')
    return redirect('detail_barang')


def keranjang(request):
    # Bagian ini dikerjakan oleh temanmu
    return render(request, 'penyewaan/keranjang.html')