# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-15 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deepURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('Url', models.CharField(max_length=254)),
                ('shortcode', models.CharField(max_length=20, unique=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]