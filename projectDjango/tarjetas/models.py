from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarjeta(models.Model):
    #id_tarjeta = models.AutoField(primary_key=True) #Clave primaria de la tarjeta
    etiqueta = models.CharField(max_length=20)
    nombre_actividad = models.CharField(max_length=150)
    fecha_creacion = models.DateField(auto_now_add=True)  # Se establece automáticamente al crear el objeto
    fecha_vencimiento = models.DateField()
    descripcion = models.CharField(max_length=500)
    #faltaría añadirle id_creador_tarjeta
    id_creador_tarjeta = models.ForeignKey(User, on_delete=models.CASCADE) #sería la clave foránea

    def __str__(self):
        return self.nombre_actividad
