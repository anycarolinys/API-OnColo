# Generated by Django 4.1.7 on 2023-03-26 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consulta', '0002_alter_consulta_data_consulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFSFI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsfi01', models.CharField(choices=[('5', 'Quase sempre ou sempre'), ('4', 'A maioria das vezes (mais da metade do tempo)'), ('3', 'Algumas vezes (cerca da metade do tempo)'), ('2', 'Poucas vezes (menos da metade do tempo)'), ('1', 'Quase nunca ou nunca')], max_length=1, verbose_name='Com que frequência você sentiu desejo ou interesse sexual?')),
                ('fsfi02', models.CharField(choices=[('5', 'Muito alto'), ('4', 'Alto'), ('3', 'Moderado'), ('2', 'Baixo'), ('1', 'Muito baixo ou absolutamente nenhum')], max_length=1, verbose_name='Como você avalia o seu grau de desejo ou interesse sexual?')),
                ('fsfi03', models.CharField(choices=[('5', 'Quase sempre ou sempre'), ('4', 'A maioria das vezes (mais da metade do tempo)'), ('3', 'Algumas vezes (cerca da metade do tempo)'), ('2', 'Poucas vezes (menos da metade do tempo)'), ('1', 'Quase nunca ou nunca'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Com que frequência (quantas vezes) você se sentiu sexualmente excitada durante a atividade sexual ou o ato sexual?')),
                ('fsfi04', models.CharField(choices=[('5', 'Muito alto'), ('4', 'Alto'), ('3', 'Moderado'), ('2', 'Baixo'), ('1', 'Muito baixo ou absolutamente nenhum'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Como você classificaria seu grau de excitação sexual durante a atividade ou ato sexual?')),
                ('fsfi05', models.CharField(choices=[('5', 'Segurança muito alta'), ('4', 'Segurança alta'), ('3', 'Segurança moderada'), ('2', 'Segurança baixa'), ('1', 'Segurança muito baixa ou sem segurança'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Como você avalia o seu grau de segurança (quão confortável é) para ficar sexualmente Excitada durante a atividade sexual ou ato sexual?')),
                ('fsfi06', models.CharField(choices=[('5', 'Quase sempre ou sempre'), ('4', 'A maioria das vezes (mais da metade do tempo)'), ('3', 'Algumas vezes (cerca da metade do tempo)'), ('2', 'Poucas vezes (menos da metade do tempo)'), ('1', 'Quase nunca ou nunca'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Com que frequência (quantas vezes) você ficou satisfeita com sua excitação sexual durante a atividade ou ato sexual?')),
                ('fsfi07', models.CharField(choices=[('5', 'Quase sempre ou sempre'), ('4', 'A maioria das vezes (mais da metade do tempo)'), ('3', 'Algumas vezes (cerca da metade do tempo)'), ('2', 'Poucas vezes (menos da metade do tempo)'), ('1', 'Quase nunca ou nunca'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Com que frequência (quantas vezes) você teve lubrificação vaginal (ficou com a “vagina molhada”) durante a atividade sexual ou ato sexual?')),
                ('fsfi08', models.CharField(choices=[('5', 'Nada difícil'), ('4', 'Ligeiramente difícil'), ('3', 'Difícil'), ('2', 'Muito difícil'), ('1', 'Extremamente difícil ou impossível'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Como você avalia sua dificuldade em TER lubrificação vaginal (ficou com a “vagina molhada”) durante a atividade sexual ou ato sexual? Levou tempo para ficar lubrificada?')),
                ('fsfi09', models.CharField(choices=[('5', 'Quase sempre ou sempre'), ('4', 'A maioria das vezes (mais da metade do tempo)'), ('3', 'Algumas vezes (cerca da metade do tempo)'), ('2', 'Poucas vezes (menos da metade do tempo)'), ('1', 'Quase nunca ou nunca'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Com que frequência (quantas vezes) você MANTEVE a lubrificação vaginal (ficou com a “vagina molhada”) até o final da atividade ou ato sexual?')),
                ('fsfi10', models.CharField(choices=[('5', 'Nada difícil'), ('4', 'Ligeiramente difícil'), ('3', 'Difícil'), ('2', 'Muito difícil'), ('1', 'Extremamente difícil ou impossível'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Qual foi sua DIFICULDADE em MANTER a lubrificação vaginal(“vagina molhada”) até o final da atividade sexual?')),
                ('fsfi11', models.CharField(choices=[('5', 'Quase sempre ou sempre'), ('4', 'A maioria das vezes (mais da metade do tempo)'), ('3', 'Algumas vezes (cerca da metade do tempo)'), ('2', 'Poucas vezes (menos da metade do tempo)'), ('1', 'Quase nunca ou nunca'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Quando teve estímulo sexual ou ato sexual, com que frequência (quantas vezes) você atingiu o orgasmo (“gozou”)?')),
                ('fsfi12', models.CharField(choices=[('5', 'Nada difícil'), ('4', 'Ligeiramente difícil'), ('3', 'Difícil'), ('2', 'Muito difícil'), ('1', 'Extremamente difícil ou impossível'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='Quando você teve estímulo sexual ou ato sexual, qual foi a sua dificuldade em você atingir o orgasmo (“gozar”)?O orgasmo para você foi fácil ou difícil, nas últimas 4 semanas?')),
                ('fsfi13', models.CharField(choices=[('5', 'Muito satisfeita'), ('4', 'Moderadamente satisfeita'), ('3', 'Quase igualmente satisfeita e insatisfeita'), ('2', 'Moderadamente insatisfeita'), ('1', 'Muito insatisfeita'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='O quanto você ficou satisfeita com sua capacidade de atingir o orgasmo (“gozar”) durante a atividade ou ato sexual?')),
                ('fsfi14', models.CharField(choices=[('5', 'Muito satisfeita'), ('4', 'Moderadamente satisfeita'), ('3', 'Quase igualmente satisfeita e insatisfeita'), ('2', 'Moderadamente insatisfeita'), ('1', 'Muito insatisfeita'), ('0', 'Sem atividade sexual')], max_length=1, verbose_name='O quanto você esteve satisfeita com a proximidade emocional entre você e o seu parceiro durante a atividade sexual?')),
                ('fsfi15', models.CharField(choices=[('5', 'Muito satisfeita'), ('4', 'Moderadamente satisfeita'), ('3', 'Quase igualmente satisfeita e insatisfeita'), ('2', 'Moderadamente insatisfeita'), ('1', 'Muito insatisfeita')], max_length=1, verbose_name='O quanto você esteve satisfeita com o relacionamento sexual entre você e o seu parceiro?')),
                ('fsfi16', models.CharField(choices=[('5', 'Muito satisfeita'), ('4', 'Moderadamente satisfeita'), ('3', 'Quase igualmente satisfeita e insatisfeita'), ('2', 'Moderadamente insatisfeita'), ('1', 'Muito insatisfeita')], max_length=1, verbose_name='O quanto você esteve satisfeita com sua vida sexual de um modo geral?')),
                ('fsfi17', models.CharField(choices=[('5', 'Quase nunca ou nunca'), ('4', 'Poucas vezes (menos da metade do tempo)'), ('3', 'Algumas vezes (cerca de metade do tempo)'), ('2', 'A maioria das vezes (mais da metade do tempo)'), ('1', 'Quase sempre ou sempre'), ('0', 'Não tentei ter relação')], max_length=1, verbose_name='Com que frequência (quantas vezes) você sentiu desconforto ou dor DURANTE a penetração vaginal?')),
                ('fsfi18', models.CharField(choices=[('5', 'Quase nunca ou nunca'), ('4', 'Poucas vezes (menos da metade do tempo)'), ('3', 'Algumas vezes (cerca de metade do tempo)'), ('2', 'A maioria das vezes (mais da metade do tempo)'), ('1', 'Quase sempre ou sempre'), ('0', 'Não tentei ter relação')], max_length=1, verbose_name='Com que frequência (quantas vezes) você sentiu desconforto ou dor APÓS a penetração vaginal?')),
                ('fsfi19', models.CharField(choices=[('5', 'Muito baixo ou absolutamente nenhum'), ('4', 'Baixo'), ('3', 'Moderado'), ('2', 'Alto'), ('1', 'Muito alto'), ('0', 'Não tentei ter relação')], max_length=1, verbose_name='Como você classificaria seu GRAU de desconforto ou dor durante ou após a penetração vaginal?')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.consulta')),
            ],
        ),
    ]
