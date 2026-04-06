from django.urls import path
from . import views # Importamos todas las vistas de la app

urlpatterns = [
    path('', views.index, name='index'),        # Ruta raíz: tu_dominio.com/
    path('home/', views.home, name='home'),      # tu_dominio.com/home/
    path('resolver/', views.resolver, name='resolver'), # tu_dominio.com/resolver/
]
