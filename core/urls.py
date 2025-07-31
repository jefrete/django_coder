from django.urls import path
from .views import inicio  # 👈 Esto funciona si la función se llama "inicio" en views.py

urlpatterns = [
    path('', inicio, name='inicio'),
]
