# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-23 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artefacts', '0004_auto_20191123_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artefact',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]
