# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0020_conge'),
    ]

    operations = [
        migrations.CreateModel(
            name='dateactivite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entree', models.TimeField()),
                ('pause', models.TimeField()),
                ('sortie', models.TimeField()),
                ('date_debut', models.DateField()),
                ('nbr_jour', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raison_demande', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='raison',
            fields=[
                ('id_raison', models.IntegerField(primary_key=True, serialize=False)),
                ('raisons', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='synthese',
            fields=[
                ('jour', models.DateField(primary_key=True, serialize=False)),
                ('dateactivite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.dateactivite')),
                ('raison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.raison')),
            ],
        ),
        migrations.CreateModel(
            name='typedocument',
            fields=[
                ('id_type', models.IntegerField(primary_key=True, serialize=False)),
                ('types', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='typedocument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.typedocument', unique=True),
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]