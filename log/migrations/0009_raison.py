# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_conge'),
    ]

    operations = [
        migrations.CreateModel(
            name='raison',
            fields=[
                ('id_raison', models.IntegerField(primary_key=True, serialize=False)),
                ('raisons', models.CharField(max_length=50)),
            ],
        ),
    ]
