# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0022_auto_20160805_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='typedocument',
        ),
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
        migrations.RemoveField(
            model_name='synthese',
            name='dateactivite',
        ),
        migrations.RemoveField(
            model_name='synthese',
            name='raison',
        ),
        migrations.DeleteModel(
            name='dateactivite',
        ),
        migrations.DeleteModel(
            name='document',
        ),
        migrations.DeleteModel(
            name='synthese',
        ),
        migrations.DeleteModel(
            name='typedocument',
        ),
    ]