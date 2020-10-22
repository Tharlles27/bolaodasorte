# Generated by Django 3.1 on 2020-10-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20201020_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='v_max_ponto',
            field=models.IntegerField(default=0, verbose_name='Porcentagem para maior pontuador. ex(30) para 30%'),
        ),
        migrations.AlterField(
            model_name='config',
            name='v_min_ponto',
            field=models.IntegerField(default=0, verbose_name='Porcentagem para menor pontuador. ex(10) para 10%'),
        ),
        migrations.AlterField(
            model_name='config',
            name='valor_jogada',
            field=models.IntegerField(default=0, verbose_name='Valor padrão de cada rodada, ex: 10, para 10,00R$'),
        ),
    ]
