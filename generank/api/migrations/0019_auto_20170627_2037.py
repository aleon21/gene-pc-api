# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-27 20:37
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consentpdf',
            name='consent_pdf',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/data/consent/', location='/Users/andreleon/PycharmProjects/gene-pc-api/data/consent'), upload_to=''),
        ),
    ]
