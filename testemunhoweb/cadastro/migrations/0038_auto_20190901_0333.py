# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-01 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0037_auto_20190901_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irmaos',
            name='maximo',
            field=models.CharField(default=3, max_length=3, verbose_name='max p/m'),
        ),
    ]
