from django.contrib.auth.models import User
from django.db import models

class Noticia(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  

    Titulo = models.CharField('Título de la noticia', max_length=400, unique=True)
    Parrafo = models.TextField('Contenido de la Noticia', max_length=10000)
    Fecha_Publicacion = models.DateField('Fecha de publicación')
    imagen = models.ImageField(upload_to='Noticia/', blank=True, null=True)

    def __str__(self):
        return self.Titulo
