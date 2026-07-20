from django.shortcuts import render, redirect

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