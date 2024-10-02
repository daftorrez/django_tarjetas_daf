# tableros/urls.py

from django.urls import path
from .views import TarjetaCreateView, TarjetaListView, TarjetaDetailView

urlpatterns = [
    path('tarjetas/', TarjetaListView.as_view(), name='tarjeta-list'),  # Listar tarjetas
    path('tarjetas/create/', TarjetaCreateView.as_view(), name='tarjeta-create'),  # Crear tarjeta
    path('tarjetas/<int:pk>/', TarjetaDetailView.as_view(), name='tarjeta-detail'),  # Detalles de tarjeta
]