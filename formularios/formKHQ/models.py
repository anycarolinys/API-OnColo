from django.db import models
from consulta.models import Consulta

class FormKHQ(models.Model):

    RESPOSTAS1 = (
        ('1', 'muito bom'),
        ('2', 'bom'),
        ('3', 'regular'),
        ('4', 'mau'),
        ('5', 'muito mau'),
    )

    RESPOSTAS2 = (
        ('1', 'nada'),
        ('2', 'um pouco'),
        ('3', 'moderadamente'),
        ('4', 'muito'),
    )

    RESPOSTAS3 = (
        ('1', 'nao aplicavel'),
        ('2', 'nada'),
        ('3', 'um pouco'),
        ('4', 'moderadamente'),
        ('5', 'muito'),
    )

    RESPOSTAS4 = (
        ('1', 'nunca'), 
        ('2', 'as vezes'),
        ('3', 'frequentemente'), 
        ('4', 'sempre'),
    )

    #Percepção Geral de Saúde
    khq01  = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    #Impacto da Incontinência
    khq02  = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='')
    #Limitações de Actividades Diárias
    khq03a = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='') 
    khq03b = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='')
    #Limitações Físicas
    khq04a = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='') 
    khq04b = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='') 
    #Limitações Sociais
    khq04c = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='') 
    khq04d = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='')
    #Relações Pessoais
    khq05a = models.CharField(max_length=1, choices=RESPOSTAS3, verbose_name='') 
    khq05b = models.CharField(max_length=1, choices=RESPOSTAS3, verbose_name='') 
    khq05c = models.CharField(max_length=1, choices=RESPOSTAS3, verbose_name='')
    #Emoções
    khq06a = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='')
    khq06b = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='')
    khq06c = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='')
    #Sono e Disposição
    khq07a = models.CharField(max_length=1, choices=RESPOSTAS4, verbose_name='')
    khq07b = models.CharField(max_length=1, choices=RESPOSTAS4, verbose_name='')
    #Medidas de Gravidade
    khq08a = models.CharField(max_length=1, choices=RESPOSTAS4, verbose_name='')
    khq08b = models.CharField(max_length=1, choices=RESPOSTAS4, verbose_name='')
    khq08c = models.CharField(max_length=1, choices=RESPOSTAS4, verbose_name='')
    khq08d = models.CharField(max_length=1, choices=RESPOSTAS4, verbose_name='')
    khq08e = models.CharField(max_length=1, choices=RESPOSTAS4, verbose_name='')

    consulta = models.ForeignKey(Consulta, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.consulta

