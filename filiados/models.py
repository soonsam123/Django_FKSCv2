from django.db import models

class Academia(models.Model):
    professor = models.CharField(max_length=100)
    nome_academia = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cep = models.IntegerField()
    num_reg = models.IntegerField()

    def __str__(self):
        return self.nome_academia +' - '+ self.cidade

class Atleta(models.Model):
    nome_atleta = models.CharField(max_length=100)
    academia = models.CharField(max_length=200)
    num_reg = models.IntegerField()

    def __str__(self):
        return self.nome_atleta

class Preta(models.Model):
    nome_preta = models.CharField(max_length=100)
    academia = models.CharField(max_length=200)
    num_reg = models.IntegerField()

    def __str__(self):
        return self.nome_preta
