# Generated by Django 2.2.7 on 2020-01-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0052_auto_20200101_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irmaos',
            name='excecao_dia',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Excecao para dias '),
        ),
    ]
