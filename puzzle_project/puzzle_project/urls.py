from django.contrib import admin
from django.urls import path, include # Importante agregar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('solver.urls')), # Esto conecta TODO lo que esté en solver/urls.py
]
