from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo


