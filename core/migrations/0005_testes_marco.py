# Generated by Django 3.1 on 2020-08-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_testes'),
    ]

    operations = [
        migrations.AddField(
            model_name='testes',
            name='marco',
            field=models.BooleanField(default=False),
        ),
    ]
