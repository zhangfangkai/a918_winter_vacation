# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 10:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DA', '0002_ans_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ans_score',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='ans_score',
            name='record',
        ),
        migrations.DeleteModel(
            name='Ans_score',
        ),
    ]
