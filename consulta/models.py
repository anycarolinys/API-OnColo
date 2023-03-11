from django.db import models
from paciente.models import Paciente
from fisioterapeuta.models import Fisioterapeuta

class Consulta(models.Model):
    data_consulta = models.DataField()
    data_retorno = models.DataField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fisioterapeuta = models.ForeignKey(Fisioterapeuta, on_delete=models.CASCADE)
    #formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)

    def __str__(self):
        return self.paciente



