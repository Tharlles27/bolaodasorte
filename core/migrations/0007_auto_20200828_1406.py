# Generated by Django 3.1 on 2020-08-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_testeum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testes',
            name='marco',
            field=models.CharField(blank=True, choices=[('1', '1'), ('0', '0')], max_length=1, null=True),
        ),
    ]