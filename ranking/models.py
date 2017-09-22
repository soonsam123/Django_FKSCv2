from django.db import models

class Rank_campeonato(models.Model):
    nome_campeonato = models.CharField(max_length=400)
    est_cidade = models.CharField(max_length=100)
    data = models.CharField(max_length=50)
    cartaz = models.FileField(default='/static/images/logo.jpg')

    def __str__(self):
        return self.nome_campeonato

class Categoria(models.Model):
    rank_campeonato = models.ForeignKey(Rank_campeonato, on_delete=models.CASCADE)
    idade = models.CharField(max_length=100)
    faixa = models.CharField(max_length=100)
    sexo = models.CharField(max_length=50)
    modalidade = models.CharField(max_length=50)
    primeiro = models.CharField(max_length=200)
    acad_primeiro = models.CharField(max_length=200)
    segundo = models.CharField(max_length=200)
    acad_segundo = models.CharField(max_length=200)
    terceiro = models.CharField(max_length=200)
    acad_terceiro = models.CharField(max_length=200)

    def __str__(self):
        return self.idade +'/'+ self.faixa +'/'+ self.sexo +'/'+ self.modalidade

