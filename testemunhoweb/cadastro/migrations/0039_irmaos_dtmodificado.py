# Generated by Django 2.2.7 on 2019-11-30 06:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0038_auto_20190901_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='irmaos',
            name='dtModificado',
            field=models.DateField(default=datetime.datetime(2019, 11, 30, 6, 34, 17, 642609, tzinfo=utc), verbose_name='Data de modificacao'),
        ),
    ]
