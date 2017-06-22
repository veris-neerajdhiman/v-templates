# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mold', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='templates',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified at'),
        ),
    ]