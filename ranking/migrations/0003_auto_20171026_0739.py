# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-26 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_auto_20170812_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='acad_segundo',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='acad_terceiro',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='segundo',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='terceiro',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
