# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-23 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresado', '0007_auto_20171123_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='egresado',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
