# Generated by Django 3.1 on 2020-10-20 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20201019_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='v_min_ponto',
            field=models.IntegerField(verbose_name='Porcentagem para menor pontuador. ex(10) para 10%'),
        ),
    ]
