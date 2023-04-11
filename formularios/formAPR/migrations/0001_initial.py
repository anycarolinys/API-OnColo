# Generated by Django 4.1.7 on 2023-04-11 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consulta', '0002_alter_consulta_data_consulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormAPR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apr01', models.FloatField(verbose_name='Peso')),
                ('apr02', models.FloatField(verbose_name='Altura')),
                ('apr03', models.FloatField(verbose_name='IMC')),
                ('apr04', models.FloatField(verbose_name='Circunferência abdominal')),
                ('apr05', models.DateField(verbose_name='Data da radioterapia')),
                ('apr06', models.DateField(verbose_name='Data final da radioterapia')),
                ('apr07', models.FloatField(verbose_name='Radiação total')),
                ('apr08', models.IntegerField(verbose_name='Número total de frações')),
                ('apr09', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Quimioterapia')),
                ('apr10', models.DateField(blank=True, null=True, verbose_name='Data da quimioterapia')),
                ('apr11', models.DateField(blank=True, null=True, verbose_name='Data final da quimioterapia')),
                ('apr12', models.FloatField(blank=True, null=True, verbose_name='Ciclo total')),
                ('apr13', models.FloatField(blank=True, null=True, verbose_name='Dose Total')),
                ('apr14', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Braquiterapia')),
                ('apr15', models.DateField(blank=True, null=True, verbose_name='Data da braquiterapia')),
                ('apr16', models.DateField(blank=True, null=True, verbose_name='Data final da braquiterapia')),
                ('apr17', models.FloatField(blank=True, null=True, verbose_name='Radiação total')),
                ('apr18', models.IntegerField(blank=True, null=True, verbose_name='Número total de frações')),
                ('apr19', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Dor')),
                ('apr20', models.CharField(blank=True, max_length=45, null=True, verbose_name='Local')),
                ('apr21', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Escala Visual Analógica(EVA)')),
                ('apr22', models.FloatField(verbose_name='MID 21')),
                ('apr23', models.FloatField(verbose_name='MID 14')),
                ('apr24', models.FloatField(verbose_name='MID 07')),
                ('apr25', models.FloatField(verbose_name='MID BSP')),
                ('apr26', models.FloatField(verbose_name='MID 28')),
                ('apr27', models.FloatField(verbose_name='MID 35')),
                ('apr28', models.FloatField(verbose_name='MID TT')),
                ('apr29', models.FloatField(verbose_name='MID Pé')),
                ('apr30', models.FloatField(verbose_name='MIE 21')),
                ('apr31', models.FloatField(verbose_name='MIE 14')),
                ('apr32', models.FloatField(verbose_name='MIE 07')),
                ('apr33', models.FloatField(verbose_name='MIE BSP')),
                ('apr34', models.FloatField(verbose_name='MIE 28')),
                ('apr35', models.FloatField(verbose_name='MIE 35')),
                ('apr36', models.FloatField(verbose_name='MIE TT')),
                ('apr37', models.FloatField(verbose_name='MIE Pé')),
                ('apr38', models.FloatField(verbose_name='# 21')),
                ('apr39', models.FloatField(verbose_name='# 14')),
                ('apr40', models.FloatField(verbose_name='# 07')),
                ('apr41', models.FloatField(verbose_name='# BSP')),
                ('apr42', models.FloatField(verbose_name='# 28')),
                ('apr43', models.FloatField(verbose_name='# 35')),
                ('apr44', models.FloatField(verbose_name='# TT')),
                ('apr45', models.FloatField(verbose_name='# Pé')),
                ('apr46', models.CharField(choices=[('Sem alterações', 'Sem alterações'), ('Sintomático reversível com elevação do membro', 'Sintomático reversível com elevação do membro'), ('Com alteração objetiva cutânea', 'Com alteração objetiva cutânea'), ('Com alteração objetiva Aguda', 'Com alteração objetiva Aguda'), ('Com alteração objetiva Tardia(com fibrose)', 'Com alteração objetiva Tardia(com fibrose)'), ('Elefantíase', 'Elefantíase')], max_length=45, verbose_name='Resultado')),
                ('apr47', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Sensação de peso')),
                ('apr48', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Pele esticada')),
                ('apr49', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Formigamento')),
                ('apr50', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Sensação de perna dura/movimentos reduzidos')),
                ('apr51', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Alguma dificuldade para realizar atividade física')),
                ('apr52', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Mudança de coloração')),
                ('apr53', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Telangiectasias')),
                ('apr54', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Veias varicosas')),
                ('apr55', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Ulcera venosa')),
                ('apr56', models.CharField(blank=True, choices=[('Fechada', 'Fechada'), ('Aberta', 'Aberta')], max_length=10, null=True, verbose_name='Ulcera venosa')),
                ('apr57', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Flexão do quadril D')),
                ('apr58', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Flexão do quadril E')),
                ('apr59', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Extensão do joelho D')),
                ('apr60', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Extensão do joelho E')),
                ('apr61', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Dorsiflexão do tornozelo D')),
                ('apr62', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Dorsiflexão do tornozelo E')),
                ('apr63', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Alterações da função INTESTINAL')),
                ('apr64', models.CharField(choices=[('Tipo I', 'Tipo I'), ('Tipo II', 'Tipo II'), ('Tipo III', 'Tipo III'), ('Tipo IV', 'Tipo IV'), ('Tipo V', 'Tipo V'), ('Tipo VI', 'Tipo VI'), ('Tipo VII', 'Tipo VII')], max_length=10, verbose_name='Escala de Bristol')),
                ('apr65', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Incontinência')),
                ('apr66', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Alterações da função VESICAL')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.consulta')),
            ],
        ),
    ]
