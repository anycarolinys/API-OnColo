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
            name='FormFIQL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiql01', models.CharField(choices=[('4', 'Muito boa'), ('3', 'Boa'), ('2', 'Regular'), ('1', 'Ruim')], max_length=1, verbose_name='Em geral você diria que sua saúde é')),
                ('fiql02', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Tenho medo de sair')),
                ('fiql03', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Evito visitar amigos ou parentes')),
                ('fiql04', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Evito passar a noite longe de casa')),
                ('fiql05', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='É difícil para eu sair e fazer coisas como ir ao cinema ou à igreja')),
                ('fiql06', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Evito comer antes de sair de casa')),
                ('fiql07', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Quando estou fora de casa tento ficar sempre que possível próximo ao banheiro')),
                ('fiql08', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='É importante eu planejar o que vou fazer de acordo com o meu funcionamento intestinal')),
                ('fiql09', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Evito viajar')),
                ('fiql10', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Fico preocupado em não ser capaz de chegar ao banheiro em tempo')),
                ('fiql11', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Sinto que não tenho controle do meu intestino')),
                ('fiql12', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Não consigo controlar minha evacuação a tempo de chegar ao banheiro')),
                ('fiql13', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Perco fezes sem perceber')),
                ('fiql14', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Tento evitar a perda de fezes, ficando próximo ao banheiro')),
                ('fiql15', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Fico envergonhado')),
                ('fiql16', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Não posso fazer muitas coisas que eu quero fazer')),
                ('fiql17', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Fico preocupado em perder fezes')),
                ('fiql18', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Sinto-me deprimido')),
                ('fiql19', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Fico preocupado se outras pessoas sentem cheiro de fezes em mim')),
                ('fiql20', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Acho que não sou uma pessoa saudável')),
                ('fiql21', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Tenho menos prazer em viver')),
                ('fiql22', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Tenho uma relação sexual com menor frequência do que gostaria')),
                ('fiql23', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Sinto-me diferente das outras pessoas')),
                ('fiql24', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Sempre estou pensando na possibilidade de perder fezes')),
                ('fiql25', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Tenho medo de ter sexo')),
                ('fiql26', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Evito viajar de carro ou ônibus')),
                ('fiql27', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Evito sair para comer')),
                ('fiql28', models.CharField(choices=[('4', 'Muitas vezes'), ('3', 'Algumas vezes'), ('2', 'Poucas vezes'), ('1', 'Nenhuma vez'), ('0', 'Nenhuma das respostas')], max_length=1, verbose_name='Quando vou a um lugar novo, procuro saber onde está o banheiro')),
                ('fiql29', models.CharField(choices=[('5', 'Extremamente. A ponto de desistir'), ('4', 'Muitas vezes'), ('3', 'Com frequência'), ('2', 'Algumas vezes - o suficiente para me preocupar (incomodar)'), ('1', 'Poucas vezes'), ('0', 'Nenhuma vez')], max_length=1, verbose_name='Durante o mês passado, eu me senti tão triste, desanimado ou tive muitos problemas que me fizeram pensar que nada valia a pena')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.consulta')),
            ],
        ),
    ]
