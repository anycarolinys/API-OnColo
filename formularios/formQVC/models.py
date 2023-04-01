from django.db import models

from consulta.models import Consulta

class FormQVC(models.Model):
    RESPOSTAS1 = (
        ('1', 'nao'),
        ('2', 'pouco'),
        ('3', 'moderado'),
        ('4', 'muito'),
    )

    RESPOSTAS2 = (
        ('1', 'pessima'),
        ('2', 'muito ruim'),
        ('3', 'ruim'),
        ('4', 'moderado'),
        ('5', 'bom'),
        ('6', 'muito bom'),
        ('7', 'otima'),
    )

    qvc01 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Voce tem qualquer dificuldade quando faz grandes esforços (carregar bolsa de compras pesada ou mala?)')
    qvc02 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem dificuldade quando faz grande caminhada?')
    qvc03 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem qualquer dificuldade quando faz uma curta caminhada fora de casa?')
    qvc04 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem que ficar numa cama ou cadeira durante o dia?')
    qvc05 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você precisa de ajuda para se alimentar, se vestir, se lavar ou usar o banheiro?')
    qvc06 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Tem sido difícil trabalhar ou realizar suas atividades diárias?')
    qvc07 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Tem sido difícil praticar seu hobby ou participar de atividades de lazer?')
    qvc08 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você teve falta de ar?')
    qvc09 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem tido dor?')
    qvc10 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você precisou repousar?')
    qvc11 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem tido problemas para dormir?')
    qvc12 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem se sentido fraca?')
    qvc13 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem sentido falta de apetite?')
    qvc14 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem se sentido enjoada?')
    qvc15 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem vomitado?')
    qvc16 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem tido prisão de ventre?')
    qvc17 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem diarréia?')
    qvc18 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você esteve cansada?')
    qvc19 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='A dor interferiu em suas atividades diárias?')
    qvc20 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem tido dificuldade para se concentrar em coisas, como ler jornal ou ver televisão?')
    qvc21 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você se sentiu nervosa?')
    qvc22 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você esteve preocupada?')
    qvc23 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você se sentiu irritada facilmente?')
    qvc24 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você se sentiu deprimida?')
    qvc25 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='Você tem tido dificuldade de se lembrar das coisas?')
    qvc26 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='A sua condição física ou o tratamento médico tem interferido em sua atividade familiar?')
    qvc27 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='A sua condição física ou o tratamento médico tem interferido em suas atividades sociais?')
    qvc28 = models.CharField(max_length=1, choices=RESPOSTAS1, verbose_name='A sua condição física ou o tratamento médico tem lhe trazido dificuldades financeiras?')
    qvc29 = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='Como você classifica a sua saúde em geral, durante a última semana?')
    qvc30 = models.CharField(max_length=1, choices=RESPOSTAS2, verbose_name='Como você classifica a sua qualidade de vida em geral durante a última semana?')

    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return self.consulta

