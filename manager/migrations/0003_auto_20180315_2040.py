# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-15 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_mappoi_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappoi',
            name='score',
            field=models.IntegerField(),
        ),
    ]