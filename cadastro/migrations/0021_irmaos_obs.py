# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-30 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0020_auto_20190127_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='irmaos',
            name='obs',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Observacao'),
        ),
    ]