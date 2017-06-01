# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commonData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u65b0\u95fb\u540d\u79f0')),
                ('htmlContent', models.CharField(max_length=200, verbose_name='\u65b0\u95fb\u5185\u5bb9')),
                ('date published', models.DateTimeField(verbose_name='\u65b0\u95fb\u53d1\u5e03\u65f6\u95f4')),
                ('image1', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72471')),
                ('image2', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72472')),
                ('image3', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72473')),
                ('image4', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72474')),
                ('image5', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72475')),
                ('new_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='commonData.NewType', verbose_name='\u65b0\u95fb\u7c7b\u522b')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonData.Status', verbose_name='\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb',
                'verbose_name_plural': '\u65b0\u95fb',
            },
        ),
        migrations.CreateModel(
            name='OfficeBuildingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u5199\u5b57\u697c\u540d\u79f0')),
                ('title_des', models.CharField(max_length=200, verbose_name='\u5199\u5b57\u697c\u8bf4\u660e')),
                ('address', models.CharField(default='', max_length=200, verbose_name='\u5730\u5740')),
                ('rent_max_price', models.IntegerField(verbose_name='\u6700\u5927\u79df\u91d1')),
                ('rent_min_price', models.IntegerField(verbose_name='\u6700\u5c0f\u79df\u91d1')),
                ('areaNum', models.IntegerField(verbose_name='\u603b\u9762\u79ef')),
                ('floorNum', models.IntegerField(verbose_name='\u603b\u697c\u5c42')),
                ('transport', models.CharField(max_length=200, verbose_name='\u9644\u8fd1\u4ea4\u901a')),
                ('information', models.CharField(max_length=2000, verbose_name='\u623f\u6e90\u4fe1\u606f')),
                ('description', models.CharField(max_length=2000, verbose_name='\u623f\u6e90\u63cf\u8ff0')),
                ('buildTime', models.DateTimeField(verbose_name='\u5927\u53a6\u5efa\u6210\u65f6\u95f4')),
                ('createTime', models.DateTimeField(verbose_name='\u4fe1\u606f\u53d1\u5e03\u65f6\u95f4')),
                ('location', models.CharField(default='0.0', max_length=200, verbose_name='\u5730\u56fe\u5750\u6807')),
                ('image1', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72471')),
                ('image2', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72472')),
                ('image3', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72473')),
                ('image4', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72474')),
                ('image5', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72475')),
                ('image6', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72476')),
                ('area_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonData.Area', verbose_name='\u6240\u5728\u533a\u57df')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonData.Status', verbose_name='\u72b6\u6001')),
                ('subway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonData.Subway', verbose_name='\u5730\u94c1')),
            ],
            options={
                'verbose_name': '\u5199\u5b57\u697c',
                'verbose_name_plural': '\u5199\u5b57\u697c',
            },
        ),
        migrations.CreateModel(
            name='OfficeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u623f\u6e90\u540d\u79f0')),
                ('rent_price', models.IntegerField(verbose_name='\u79df\u91d1')),
                ('areaNum', models.IntegerField(verbose_name='\u9762\u79ef')),
                ('floorNum', models.IntegerField(verbose_name='\u697c\u5c42')),
                ('information', models.CharField(max_length=2000, verbose_name='\u623f\u6e90\u4fe1\u606f')),
                ('description', models.CharField(max_length=2000, verbose_name='\u623f\u6e90\u63cf\u8ff0')),
                ('date published', models.DateTimeField(verbose_name='\u4fe1\u606f\u53d1\u5e03\u65f6\u95f4')),
                ('image1', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72471')),
                ('image2', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72472')),
                ('image3', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72473')),
                ('image4', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72474')),
                ('image5', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72475')),
                ('image6', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/', verbose_name='\u56fe\u72476')),
                ('officeBuilding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publish.OfficeBuildingList', verbose_name='\u6240\u5c5e\u6240\u5b57\u697c')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonData.Status', verbose_name='\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u5199\u5b57\u697c',
                'verbose_name_plural': '\u5199\u5b57\u697c',
            },
        ),
    ]
