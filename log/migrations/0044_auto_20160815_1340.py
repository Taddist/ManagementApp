# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0043_auto_20160815_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pole',
        ),
        migrations.AlterField(
            model_name='document',
            name='typedocument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Typedocument'),
        ),
        migrations.AlterField(
            model_name='nonactivite',
            name='raison',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='log.Raison'),
        ),
        migrations.DeleteModel(
            name='Pole',
        ),
    ]
