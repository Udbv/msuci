# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-19 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ms', '0005_auto_20170819_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_track',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='ms.Track'),
            preserve_default=False,
        ),
    ]