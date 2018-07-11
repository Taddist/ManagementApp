# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0031_auto_20160805_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typecontrat', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='pole',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
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
            name='UserProfile',
        ),
    ]
