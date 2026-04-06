from django.contrib import admin
from django.urls import path, include
from solver.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]
