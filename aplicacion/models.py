from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre=models.CharField('nombre de genero', max_length=30, null=False)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('nombre pelicula', max_length=40, null=False)
    duracion=models.IntegerField()
    fecha=models.DateField()
    Genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True)

    def __str__(self):
        return self.nombre