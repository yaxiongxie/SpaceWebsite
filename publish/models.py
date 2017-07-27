# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from commonData.models import Area,Subway,Status,NewType,District,SourceType


class OfficeBuildingList(models.Model):
    title = models.CharField('写字楼名称',max_length=200)
    area_type = models.ForeignKey(Area, verbose_name='所在区域')
    district_type = models.ForeignKey(District, verbose_name='所在街道', blank=True, null=True)
    subway = models.ForeignKey(Subway, verbose_name='地铁', null=True, blank=True)
    address = models.CharField('地址',max_length=200,default='')
    transport = models.CharField('附近交通', max_length=200,default='',null=True,blank=True)
    rent_count=models.IntegerField('在租房源个数',default=1)
    rent_max_price = models.IntegerField('最大租金',default=1)
    rent_min_price = models.IntegerField('最小租金',default=1)
    rent_max_area=models.IntegerField('最大可租面积',default=1)
    rent_min_area=models.IntegerField('最小可租面积',default=1)
    floor_count=models.IntegerField('总楼层',default=1)
    rent_area=models.CharField('可租面积（多个用逗号连接）',max_length=200,null=True,blank=True)
    information = models.TextField('房源信息',max_length=2000,null=True,blank=True)
    information_match=models.TextField('房源配套',max_length=500,null=True,blank=True)
    building_type= models.ForeignKey(SourceType,verbose_name='类型',default=1)
    buildTime = models.DateTimeField('大厦建成时间')
    createTime = models.DateTimeField('信息发布时间',auto_now=True)

    location = models.CharField('地图坐标',max_length=200, default='0.0',null=True,blank=True)
    status= models.ForeignKey(Status,verbose_name='状态')

    image1 = models.ImageField('图片1',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image2 = models.ImageField('图片2',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image3 = models.ImageField('图片3',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image4 = models.ImageField('图片4',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image5 = models.ImageField('图片5',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image6 = models.ImageField('图片6',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = '楼盘'
        verbose_name_plural = '楼盘'


class OfficeList(models.Model):
    officeBuilding = models.ForeignKey(OfficeBuildingList, verbose_name='所属所字楼')

    title = models.CharField('房源名称',max_length=200)
    rent_price = models.IntegerField('租金',default=0)
    areaNum = models.IntegerField('面积',default=0)
    floorNum = models.IntegerField('楼层',default=0)
    information = models.TextField('房源信息',max_length=2000,null=True,blank=True)

    ownerName=models.CharField('房东姓名',max_length=200,default='',blank=True,null=True)
    ownerTelephone = models.CharField('房东联系电话', max_length=200,default='',blank=True,null=True)
    ownerInformation = models.TextField('房东要求', max_length=200,default='',blank=True,null=True)

    createTime = models.DateTimeField('信息发布时间',auto_now=True)
    status= models.ForeignKey(Status,verbose_name='状态')

    image1 = models.ImageField('图片1',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image2 = models.ImageField('图片2',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image3 = models.ImageField('图片3',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image4 = models.ImageField('图片4',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image5 = models.ImageField('图片5',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)
    image6 = models.ImageField('图片6',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg',null=True,blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = '房源'
        verbose_name_plural = '房源'



class News(models.Model):
    title = models.CharField('新闻名称',max_length=200)
    abstractText = models.CharField('新闻摘要', max_length=200,default='')
    htmlContent = models.TextField('新闻内容',default='')
    new_type = models.ForeignKey(NewType,verbose_name="新闻类别",default=1)
    createTime = models.DateTimeField('新闻发布时间',auto_now=True)
    status= models.ForeignKey(Status,verbose_name='状态')

    image1 = models.ImageField('图片1',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image2 = models.ImageField('图片2',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image3 = models.ImageField('图片3',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image4 = models.ImageField('图片4',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image5 = models.ImageField('图片5',upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'