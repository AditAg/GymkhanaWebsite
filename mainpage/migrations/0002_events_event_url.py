# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_url',
            field=models.CharField(default='', max_length=300),
        ),
    ]