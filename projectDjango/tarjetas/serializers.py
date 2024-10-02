from rest_framework import serializers
from .models import Tarjeta  
from users.models import User  

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ('etiqueta', 'nombre_actividad', 'fecha_vencimiento', 
                  'descripcion', 'id_creador_tarjeta')

    def create(self, validated_data):
        tarjeta = Tarjeta.objects.create(
            etiqueta=validated_data['etiqueta'],
            nombre_actividad=validated_data['nombre_actividad'],
            fecha_vencimiento=validated_data['fecha_vencimiento'],
            descripcion=validated_data['descripcion'],
            id_creador_tarjeta=validated_data['id_creador_tarjeta']  # FK al User
        )
        return tarjeta