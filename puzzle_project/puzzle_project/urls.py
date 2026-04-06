from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('solver.urls')),   # ← ESTA LÍNEA FALTABA
    path('admin/', admin.site.urls),
    path('api/', include('solver.urls')),
]