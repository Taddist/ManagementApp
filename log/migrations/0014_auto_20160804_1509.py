# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0013_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conge',
            old_name='date_debut_conge',
            new_name='datedebut_conge',
        ),
        migrations.RenameField(
            model_name='conge',
            old_name='nbr_jour',
            new_name='nbrjour',
        ),
    ]
