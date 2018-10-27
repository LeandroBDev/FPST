from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fec_creacion = models.DateTimeField(default=timezone.now)
    fec_publicacion = models.DateTimeField(blank=True, null=True)

    def publicado(self):
        self.fec_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo