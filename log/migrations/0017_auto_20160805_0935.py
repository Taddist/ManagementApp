# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 08:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0016_auto_20160805_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conge',
            name='user',
        ),
        migrations.DeleteModel(
            name='conge',
        ),
    ]
