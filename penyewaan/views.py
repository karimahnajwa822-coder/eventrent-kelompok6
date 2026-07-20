from django.shortcuts import render, redirect

<<<<<<< HEAD
def dashboard(request):
    return render(request, 'penyewaan/dashboard.html')

def penyewaan(request):
    return render(request, 'penyewaan/penyewaan.html')

def form_penyewaan(request):
    return render(request, 'penyewaan/form_penyewaan.html')
=======
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
>>>>>>> e43f98125f5d66dea1767357b9d875f11f76b2c0
