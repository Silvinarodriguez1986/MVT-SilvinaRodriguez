from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    relacion = models.CharField(max_length=40)
    nacimiento = models.IntegerField()
    edad = models.IntegerField()

def __str__(self) -> str:
        return f"Familia: {self.nombre} | apellido: {self.apellido} | edad: {self.edad} | relacion: {self.relacion} | nacimiento: {self.nacimiento} | edad: {self.edad}"
        