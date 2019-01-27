from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length = 50)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    contato = models.CharField(max_length=100)
