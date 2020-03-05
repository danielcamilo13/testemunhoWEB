# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-14 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia_semana', models.CharField(max_length=80, verbose_name='dia da semana')),
            ],
        ),
        migrations.CreateModel(
            name='irmaos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nm', models.CharField(max_length=120, verbose_name='Nome do irmao')),
                ('cgcao', models.CharField(max_length=90, verbose_name='Congrega\xe7\xe3o')),
                ('gr', models.CharField(max_length=70, verbose_name='G\xeanero')),
                ('estado_civil', models.CharField(max_length=80, verbose_name='Estado Civil')),
            ],
        ),
        migrations.CreateModel(
            name='periodo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('periodo', models.CharField(max_length=80, verbose_name='Periodo')),
            ],
        ),
    ]