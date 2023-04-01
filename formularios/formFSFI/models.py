from django.db import models
from consulta.models import Consulta


class FormFSFI(models.Model):

    RESPOSTAS1 = (

        ('Quase sempre ou sempre', 'Quase sempre ou sempre'),
        ('A maioria das vezes (mais da metade do tempo)', 'A maioria das vezes (mais da metade do tempo)'),
        ('Algumas vezes (cerca da metade do tempo)', 'Algumas vezes (cerca da metade do tempo)'),
        ('Poucas vezes (menos da metade do tempo)', 'Poucas vezes (menos da metade do tempo)'),
        ('Quase nunca ou nunca', 'Quase nunca ou nunca')

    )

    RESPOSTAS2 = (

        ('Quase sempre ou sempre', 'Quase sempre ou sempre'),
        ('A maioria das vezes (mais da metade do tempo)', 'A maioria das vezes (mais da metade do tempo)'),
        ('Algumas vezes (cerca da metade do tempo)', 'Algumas vezes (cerca da metade do tempo)'),
        ('Poucas vezes (menos da metade do tempo)', 'Poucas vezes (menos da metade do tempo)'),
        ('Quase nunca ou nunca', 'Quase nunca ou nunca'),
        ('Sem atividade sexual', 'Sem atividade sexual')

    )

    RESPOSTAS3 = (

        ('Muito alto', 'Muito alto'),
        ('Alto', 'Alto'),
        ('Moderado', 'Moderado'),
        ('Baixo', 'Baixo'),
        ('Muito baixo ou absolutamente nenhum', 'Muito baixo ou absolutamente nenhum')

    )

    RESPOSTAS4 = (

        ('Muito alto', 'Muito alto'),
        ('Alto', 'Alto'),
        ('Moderado', 'Moderado'),
        ('Baixo', 'Baixo'),
        ('Muito baixo ou absolutamente nenhum', 'Muito baixo ou absolutamente nenhum'),
        ('Sem atividade sexual', 'Sem atividade sexual')

    )

    RESPOSTAS5 = (

        ('Segurança muito alta', 'Segurança muito alta'),
        ('Segurança alta', 'Segurança alta'),
        ('Segurança moderada', 'Segurança moderada'),
        ('Segurança baixa', 'Segurança baixa'),
        ('Segurança muito baixa ou sem segurança', 'Segurança muito baixa ou sem segurança'),
        ('Sem atividade sexual', 'Sem atividade sexual')

    )

    RESPOSTAS6 = (

        ('Nada difícil', 'Nada difícil'),
        ('Ligeiramente difícil', 'Ligeiramente difícil'),
        ('Difícil', 'Difícil'),
        ('Muito difícil', 'Muito difícil'),
        ('Extremamente difícil ou impossível', 'Extremamente difícil ou impossível'),
        ('Sem atividade sexual', 'Sem atividade sexual')

    )

    
    RESPOSTAS7 = (

        ('Muito satisfeita', 'Muito satisfeita'),
        ('Moderadamente satisfeita', 'Moderadamente satisfeita'),
        ('Quase igualmente satisfeita e insatisfeita', 'Quase igualmente satisfeita e insatisfeita'),
        ('Moderadamente insatisfeita', 'Moderadamente insatisfeita'),
        ('Muito insatisfeita', 'Muito insatisfeita'),
        ('Sem atividade sexual', 'Sem atividade sexual')

    )

    RESPOSTAS8 = (

        ('Muito satisfeita', 'Muito satisfeita'),
        ('Moderadamente satisfeita', 'Moderadamente satisfeita'),
        ('Quase igualmente satisfeita e insatisfeita', 'Quase igualmente satisfeita e insatisfeita'),
        ('Moderadamente insatisfeita', 'Moderadamente insatisfeita'),
        ('Muito insatisfeita', 'Muito insatisfeita')
    )

    RESPOSTAS9 = (

        ('Quase nunca ou nunca', 'Quase nunca ou nunca'),
        ('Poucas vezes (menos da metade do tempo)', 'Poucas vezes (menos da metade do tempo)'),
        ('Algumas vezes (cerca de metade do tempo)', 'Algumas vezes (cerca de metade do tempo)'),
        ('A maioria das vezes (mais da metade do tempo)', 'A maioria das vezes (mais da metade do tempo)'),
        ('Quase sempre ou sempre', 'Quase sempre ou sempre'),
        ('Não tentei ter relação', 'Não tentei ter relação')

    )

    RESPOSTAS10 = (

        ('Muito baixo ou absolutamente nenhum', 'Muito baixo ou absolutamente nenhum'),
        ('Baixo', 'Baixo'),
        ('Moderado', 'Moderado'),
        ('Alto', 'Alto'),
        ('Muito alto', 'Muito alto'),
        ('Não tentei ter relação', 'Não tentei ter relação')

    )

    fsfi01 = models.CharField(max_length=45, choices=RESPOSTAS1, verbose_name='Com que frequência você sentiu desejo ou interesse sexual?')
    fsfi02 = models.CharField(max_length=45, choices=RESPOSTAS3, verbose_name='Como você avalia o seu grau de desejo ou interesse sexual?')
    fsfi03 = models.CharField(max_length=45, choices=RESPOSTAS2, verbose_name='Com que frequência (quantas vezes) você se sentiu sexualmente excitada durante a atividade sexual ou o ato sexual?')
    fsfi04 = models.CharField(max_length=45, choices=RESPOSTAS4, verbose_name='Como você classificaria seu grau de excitação sexual durante a atividade ou ato sexual?')
    fsfi05 = models.CharField(max_length=45, choices=RESPOSTAS5, verbose_name='Como você avalia o seu grau de segurança (quão confortável é) para ficar sexualmente Excitada durante a atividade sexual ou ato sexual?')
    fsfi06 = models.CharField(max_length=45, choices=RESPOSTAS2, verbose_name='Com que frequência (quantas vezes) você ficou satisfeita com sua excitação sexual durante a atividade ou ato sexual?')
    fsfi07 = models.CharField(max_length=45, choices=RESPOSTAS2, verbose_name='Com que frequência (quantas vezes) você teve lubrificação vaginal (ficou com a “vagina molhada”) durante a atividade sexual ou ato sexual?')
    fsfi08 = models.CharField(max_length=45, choices=RESPOSTAS6, verbose_name='Como você avalia sua dificuldade em TER lubrificação vaginal (ficou com a “vagina molhada”) durante a atividade sexual ou ato sexual? Levou tempo para ficar lubrificada?')
    fsfi09 = models.CharField(max_length=45, choices=RESPOSTAS2, verbose_name='Com que frequência (quantas vezes) você MANTEVE a lubrificação vaginal (ficou com a “vagina molhada”) até o final da atividade ou ato sexual?')
    fsfi10 = models.CharField(max_length=45, choices=RESPOSTAS6, verbose_name='Qual foi sua DIFICULDADE em MANTER a lubrificação vaginal(“vagina molhada”) até o final da atividade sexual?')
    fsfi11 = models.CharField(max_length=45, choices=RESPOSTAS2, verbose_name='Quando teve estímulo sexual ou ato sexual, com que frequência (quantas vezes) você atingiu o orgasmo (“gozou”)?')
    fsfi12 = models.CharField(max_length=45, choices=RESPOSTAS6, verbose_name='Quando você teve estímulo sexual ou ato sexual, qual foi a sua dificuldade em você atingir o orgasmo (“gozar”)?O orgasmo para você foi fácil ou difícil, nas últimas 4 semanas?')
    fsfi13 = models.CharField(max_length=45, choices=RESPOSTAS7, verbose_name='O quanto você ficou satisfeita com sua capacidade de atingir o orgasmo (“gozar”) durante a atividade ou ato sexual?')
    fsfi14 = models.CharField(max_length=45, choices=RESPOSTAS7, verbose_name='O quanto você esteve satisfeita com a proximidade emocional entre você e o seu parceiro durante a atividade sexual?')
    fsfi15 = models.CharField(max_length=45, choices=RESPOSTAS8, verbose_name='O quanto você esteve satisfeita com o relacionamento sexual entre você e o seu parceiro?')
    fsfi16 = models.CharField(max_length=45, choices=RESPOSTAS8, verbose_name='O quanto você esteve satisfeita com sua vida sexual de um modo geral?')
    fsfi17 = models.CharField(max_length=45, choices=RESPOSTAS9, verbose_name='Com que frequência (quantas vezes) você sentiu desconforto ou dor DURANTE a penetração vaginal?')
    fsfi18 = models.CharField(max_length=45, choices=RESPOSTAS9, verbose_name='Com que frequência (quantas vezes) você sentiu desconforto ou dor APÓS a penetração vaginal?')
    fsfi19 = models.CharField(max_length=45, choices=RESPOSTAS10, verbose_name='Como você classificaria seu GRAU de desconforto ou dor durante ou após a penetração vaginal?')
    
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.consulta)
