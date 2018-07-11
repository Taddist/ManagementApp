# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_conge'),
    ]

    operations = [
        migrations.CreateModel(
            name='raison',
            fields=[
                ('id_raison', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='synthese',
            fields=[
                ('jour', models.DateField(primary_key=True, serialize=False)),
                ('raison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.raison', unique=True)),
            ],
        ),
    ]