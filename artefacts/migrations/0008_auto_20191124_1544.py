# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-24 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artefacts', '0007_auto_20191123_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artefact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]
