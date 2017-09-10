# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('link', models.CharField(max_length=200, verbose_name='Link')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='imagem')),
            ],
            options={
                'verbose_name': 'portfólio',
                'verbose_name_plural': 'portfólios',
            },
        ),
    ]