from django.db import models
from consulta.models import Consulta


class FormAPR(models.Model):

    RESPOSTAS1 = (

        ('Sim', 'Sim'),
        ('Não', 'Não')

    )

    RESPOSTAS2 = (

        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')

    )

    RESPOSTAS3 = (

        ('Sem alterações', 'Sem alterações'),
        ('Sintomático reversível com elevação do membro', 'Sintomático reversível com elevação do membro'),
        ('Com alteração objetiva cutânea', 'Com alteração objetiva cutânea'),
        ('Com alteração objetiva Aguda', 'Com alteração objetiva Aguda'),
        ('Com alteração objetiva Tardia(com fibrose)', 'Com alteração objetiva Tardia(com fibrose)'),
        ('Elefantíase', 'Elefantíase')

    )

    RESPOSTAS4 = (

        ('Fechada', 'Fechada'),
        ('Aberta', 'Aberta')

    )

    RESPOSTAS5 = (

        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')

    )

    RESPOSTAS6 = (

        ('Tipo I', 'Tipo I'),
        ('Tipo II', 'Tipo II'),
        ('Tipo III', 'Tipo III'),
        ('Tipo IV', 'Tipo IV'),
        ('Tipo V', 'Tipo V'),
        ('Tipo VI', 'Tipo VI'),
        ('Tipo VII', 'Tipo VII')

    )

    apr01 = models.FloatField(verbose_name='Peso')
    apr02 = models.FloatField(verbose_name='Altura')
    apr03 = models.FloatField(verbose_name='IMC')
    apr04 = models.FloatField(verbose_name='Circunferência abdominal')
    apr05 = models.DateField(verbose_name='Data da radioterapia')
    apr06 = models.DateField(verbose_name='Data final da radioterapia')
    apr07 = models.FloatField(verbose_name='Radiação total')
    apr08 = models.IntegerField(verbose_name='Número total de frações')
    apr09 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Quimioterapia')
    apr10 = models.DateField(verbose_name='Data da quimioterapia', null=True, blank=True)
    apr11 = models.DateField(verbose_name='Data final da quimioterapia', null=True, blank=True)
    apr12 = models.FloatField(verbose_name='Ciclo total', null=True, blank=True)
    apr13 = models.FloatField(verbose_name='Dose Total', null=True, blank=True)
    apr14 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Braquiterapia')
    apr15 = models.DateField(verbose_name='Data da braquiterapia', null=True, blank=True)
    apr16 = models.DateField(verbose_name='Data final da braquiterapia', null=True, blank=True)
    apr17 = models.FloatField(verbose_name='Radiação total', null=True, blank=True)
    apr18 = models.IntegerField(verbose_name='Número total de frações', null=True, blank=True)
    apr19 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Dor')
    apr20 = models.CharField(max_length=45, verbose_name='Local', null=True, blank=True)
    apr21 = models.IntegerField(choices=RESPOSTAS2, verbose_name='Escala Visual Analógica(EVA)')
    apr22 = models.FloatField(verbose_name='MID 21')
    apr23 = models.FloatField(verbose_name='MID 14')
    apr24 = models.FloatField(verbose_name='MID 07')
    apr25 = models.FloatField(verbose_name='MID BSP')
    apr26 = models.FloatField(verbose_name='MID 28')
    apr27 = models.FloatField(verbose_name='MID 35')
    apr28 = models.FloatField(verbose_name='MID TT')
    apr29 = models.FloatField(verbose_name='MID Pé')
    apr30 = models.FloatField(verbose_name='MIE 21')
    apr31 = models.FloatField(verbose_name='MIE 14')
    apr32 = models.FloatField(verbose_name='MIE 07')
    apr33 = models.FloatField(verbose_name='MIE BSP')
    apr34 = models.FloatField(verbose_name='MIE 28')
    apr35 = models.FloatField(verbose_name='MIE 35')
    apr36 = models.FloatField(verbose_name='MIE TT')
    apr37 = models.FloatField(verbose_name='MIE Pé')
    apr38 = models.FloatField(verbose_name='# 21')
    apr39 = models.FloatField(verbose_name='# 14')
    apr40 = models.FloatField(verbose_name='# 07')
    apr41 = models.FloatField(verbose_name='# BSP')
    apr42 = models.FloatField(verbose_name='# 28')
    apr43 = models.FloatField(verbose_name='# 35')
    apr44 = models.FloatField(verbose_name='# TT')
    apr45 = models.FloatField(verbose_name='# Pé')
    apr46 = models.CharField(max_length=45, choices=RESPOSTAS3, verbose_name='Resultado')
    apr47 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Sensação de peso')
    apr48= models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Pele esticada')
    apr49 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Formigamento')
    apr50 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Sensação de perna dura/movimentos reduzidos')
    apr51 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Alguma dificuldade para realizar atividade física')
    apr52 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Mudança de coloração')
    apr53 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Telangiectasias')
    apr54 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Veias varicosas')
    apr55 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Ulcera venosa')
    apr56 = models.CharField(max_length=10, choices=RESPOSTAS4, verbose_name='Ulcera venosa', null=True, blank=True)
    apr57 = models.IntegerField(choices=RESPOSTAS5, verbose_name='Flexão do quadril D')
    apr58 = models.IntegerField(choices=RESPOSTAS5, verbose_name='Flexão do quadril E')
    apr59 = models.IntegerField(choices=RESPOSTAS5, verbose_name='Extensão do joelho D')
    apr60 = models.IntegerField(choices=RESPOSTAS5, verbose_name='Extensão do joelho E')
    apr61 = models.IntegerField(choices=RESPOSTAS5, verbose_name='Dorsiflexão do tornozelo D')
    apr62 = models.IntegerField(choices=RESPOSTAS5, verbose_name='Dorsiflexão do tornozelo E')
    apr63 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Alterações da função INTESTINAL')
    apr64 = models.CharField(max_length=10, choices=RESPOSTAS6, verbose_name='Escala de Bristol')
    apr65 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Incontinência')
    apr66 = models.CharField(max_length=10, choices=RESPOSTAS1, verbose_name='Alterações da função VESICAL')
    
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return self.consulta
 