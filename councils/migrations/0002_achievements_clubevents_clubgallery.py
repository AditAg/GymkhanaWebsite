# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('councils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_title', models.CharField(max_length=100)),
                ('achievement_detail', models.CharField(max_length=500)),
                ('achievement_image', models.CharField(max_length=300)),
                ('council', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='councils.Councils')),
            ],
        ),
        migrations.CreateModel(
            name='Clubevents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=100)),
                ('event_detail', models.CharField(max_length=500)),
                ('event_image', models.CharField(max_length=300)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='councils.Clubs')),
            ],
        ),
        migrations.CreateModel(
            name='Clubgallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubgallery_image', models.CharField(max_length=300)),
                ('clubgallery_title', models.CharField(max_length=200)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='councils.Clubs')),
            ],
        ),
    ]