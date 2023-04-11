from django.db import models
from respostatexto.models import RespostaTexto
from consulta.models import Consulta

IMC_CHOICES = [
    ('Soberest', 'Soberest'),
    ('Obesidade grau I', 'Obesidade grau I'),
    ('Obesidade grau II', 'Obesidade grau II'),
    ('Obesidade grau III', 'Obesidade grau III')
]

SIM_NAO = [('Sim', 'Sim'), ('Não', 'Não')]

SINTOMAS_MENOPAUSA = [
    ('Fogachos', 'Fogachos'),
    ('Ressecamento vaginal', 'Ressecamento vaginal'),
    ('Insônia', 'Insônia'),
    ('Depressão', 'Depressão'),
    ('Outros', 'Outros'),
]

COR_PELE = [
    ('Preta', 'Preta'),
    ('Parda', 'Parda'),
    ('Branca', 'Branca'),
    ('Indígena', 'Indígena'),
    ('Amarela', 'Amarela'),
]

ESTADO_CIVIL = [
    ('Casada/União estável', 'Casada/União estável'),
    ('Solteira', 'Solteira'),
    ('Divorciada/Separada', 'Divorciada/Separada'),
    ('Viúva', 'Viúva'),
]


PROFISSAO = [
    ('Do lar', 'Do lar'),
    ('Em atividade ', 'Em atividade'),
    ('Aposentada', 'Aposentada'),
    ('Desempregada', 'Desempregada'),
]

RENDA_FAMILIAR = [
    ('Menor que 1 salário', 'Menor que 1 salário'),
    ('Entre 1 e 3 salário(s)', 'Entre 1 e 3 salário(s)'),
    ('Maior que 3 salários', 'Maior que 3 salários'),
    ('Sem renda', 'Sem renda'),
    ('Sem informação', 'Sem informação'),
]

ESCOLARIDADE = [
    ('Analfabeta', 'Analfabeta'),
    ('Fundamental incompleto', 'Fundamental incompleto'),
    ('Fundamental completo', 'Fundamental completo'),
    ('Ensino médio incompleto', 'Ensino médio incompleto'),
    ('Ensino médio completo', 'Ensino médio completo'),
    ('Superior incompleto', 'Superior incompleto'),
    ('Superior completo', 'Superior completo'),
    ('Pós-graduação', 'Pós-graduação'),
]

VINCULO_PREVIDENCIARIO = [
    ('Não possui', 'Não possui'),
    ('Aposentada', 'Aposentada'),
    ('Beneficiária', 'Beneficiária'),
]

FIGO = [
    ('0','0'),
    ('I A','I A'),
    ('I B', 'I B'), 
    ('II A', 'II A'),   
    ('II B', 'II B'),   
    ('III A', 'III A'),   
    ('III B', 'III B'),   
    ('I V', 'I V'),   
    ('Sem informação', 'Sem informação'),   
]

ESTADIAMENTO_HISTOPATOLOGICO = [
    ('Carcinoma epidermóide','Carcinoma epidermóide'),
    ('Adenocarcinoma','Adenocarcinoma'),
    ('Outros', 'Outros'), 
    ('Sem informação', 'Sem informação'),   
] 

TIPO_HISTOLOGICO = [
    ('Grau X','Grau X'),
    ('Grau 1','Grau 1'),
    ('Grau 2', 'Grau 2'), 
    ('Grau 3', 'Grau 3'),   
    ('Sem informação', 'Sem informação'),   
]

TECNICA_CIRURGICA = [
    ('HTA I','HTA I'),
    ('HTA II','HTA II'),
    ('HTA III', 'HTA III'), 
    ('HTV', 'HTV'),
    ('SOB', 'SOB'),   
    ('SOU/SOD/SOE', 'SOU/SOD/SOE'),
    ('Traquelectomia radical', 'Traquelectomia radical'),   
    ('Cirurgia de Schauta', 'Cirurgia de Schauta'),
]

