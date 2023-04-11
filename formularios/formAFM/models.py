from django.db import models
from consulta.models import Consulta
from respostatexto.models import RespostaTexto


SIM_NAO = [('Sim', 'Sim'), ('Não', 'Não')]
INTENSIDADE_PERDA = [('Muita', 'Muita'), ('Moderada', 'Moderada'), ('Pouca', 'Pouca')]
QUANTIDADE_PERDA = [('Gota', 'Gota'), ('Colher', 'Colher'), ('Jato', 'Jato')]
TIPO_INCONTINENCIA = [('Urgência', 'Urgência'), ('Esforço', 'Esforço'), 
                      ('Mista', 'Mista'), ('Transbordamento', 'Transbordamento')]
TOQUE_VAGINAL= [('Unidigital', 'Unidigital'), ('Bidigital', 'Bidigital')]
DOR = [('Ausente', 'Ausente'), ('Suave', 'Suave'), ('Severo', 'Severo')]
MUSCULATURA_ACESSORIA = [('Abdômen', 'Abdômen'), ('Glúteos', 'Glúteos'), ('Adutores', 'Adutores')]
ATIVIDADE_TONICA = [('Diminuído', 'Diminuído'), ('Normal','Normal'), ('Aumentado', 'Aumentado')]
FORCA_MUSCULATURA = [('0', 'Ausência de resposta muscular'),
                    ('1', 'Esboço de contração não sustentada'),
                    ('2', 'Presença de contração de pequena intensidade, mas que se sustenta'),
                    ('3', 'Contração moderada, sentida com o aumento da pressão intavaginal, que comprime os dedos do examinador com pequena elevação cranial da parede vaginal'),
                    ('4', 'Contração satisfatória, que aperta os dedos do examinador, com elevação da parede vaginal em direção à sínfise púbica'),
                    ('5', 'Contração forte, compressão firme dos dedos do examinador com movimento positivo em relação à sínfise púbica')]
ESCALA_NEW_PERFECT = [('P', 'Power'),
                    ('E', 'Endurance'),
                    ('R', 'Repetition'),
                    ('F', 'Fast')]

class FormAFM(models.Model):
    afm01 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Bebe 2 litros de água?')
    afm02  = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Sente vontade de urinar?')
    afm03 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Tem sensação de esvaziamento incompleto?')
    afm04 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Há gotejamento após esvaziament')
    afm05 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Você perde xixi?')
    
    afm06 = models.ManyToManyField(RespostaTexto, related_name='+',null=True, verbose_name='Circunstância da perda')

    afm07 = models.DateField(verbose_name='Data do último episódio:', null=True)
    afm08 = models.IntegerField(verbose_name='Perda diária:', null=True)
    afm09 = models.CharField(max_length=20, choices=INTENSIDADE_PERDA, verbose_name='Intensidade de perda:', null=True)
    afm10 = models.CharField(max_length=20, choices=QUANTIDADE_PERDA, verbose_name='Quantidade da perda:', null=True)
    afm11 = models.CharField(max_length=20, choices=TIPO_INCONTINENCIA, verbose_name='Tipo da incontinência urinária:', null=True)
    afm12 = models.DateField(verbose_name='Início dos sintomas:', null=True)
    afm13 = models.IntegerField(verbose_name='Frequência urinária diária:')
    afm14 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Dor para urinar?')
    afm15 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Infecção urinária?')
    afm16 = models.IntegerField(verbose_name='Quantas vezes?', null=True)
    afm17 = models.DateField(verbose_name='Qual a data do último episódio?', null=True)
    afm18 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name=' Uso de forro?')
    afm19 = models.IntegerField(verbose_name='Quantidade por dia?', null=True)
    afm20 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name=' Enurese?')
    afm21 = models.IntegerField(verbose_name='Quantidade de vezes?', null=True)
    afm22 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Nocturia?')
    afm23 = models.IntegerField(verbose_name='Quantidade de vezes?', null=True)
    afm24 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Sente protuberância ou algo caindo que pode ver ou sentir na área vaginal?')
    afm25 = models.CharField(max_length=20, choices=TOQUE_VAGINAL, verbose_name='Toque vaginal')
    afm26 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Desconforto ao toque vaginal?')
    afm27 = models.CharField(max_length=20, choices=DOR, verbose_name='Dor')
    afm28 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Sangramento Vaginal')
    afm29 = models.FloatField(verbose_name='Comprimento')
    afm30 = models.IntegerField(verbose_name='Segundos de contração do MAP sustentada')
    afm31 = models.IntegerField(verbose_name='Contrações rápidas sem perder a força')
    afm32= models.CharField(max_length=3, choices=SIM_NAO,  verbose_name='Usa musculatura acessória para contração?')
    
    afm33 = models.ManyToManyField(RespostaTexto, related_name='+',null=True, verbose_name='Musculatura')

    afm34= models.CharField(max_length=20, choices=ATIVIDADE_TONICA, verbose_name='Atividade tônica dos músculos do assoalho pélvico')
    afm35 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Contração do levantador do ânus/ contração em direção à sínfise púbica')
    afm36 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Exercícios com dilatadores')
    afm37 = models.IntegerField(verbose_name='Frequência dilatadores', null=True)
    afm38 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Relação sexual')
    afm39 = models.IntegerField(verbose_name='Frequência relação sexual', null=True)
    afm40 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Desconforto na relação sexual?', null=True)
    afm41 = models.CharField(max_length=20, choices=FORCA_MUSCULATURA, verbose_name='Força da musculatura do assoalho pélvico')
    afm42 = models.CharField(max_length=20, choices=ESCALA_NEW_PERFECT, verbose_name='Escala New Perfect')
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, related_name='consulta_afm', null=False)

    def __str__(self):
        return str(self.consulta)