# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-04 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=45)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
    ]
