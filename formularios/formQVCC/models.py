from django.db import models

from consulta.models import Consulta

class FormQVCC(models.Model):

    RESPOSTAS1 = (
            ('1', 'nao'),
            ('2', 'pouco'),
            ('3', 'moderado'),
            ('4', 'muito'),
        )

    qvc31 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc32 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc33 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc34 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc35 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc36 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc37 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc38 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc39 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc40 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc41 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc42 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc43 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc44 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc45 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc46 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc47 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc48 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc49 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc50 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc51 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc52 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc53 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')
    qvc54 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='')

    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.consulta)