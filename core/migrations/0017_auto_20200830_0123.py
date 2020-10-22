# Generated by Django 3.1 on 2020-08-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_config_lucro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='lucro',
            field=models.IntegerField(verbose_name='Lucro definido para o gerente do sistema'),
        ),
        migrations.AlterField(
            model_name='config',
            name='v_max_ponto',
            field=models.IntegerField(verbose_name='Prêmio para maior pontuador'),
        ),
        migrations.AlterField(
            model_name='config',
            name='v_min_ponto',
            field=models.IntegerField(verbose_name='Prêmio para menor pontuador'),
        ),
        migrations.AlterField(
            model_name='config',
            name='valor_jogada',
            field=models.IntegerField(verbose_name='Valor padrão de cada rodada, ex: 10,00'),
        ),
    ]
