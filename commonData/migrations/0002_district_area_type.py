# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='area_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='commonData.Area', verbose_name='\u6240\u5c5e\u533a\u57df'),
        ),
    ]
