# tableros/views.py

from rest_framework import generics
from .models import Tarjeta
from .serializers import TarjetaSerializer
from rest_framework.permissions import IsAuthenticated

# Vista para crear una nueva tarjeta
class TarjetaCreateView(generics.CreateAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    permission_classes = (IsAuthenticated,)  # Solo usuarios autenticados pueden crear tarjetas

# Vista para listar todas las tarjetas
class TarjetaListView(generics.ListAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

# Vista para obtener los detalles de una tarjeta específica
class TarjetaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    permission_classes = (IsAuthenticated,)  # Solo usuarios autenticados pueden acceder