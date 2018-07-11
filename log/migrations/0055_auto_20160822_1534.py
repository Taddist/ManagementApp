# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 14:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0054_auto_20160822_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrashConge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbrjour', models.PositiveIntegerField()),
                ('datesupprime', models.DateTimeField(auto_now_add=True)),
                ('datedebutconge', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
        migrations.AlterField(
            model_name='pole',
            name='souspole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Souspole'),
        ),
    ]
