# Generated by Django 4.1.7 on 2023-03-11 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0002_remove_instituicao_id_administrador'),
        ('fisioterapeuta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisioterapeuta',
            name='instituicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instituicao.instituicao'),
        ),
    ]
