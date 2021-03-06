# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-11 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('facility', models.TextField()),
                ('roomtype', models.TextField()),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('zoom', models.PositiveSmallIntegerField(default=14)),
                ('site', models.CharField(max_length=200)),
            ],
        ),
    ]
