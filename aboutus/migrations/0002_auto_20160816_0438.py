# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='wwb',
            name='content',
            field=models.TextField(),
        ),
    ]
