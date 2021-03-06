# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-29 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0012_auto_20181228_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dias',
            name='max',
            field=models.CharField(max_length=3, verbose_name='Qte max no mes'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p1',
            field=models.BooleanField(default=False, verbose_name='Periodo 1'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p1_1',
            field=models.BooleanField(default=False, verbose_name='Periodo 1'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p1_2',
            field=models.BooleanField(default=False, verbose_name='Periodo 1'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p2',
            field=models.BooleanField(default=False, verbose_name='Periodo 2'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p2_1',
            field=models.BooleanField(default=False, verbose_name='Periodo 2'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p3',
            field=models.BooleanField(default=False, verbose_name='Periodo 3'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p3_1',
            field=models.BooleanField(default=False, verbose_name='Periodo 3'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p4',
            field=models.BooleanField(default=False, verbose_name='Periodo 4'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p4_1',
            field=models.BooleanField(default=False, verbose_name='Periodo 4'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p5',
            field=models.BooleanField(default=False, verbose_name='Periodo 5'),
        ),
        migrations.AlterField(
            model_name='dias',
            name='p5_1',
            field=models.BooleanField(default=False, verbose_name='Periodo 5'),
        ),
    ]
