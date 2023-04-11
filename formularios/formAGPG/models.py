from django.db import models
from consulta.models import Consulta

SIM_NAO = [('Sim', 'Sim'), ('Não', 'Não')]

IMC_CHOICES = [
        ('Soberest', 'Soberest'),
        ('Obesidade grau I', 'Obesidade grau I'),
        ('Obesidade grau II', 'Obesidade grau II'),
        ('Obesidade grau III', 'Obesidade grau III')
]

RESULTADO_CHOICES = [
    ('Sem alterações', 'Sem alterações'),
    ('Sintomático reversível com elevação do membro', 'Sintomático reversível com elevação do membro'),
    ('Com alteração objetiva cutânea', 'Com alteração objetiva cutânea'),
    ('Aguda', 'Aguda'),
    ('Tardia (com fibrose)', 'Tardia (com fibrose)'),
    ('Elefantíase', 'Elefantíase')
]

TIPO_ULCERA = [('Fechada', 'Fechada'), ('Aberta', 'Aberta')]

FORCA_MMII = [('1', '1'), ('2', '2'),
           ('3', '3'), ('4 ', '4 '), ('5 ', '5 ')]

ESCALA_BRISTOL = [('Tipo I', 'Tipo I'), ('Tipo II', 'Tipo II'),('Tipo III', 'Tipo III'),
                  ('Tipo IV', 'Tipo IV'),('Tipo V', 'Tipo V')]

class FormAGPG(models.Model):
    agpg01 = models.FloatField(verbose_name='Peso')
    agpg02 = models.FloatField(verbose_name='Altura')
    agpg03 = models.CharField(max_length=20, verbose_name='IMC', choices=IMC_CHOICES)
    agpg04 = models.FloatField(verbose_name='Circunferência abdominal')

    # LINFEDEMA
    agpg05 = models.FloatField(max_length=10, verbose_name='MID 21')
    agpg06 = models.FloatField(max_length=10, verbose_name='MID 14')
    agpg07 = models.FloatField(max_length=10, verbose_name='MID 07')
    agpg08 = models.FloatField(max_length=10, verbose_name='MID BSP')
    agpg09 = models.FloatField(max_length=10, verbose_name='MID 28')
    agpg10 = models.FloatField(max_length=10, verbose_name='MID 35')
    agpg11 = models.FloatField(max_length=10, verbose_name='MID TT')
    agpg12 = models.FloatField(max_length=10, verbose_name='MID Pé')
    agpg13 = models.FloatField(max_length=10, verbose_name='MIE 21')
    agpg14 = models.FloatField(max_length=10, verbose_name='MIE 14')
    agpg15 = models.FloatField(max_length=10, verbose_name='MIE 07')
    agpg16 = models.FloatField(max_length=10, verbose_name='MIE BSP')
    agpg17 = models.FloatField(max_length=10, verbose_name='MIE 28')
    agpg18 = models.FloatField(max_length=10, verbose_name='MIE 35')
    agpg19 = models.FloatField(max_length=10, verbose_name='MIE TT')
    agpg20 = models.FloatField(max_length=10, verbose_name='MIE Pé')
    agpg21 = models.FloatField(max_length=10, verbose_name='# 21')
    agpg22 = models.FloatField(max_length=10, verbose_name='# 14')
    agpg23 = models.FloatField(max_length=10, verbose_name='# 07')
    agpg24 = models.FloatField(max_length=10, verbose_name='# BSP')
    agpg25 = models.FloatField(max_length=10, verbose_name='# 28')
    agpg26 = models.FloatField(max_length=10, verbose_name='# 35')
    agpg27 = models.FloatField(max_length=10, verbose_name='# TT')
    agpg28 = models.FloatField(max_length=10, verbose_name='# Pé')

    # RESULTADO
    agpg29 = models.CharField(max_length=50, verbose_name='Resultado', choices=RESULTADO_CHOICES)

    # AUTO RELATO
    agpg30 = models.CharField(max_length=3, verbose_name='Sensação de peso', choices=SIM_NAO)
    agpg31 = models.CharField(max_length=3, verbose_name='Pele esticada ', choices=SIM_NAO)
    agpg32 = models.CharField(max_length=3, verbose_name='Formigamento', choices=SIM_NAO)
    agpg33 = models.CharField(max_length=3, verbose_name='Sensação de perna dura/movimentos reduzidos', choices=SIM_NAO)
    agpg34 = models.CharField(max_length=3, verbose_name='Alguma dificuldade para realizar atividade física', choices=SIM_NAO)
    
    # ALTERAÇÃO VENOSA
    agpg35 = models.CharField(max_length=3, verbose_name='Mudança de coloração', choices=SIM_NAO)
    agpg36 = models.CharField(max_length=3, verbose_name='Telangiectasias', choices=SIM_NAO)
    agpg37 = models.CharField(max_length=3, verbose_name='Veias varicosas', choices=SIM_NAO)
    agpg38 = models.CharField(max_length=3, verbose_name='Úlcera venosa', choices=SIM_NAO)
    agpg39 = models.CharField(max_length=20, verbose_name='Tipo úlcera venosa', choices=TIPO_ULCERA, null=True)
    agpg40 = models.CharField(max_length=3, verbose_name='Lesão nervosa periférica', choices=SIM_NAO)    
    
    # AVALIAÇÃO DE FORÇA DE MMII (Teste de Oxford)
    agpg41 = models.IntegerField(verbose_name='Flexão do quadril direito', choices=FORCA_MMII)    
    agpg42 = models.IntegerField(verbose_name='Flexão do quadril esquerdo', choices=FORCA_MMII)    
    agpg43 = models.IntegerField(verbose_name='Extensão do joelho direito', choices=FORCA_MMII)    
    agpg44 = models.IntegerField(verbose_name='Extensão do joelho esquerdo', choices=FORCA_MMII)    
    agpg45 = models.IntegerField(verbose_name='Dorsiflexão do tornozelo direito', choices=FORCA_MMII)    
    agpg46 = models.IntegerField(verbose_name='Dorsiflexão do tornozelo esquerdo', choices=FORCA_MMII)    
    
    # AVALIAÇÃO DA FUNÇÃO INTESTINAL E/OU VESICAL
    agpg47 = models.CharField(max_length=3, verbose_name='Alterações da função intestinal', choices=SIM_NAO)    
    agpg48 = models.CharField(max_length=20, verbose_name='Escala de Bristol', choices=ESCALA_BRISTOL)    
    agpg49 = models.CharField(max_length=3, verbose_name='Incontinência', choices=SIM_NAO)    
    agpg50 = models.CharField(max_length=3, verbose_name='Alterações da função vesical', choices=SIM_NAO)    

    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, related_name='consulta_agpg', null=False)

    def __str__(self):
        return str(self.consulta)