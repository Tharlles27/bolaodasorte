# Generated by Django 3.1 on 2020-08-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200830_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodadas',
            name='num_rodada',
            field=models.CharField(choices=[('1', '1° Rodada'), ('2', '2° Rodada'), ('3', '3° Rodada'), ('4', '4° Rodada'), ('5', '5° Rodada'), ('6', '6° Rodada'), ('7', '7° Rodada'), ('8', '8° Rodada'), ('9', '9° Rodada'), ('10', '10° Rodada'), ('11', '11° Rodada')], max_length=2, verbose_name='Numero da rodada'),
        ),
    ]
