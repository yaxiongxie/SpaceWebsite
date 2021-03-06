# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200, verbose_name='\u533a\u540d')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u533a',
                'verbose_name_plural': '\u533a',
            },
        ),
        migrations.CreateModel(
            name='DecorateDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decorate_name', models.CharField(max_length=200, verbose_name='\u88c5\u4fee\u7a0b\u5e8f')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u88c5\u4fee\u7a0b\u5e8f',
                'verbose_name_plural': '\u88c5\u4fee\u7a0b\u5e8f',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=200, verbose_name='\u8857\u9053\u540d')),
                ('district_firstChar', models.CharField(max_length=200, verbose_name='\u8857\u9053\u540d\u9996\u5b57\u6bcd')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u8857\u9053',
                'verbose_name_plural': '\u8857\u9053',
            },
        ),
        migrations.CreateModel(
            name='NewType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200, verbose_name='\u65b0\u95fb\u7c7b\u522b')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u7c7b\u522b',
                'verbose_name_plural': '\u65b0\u95fb\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex_name', models.CharField(max_length=200, verbose_name='\u6027\u522b')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u6027\u522b',
                'verbose_name_plural': '\u6027\u522b',
            },
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type_name', models.CharField(max_length=200, verbose_name='\u623f\u6e90\u7c7b\u578b')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u623f\u6e90\u7c7b\u578b',
                'verbose_name_plural': '\u623f\u6e90\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=200, verbose_name='\u72b6\u6001')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u72b6\u6001',
                'verbose_name_plural': '\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subway_name', models.CharField(max_length=200, verbose_name='\u5730\u94c1\u540d\u79f0')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u5730\u94c1',
                'verbose_name_plural': '\u5730\u94c1',
            },
        ),
        migrations.CreateModel(
            name='UseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_name', models.CharField(max_length=200, verbose_name='\u623f\u6e90\u7528\u9014')),
                ('sort_int', models.IntegerField(verbose_name='\u6392\u5e8f\u53f7')),
            ],
            options={
                'verbose_name': '\u623f\u6e90\u7528\u9014',
                'verbose_name_plural': '\u623f\u6e90\u7528\u9014',
            },
        ),
    ]
