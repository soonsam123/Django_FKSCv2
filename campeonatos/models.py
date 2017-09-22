from django.db import models

class Campeonato(models.Model):
    nome_campeonato = models.CharField(max_length=400)
    est_cidade = models.CharField(max_length=100)
    data = models.CharField(max_length=50)
    endereco = models.CharField(max_length=500)
    cartaz = models.FileField(default='/static/images/logo.jpg')

    def __str__(self):
        return self.nome_campeonato

