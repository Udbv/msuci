# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-19 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ms', '0003_auto_20170819_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_genre',
        ),
        migrations.AddField(
            model_name='album',
            name='album_genre',
            field=models.ManyToManyField(to='ms.Genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='al_sing', to='ms.Singer'),
        ),
    ]
