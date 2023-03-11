from django.db import models
from instituicao.models import Instituicao

class Fisioterapeuta(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=45)
    sobrenome = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=45)
    instituicao = models.ForeignKey(Instituicao, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
