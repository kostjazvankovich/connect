# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 23:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_transfer_stripe_charge_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account_value',
        ),
    ]
