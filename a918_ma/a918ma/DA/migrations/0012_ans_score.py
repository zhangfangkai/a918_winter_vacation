# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DA', '0011_auto_20170901_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ans_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.IntegerField()),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DA.Record')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DA.Score')),
            ],
        ),
    ]
