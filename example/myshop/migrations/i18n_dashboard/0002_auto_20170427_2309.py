# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-27 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SmartPhone',
            new_name='SmartPhoneVariant',
        ),
    ]
