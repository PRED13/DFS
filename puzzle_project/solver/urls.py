from django.urls import path
from .views import resolver, home

urlpatterns = [
    path('', home),
    path('resolver/', resolver),
]