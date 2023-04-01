from django.db import models
from consulta.models import Consulta


class FormFIQL(models.Model):

    RESPOSTAS1 = (

        ('Muito boa', 'Muito boa'),
        ('Boa', 'Boa'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim')
    )

    RESPOSTAS2 = (

        ('Muitas vezes', 'Muitas vezes'),
        ('Algumas vezes', 'Algumas vezes'),
        ('Poucas vezes', 'Poucas vezes'),
        ('Nenhuma vez', 'Nenhuma vez'),
        ('Nenhuma das respostas', 'Nenhuma das respostas')
    )

    RESPOSTAS3 = (

        ('Extremamente. A ponto de desistir', 'Extremamente. A ponto de desistir'),
        ('Muitas vezes', 'Muitas vezes'),
        ('Com frequência', 'Com frequência'),
        ('Algumas vezes - o suficiente para me preocupar (incomodar)', 'Algumas vezes - o suficiente para me preocupar (incomodar)'),
        ('Poucas vezes', 'Poucas vezes'),
        ('Nenhuma vez', 'Nenhuma vez')
    )

    fiql01 = models.CharField(max_length=70, choices=RESPOSTAS1, verbose_name='Em geral você diria que sua saúde é')
    fiql02 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Tenho medo de sair')
    fiql03 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Evito visitar amigos ou parentes')
    fiql04 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Evito passar a noite longe de casa')
    fiql05 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='É difícil para eu sair e fazer coisas como ir ao cinema ou à igreja')
    fiql06 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Evito comer antes de sair de casa')
    fiql07 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Quando estou fora de casa tento ficar sempre que possível próximo ao banheiro')
    fiql08 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='É importante eu planejar o que vou fazer de acordo com o meu funcionamento intestinal')
    fiql09 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Evito viajar')
    fiql10 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Fico preocupado em não ser capaz de chegar ao banheiro em tempo')
    fiql11 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Sinto que não tenho controle do meu intestino')
    fiql12 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Não consigo controlar minha evacuação a tempo de chegar ao banheiro')
    fiql13 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Perco fezes sem perceber')
    fiql14 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Tento evitar a perda de fezes, ficando próximo ao banheiro')
    fiql15 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Fico envergonhado')
    fiql16 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Não posso fazer muitas coisas que eu quero fazer')
    fiql17 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Fico preocupado em perder fezes')
    fiql18 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Sinto-me deprimido')
    fiql19 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Fico preocupado se outras pessoas sentem cheiro de fezes em mim')
    fiql20 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Acho que não sou uma pessoa saudável')
    fiql21 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Tenho menos prazer em viver')
    fiql22 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Tenho uma relação sexual com menor frequência do que gostaria')
    fiql23 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Sinto-me diferente das outras pessoas')
    fiql24 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Sempre estou pensando na possibilidade de perder fezes')
    fiql25 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Tenho medo de ter sexo')
    fiql26 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Evito viajar de carro ou ônibus')
    fiql27 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Evito sair para comer')
    fiql28 = models.CharField(max_length=70, choices=RESPOSTAS2, verbose_name='Quando vou a um lugar novo, procuro saber onde está o banheiro')
    fiql29 = models.CharField(max_length=70, choices=RESPOSTAS3, verbose_name='Durante o mês passado, eu me senti tão triste, desanimado ou tive muitos problemas que me fizeram pensar que nada valia a pena')
    
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return self.consulta