SIM_NAO_INFO = [('Sim', 'Sim'),
                ('Não', 'Não'),
                ('Sem informação', 'Sem informação'),   
]

TIPO_QUIMIO = [('Neoadjuvante', 'Neoadjuvante'), 
                ('Adjuvante', 'Adjuvante'),
]


class FormAICS(models.Model):
    aics01  = models.DateField(verbose_name='Data de nascimento')
    # aics02 = models.IntegerField(verbose_name='Idade')
    aics03 = models.FloatField(verbose_name='Peso')
    aics04 = models.FloatField(verbose_name='Altura')
    aics05 = models.CharField(max_length=20, choices=IMC_CHOICES, verbose_name='IMC')
    aics06 = models.FloatField(verbose_name='Circunferência abdominal')
    aics07 = models.IntegerField(verbose_name='Paridade (gestações)')
    aics08 = models.IntegerField(verbose_name='Paridade (partos)')
    aics09 = models.IntegerField(verbose_name='Paridade (abortos)')
    aics10 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Menopausa por tratamento oncológico')
    
    aics11= models.ManyToManyField(RespostaTexto, related_name='+', verbose_name='Sintomas da menopausa')

    aics12 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Tabagista')
    aics13 = models.DateField(null=True, verbose_name='Ex-tabagista (há quanto tempo)')
    aics14 = models.CharField(max_length=20, choices=COR_PELE, verbose_name='Cor da pele')
    aics15 = models.CharField(max_length=20, choices=ESTADO_CIVIL, verbose_name='Estado civil')
    aics16 = models.CharField(max_length=20, choices=PROFISSAO, verbose_name='Profissão')
    aics17 = models.CharField(max_length=50, choices=ESCOLARIDADE, verbose_name='Escolaridade')
    aics18 = models.CharField(max_length=50, choices=RENDA_FAMILIAR, verbose_name='Renda familiar')
    aics19 = models.CharField(max_length=20, choices=VINCULO_PREVIDENCIARIO, verbose_name='Vínculo previdenciário')
    aics20 = models.CharField(max_length=20, choices=FIGO, verbose_name='Estadiamento Clínico FIGO')
    aics21 = models.CharField(max_length=50, choices=ESTADIAMENTO_HISTOPATOLOGICO, verbose_name='Estadiamento histopatológico')
    aics22 = models.CharField(max_length=20, choices=TIPO_HISTOLOGICO, verbose_name='Tipo/grau histológico')

    aics23 = models.ManyToManyField(RespostaTexto, related_name='+', verbose_name='Tratamento indicado')

    aics24 = models.CharField(max_length=20, null=True, verbose_name='Procedimento cirúrgico')
    aics25 = models.DateField(null=True, verbose_name='Data de realização da primeira cirurgia:')
    aics26 = models.CharField(max_length=50, null=True, choices=TECNICA_CIRURGICA, verbose_name='Técnica cirúrgica')
    aics27 = models.CharField(max_length=20, null=True, choices=SIM_NAO_INFO, verbose_name='Complicação pós-cirúrgica até 30 dias após a cirurgia')
    
    aics28 = models.IntegerField(null=True, verbose_name='Número de sessões de radioterapia')
    aics29 = models.FloatField(null=True, verbose_name='Dose na radioterapia (Gy)')
    aics30 = models.DateField(null=True, verbose_name='Tempo de tratamento com radioterapia')

    aics31 = models.IntegerField(null=True, verbose_name='Número de sessões de braquiterapia:')
    aics32 = models.FloatField(null=True, verbose_name='Dose na braquiterapia (Gy)')
    aics33 = models.DateField(null=True, verbose_name='Tempo de tratamento com braquiterapia')

    aics34 = models.CharField(max_length=20, null=True, choices=TIPO_QUIMIO, verbose_name='Tipo da quimioterapia')

    aics35 = models.ManyToManyField(RespostaTexto, related_name='+', null=True, verbose_name='Comorbidades')

    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, related_name='consulta_aics', null=False)

    def __str__(self):
        return str(self.consulta)