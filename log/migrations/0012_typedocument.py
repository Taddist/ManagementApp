# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0011_synthese'),
    ]

    operations = [
        migrations.CreateModel(
            name='typedocument',
            fields=[
                ('id_type', models.IntegerField(primary_key=True, serialize=False)),
                ('types', models.CharField(max_length=100)),
            ],
        ),
    ]
