# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-17 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20191112_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='county',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postcode',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street_Address1',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street_Address2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='town_or_city',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]