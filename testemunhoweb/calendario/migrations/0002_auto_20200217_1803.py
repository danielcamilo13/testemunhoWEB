# Generated by Django 2.2.7 on 2020-02-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='data_final',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Final'),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='data_inicial',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Inicial'),
        ),
    ]
