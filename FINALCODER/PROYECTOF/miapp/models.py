from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre}, {self.contraseña}"

class Jugadores(models.Model):
    
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=40)
    ultimo_equipo = models.CharField(max_length=40)
    nuevo_equipo = models.CharField(max_length=40)
    valor_de_traspaso = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.nacionalidad}, {self.ultimo_equipo}, {self.nuevo_equipo},{self.valor_de_traspaso}"
    