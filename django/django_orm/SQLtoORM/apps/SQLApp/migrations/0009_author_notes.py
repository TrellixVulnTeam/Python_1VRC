# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-12 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SQLApp', '0008_auto_20190912_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(default='notes', max_length=255),
        ),
    ]
