from django.db import models

class RespostaTexto(models.Model):
    texto = models.CharField(max_length=30, null=False)

    def __str__(self):
        return str(self.texto)
