# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-01 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0034_irmaos_grupo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='irmaos',
            old_name='max',
            new_name='maximo',
        ),
        migrations.RemoveField(
            model_name='irmaos',
            name='excecao',
        ),
        migrations.AddField(
            model_name='irmaos',
            name='excecao_dia',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Excecao para dias '),
        ),
        migrations.AddField(
            model_name='irmaos',
            name='excecao_nome',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='Excecao com nomes'),
        ),
    ]
