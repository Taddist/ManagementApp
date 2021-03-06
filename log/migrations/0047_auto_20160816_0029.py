# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0046_auto_20160815_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conge',
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
        migrations.AlterField(
            model_name='pole',
            name='souspole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Souspole'),
        ),
        migrations.AlterField(
            model_name='pole',
            name='typepole',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='souspole',
            name='typesouspole',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Conge',
        ),
    ]
