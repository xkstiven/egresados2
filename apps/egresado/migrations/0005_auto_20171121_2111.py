# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-22 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresado', '0004_auto_20171121_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='egresado',
            name='apellidos',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='egresado',
            name='nombre',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
