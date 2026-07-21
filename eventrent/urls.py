from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='detail-barang/')),
=======

urlpatterns = [
    path('admin/', admin.site.urls),
>>>>>>> main
    path('', include('penyewaan.urls')),
]