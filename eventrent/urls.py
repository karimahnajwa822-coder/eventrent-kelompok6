from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD

=======
>>>>>>> e43f98125f5d66dea1767357b9d875f11f76b2c0
    path('', include('penyewaan.urls')),
]