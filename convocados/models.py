from django.db import models

class Convocado_campeonato(models.Model):
    nome_campeonato = models.CharField(max_length=400)
    est_cidade = models.CharField(max_length=100)
    data = models.CharField(max_length=50)
    cartaz = models.FileField(default='/static/images/logo.jpg')

    def __str__(self):
        return self.nome_campeonato

class Convocados(models.Model):
    Convocado_campeonato = models.ForeignKey(Convocado_campeonato, on_delete=models.CASCADE)
    nome = models.CharField(max_length=500)
    academia = models.CharField(max_length=200)
    faixa = models.CharField(max_length=100)
    reg_fed = models.IntegerField()

    def __str__(self):
        return self.nome

