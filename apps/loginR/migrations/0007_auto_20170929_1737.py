# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginR', '0006_auto_20170929_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poke',
            name='poker',
        ),
        migrations.RemoveField(
            model_name='poke',
            name='poked',
        ),
        migrations.AddField(
            model_name='poke',
            name='poked',
            field=models.ManyToManyField(related_name='poked', to='loginR.User'),
        ),
    ]