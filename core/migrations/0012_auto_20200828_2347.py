# Generated by Django 3.1 on 2020-08-29 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_escolha_acertos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escolha',
            name='acertos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
