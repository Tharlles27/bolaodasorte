# Generated by Django 3.1 on 2020-10-19 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0021_auto_20200901_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='lucro',
        ),
        migrations.AddField(
            model_name='config',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='config',
            name='v_max_ponto',
            field=models.IntegerField(verbose_name='Porcentagem para maior pontuador. ex(30) para 30%'),
        ),
        migrations.AlterField(
            model_name='config',
            name='v_min_ponto',
            field=models.IntegerField(verbose_name='Porcentagem para maior pontuador. ex(30) para 30%'),
        ),
    ]
