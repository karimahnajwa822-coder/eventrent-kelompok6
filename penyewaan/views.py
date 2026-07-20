from django.shortcuts import render

def dashboard(request):
    return render(request, 'penyewaan/dashboard.html')

def penyewaan(request):
    return render(request, 'penyewaan/penyewaan.html')

def form_penyewaan(request):
    return render(request, 'penyewaan/form_penyewaan.html')