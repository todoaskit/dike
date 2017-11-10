# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 09:23
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdike', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(choices=[('SP', 'Splitted'), ('PO', 'Polished'), ('CN', 'Connected'), ('EX', 'Explained')], max_length=2)),
                ('sid', models.IntegerField()),
                ('vote', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('result', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.RenameField(
            model_name='document',
            old_name='made_at',
            new_name='announced_at',
        ),
    ]
