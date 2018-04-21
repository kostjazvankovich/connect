# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-21 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180418_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='ip',
            field=models.GenericIPAddressField(db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='ipaddress',
            unique_together=set([('ip', 'user')]),
        ),
    ]