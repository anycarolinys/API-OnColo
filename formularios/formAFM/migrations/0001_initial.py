# Generated by Django 4.1.7 on 2023-04-11 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consulta', '0002_alter_consulta_data_consulta'),
        ('respostatexto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormAFM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afm01', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Bebe 2 litros de água?')),
                ('afm02', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Sente vontade de urinar?')),
                ('afm03', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Tem sensação de esvaziamento incompleto?')),
                ('afm04', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Há gotejamento após esvaziament')),
                ('afm05', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Você perde xixi?')),
                ('afm07', models.DateField(null=True, verbose_name='Data do último episódio:')),
                ('afm08', models.IntegerField(null=True, verbose_name='Perda diária:')),
                ('afm09', models.CharField(choices=[('Muita', 'Muita'), ('Moderada', 'Moderada'), ('Pouca', 'Pouca')], max_length=20, null=True, verbose_name='Intensidade de perda:')),
                ('afm10', models.CharField(choices=[('Gota', 'Gota'), ('Colher', 'Colher'), ('Jato', 'Jato')], max_length=20, null=True, verbose_name='Quantidade da perda:')),
                ('afm11', models.CharField(choices=[('Urgência', 'Urgência'), ('Esforço', 'Esforço'), ('Mista', 'Mista'), ('Transbordamento', 'Transbordamento')], max_length=20, null=True, verbose_name='Tipo da incontinência urinária:')),
                ('afm12', models.DateField(null=True, verbose_name='Início dos sintomas:')),
                ('afm13', models.IntegerField(verbose_name='Frequência urinária diária:')),
                ('afm14', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Dor para urinar?')),
                ('afm15', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Infecção urinária?')),
                ('afm16', models.IntegerField(null=True, verbose_name='Quantas vezes?')),
                ('afm17', models.DateField(null=True, verbose_name='Qual a data do último episódio?')),
                ('afm18', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name=' Uso de forro?')),
                ('afm19', models.IntegerField(null=True, verbose_name='Quantidade por dia?')),
                ('afm20', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name=' Enurese?')),
                ('afm21', models.IntegerField(null=True, verbose_name='Quantidade de vezes?')),
                ('afm22', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Nocturia?')),
                ('afm23', models.IntegerField(null=True, verbose_name='Quantidade de vezes?')),
                ('afm24', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Sente protuberância ou algo caindo que pode ver ou sentir na área vaginal?')),
                ('afm25', models.CharField(choices=[('Unidigital', 'Unidigital'), ('Bidigital', 'Bidigital')], max_length=20, verbose_name='Toque vaginal')),
                ('afm26', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Desconforto ao toque vaginal?')),
                ('afm27', models.CharField(choices=[('Ausente', 'Ausente'), ('Suave', 'Suave'), ('Severo', 'Severo')], max_length=20, verbose_name='Dor')),
                ('afm28', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Sangramento Vaginal')),
                ('afm29', models.FloatField(verbose_name='Comprimento')),
                ('afm30', models.IntegerField(verbose_name='Segundos de contração do MAP sustentada')),
                ('afm31', models.IntegerField(verbose_name='Contrações rápidas sem perder a força')),
                ('afm32', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Usa musculatura acessória para contração?')),
                ('afm34', models.CharField(choices=[('Diminuído', 'Diminuído'), ('Normal', 'Normal'), ('Aumentado', 'Aumentado')], max_length=20, verbose_name='Atividade tônica dos músculos do assoalho pélvico')),
                ('afm35', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Contração do levantador do ânus/ contração em direção à sínfise púbica')),
                ('afm36', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Exercícios com dilatadores')),
                ('afm37', models.IntegerField(null=True, verbose_name='Frequência dilatadores')),
                ('afm38', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Relação sexual')),
                ('afm39', models.IntegerField(null=True, verbose_name='Frequência relação sexual')),
                ('afm40', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True, verbose_name='Desconforto na relação sexual?')),
                ('afm41', models.CharField(choices=[('0', 'Ausência de resposta muscular'), ('1', 'Esboço de contração não sustentada'), ('2', 'Presença de contração de pequena intensidade, mas que se sustenta'), ('3', 'Contração moderada, sentida com o aumento da pressão intavaginal, que comprime os dedos do examinador com pequena elevação cranial da parede vaginal'), ('4', 'Contração satisfatória, que aperta os dedos do examinador, com elevação da parede vaginal em direção à sínfise púbica'), ('5', 'Contração forte, compressão firme dos dedos do examinador com movimento positivo em relação à sínfise púbica')], max_length=20, verbose_name='Força da musculatura do assoalho pélvico')),
                ('afm42', models.CharField(choices=[('P', 'Power'), ('E', 'Endurance'), ('R', 'Repetition'), ('F', 'Fast')], max_length=20, verbose_name='Escala New Perfect')),
                ('afm06', models.ManyToManyField(null=True, related_name='+', to='respostatexto.respostatexto', verbose_name='Circunstância da perda')),
                ('afm33', models.ManyToManyField(null=True, related_name='+', to='respostatexto.respostatexto', verbose_name='Musculatura')),
                ('consulta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consulta_afm', to='consulta.consulta')),
            ],
        ),
    ]
