# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0016_auto_20171102_0719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant_data',
            old_name='plantID',
            new_name='plant',
        ),
        migrations.RenameField(
            model_name='tank_data',
            old_name='tankID',
            new_name='tank',
        ),
    ]
