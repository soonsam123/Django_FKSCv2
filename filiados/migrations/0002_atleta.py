# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-29 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filiados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_atleta', models.CharField(max_length=100)),
                ('academia', models.CharField(max_length=200)),
                ('num_registro', models.IntegerField()),
            ],
        ),
    ]
