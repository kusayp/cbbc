# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pastor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('background', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('pastor', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
    ]
