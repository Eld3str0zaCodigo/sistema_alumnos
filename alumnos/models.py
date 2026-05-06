from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()  # en años o semestres, asumir años

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    foto = models.ImageField(upload_to='alumnos/', blank=True, null=True)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
