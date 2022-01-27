from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateField()
    archivados = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo