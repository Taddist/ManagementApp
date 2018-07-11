# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-25 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0056_auto_20160823_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trashconge',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trashdocument',
            name='typedocument',
        ),
        migrations.RemoveField(
            model_name='trashdocument',
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
        migrations.DeleteModel(
            name='TrashConge',
        ),
        migrations.DeleteModel(
            name='TrashDocument',
        ),
    ]
