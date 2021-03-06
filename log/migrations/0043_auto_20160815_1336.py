# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0042_auto_20160815_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=20)),
                ('cin', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('date_embauche', models.DateField()),
                ('enfant', models.IntegerField()),
                ('contrat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Contrat')),
                ('pole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Pole')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Role')),
                ('situation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Situation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
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
    ]
