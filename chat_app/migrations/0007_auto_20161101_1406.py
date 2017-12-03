# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-01 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0006_auto_20161101_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='room',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat_app.ChatRoom'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='label',
            field=models.SlugField(default='1', unique=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
