# Generated by Django 3.1 on 2020-08-29 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_escolha_acertos'),
    ]

    operations = [
        migrations.AddField(
            model_name='escolha',
            name='acertos',
            field=models.IntegerField(default=0),
        ),
    ]
