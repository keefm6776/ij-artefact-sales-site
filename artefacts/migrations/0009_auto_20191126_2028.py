# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-26 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artefacts', '0008_auto_20191124_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artefact',
            name='century',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
