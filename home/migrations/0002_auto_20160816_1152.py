# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastor',
            name='background',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='welcome',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='welcome',
            name='note',
            field=models.TextField(),
        ),
    ]