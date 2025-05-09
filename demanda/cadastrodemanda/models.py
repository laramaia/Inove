from django.db import models

# Create your models here.

class Demanda(models.Model):
    nome_demanda = models.CharField(max_length=30)
    descricao = models.CharField(max_length=600)
    nome_orientador = models.CharField(max_length=100, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome_demanda



