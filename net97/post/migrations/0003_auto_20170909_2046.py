# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170909_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'portfólio', 'verbose_name_plural': 'portfólios'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='post',
            name='order',
        ),
    ]
