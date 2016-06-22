# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gene_pc_api', '0010_auto_20160620_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='registration_code',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
