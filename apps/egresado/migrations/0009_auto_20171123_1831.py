# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-23 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresado', '0008_egresado_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egresado',
            name='image',
            field=models.ImageField(blank=True, default='apps/egresado/media/profile_image/perfil.jpg', upload_to='profile_image'),
        ),
    ]
