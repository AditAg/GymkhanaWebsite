# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-13 14:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_user_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_events',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]