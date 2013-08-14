from django.db import models

# Create your models here.

class Doenca(models.Model):
    nome = models.CharField(max_length=255)
    nomebusca = models.CharField(max_length=255)
    descricao = models.TextField()
