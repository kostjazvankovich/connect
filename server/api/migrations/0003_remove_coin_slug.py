# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-22 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171222_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='slug',
        ),
    ]
