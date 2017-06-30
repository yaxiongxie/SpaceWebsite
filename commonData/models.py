# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Subway(models.Model):
    subway_name = models.CharField('地铁名称',max_length=200)
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.subway_name

    class Meta:
        verbose_name = '地铁'
        verbose_name_plural = '地铁'

class ServiceType(models.Model):
    service_type_name = models.CharField('服务类别',max_length=200)
    information = models.TextField('服务类别内容', max_length=2000,default='')
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.service_type_name

    class Meta:
        verbose_name = '商业服务类别'
        verbose_name_plural = '商业服务类别'


class Services(models.Model):
    service_name = models.CharField('服务名称',max_length=200)
    information = models.TextField('服务内容', max_length=2000)
    small_image = models.CharField('小图标',max_length=200,default='')
    small_image_color = models.CharField('小图标_彩色',max_length=200, default='')
    large_image = models.CharField('大图标',max_length=200, default='')
    sort_int = models.IntegerField('排序号')
    service_type = models.ForeignKey(ServiceType, verbose_name='所属类型')

    def __unicode__(self):
        return u'%s' % self.service_name

    class Meta:
        verbose_name = '商业服务'
        verbose_name_plural = '商业服务'


class Area(models.Model):
    country_name = models.CharField('区名',max_length=200)
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.country_name

    class Meta:
        verbose_name = '区'
        verbose_name_plural = '区'


class District(models.Model):
    district_name = models.CharField('街道名',max_length=200)
    district_firstChar = models.CharField('街道名首字母', max_length=200)
    sort_int = models.IntegerField('排序号')
    area_type = models.ForeignKey(Area, verbose_name='所属区域', default=1)

    def __unicode__(self):
        return u'%s' % self.district_name

    class Meta:
        verbose_name = '街道'
        verbose_name_plural = '街道'


class SourceType(models.Model):
    source_type_name = models.CharField('房源类型',max_length=200)
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.source_type_name

    class Meta:
        verbose_name = '房源类型'
        verbose_name_plural = '房源类型'


class UseType(models.Model):
    use_name = models.CharField('房源用途',max_length=200)
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.use_name

    class Meta:
        verbose_name = '房源用途'
        verbose_name_plural = '房源用途'


class DecorateDegree(models.Model):
    decorate_name = models.CharField('装修程序',max_length=200)
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.decorate_name

    class Meta:
        verbose_name = '装修程序'
        verbose_name_plural = '装修程序'



class NewType(models.Model):
    type_name = models.CharField('新闻类别',max_length=200)
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.type_name

    class Meta:
        verbose_name = '新闻类别'
        verbose_name_plural = '新闻类别'

class Sex(models.Model):
    sex_name = models.CharField('性别',max_length=200)
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.sex_name

    class Meta:
        verbose_name = '性别'
        verbose_name_plural = '性别'


class Status(models.Model):
    status_name = models.CharField('状态',max_length=200)
    sort_int = models.IntegerField('排序号')

    def __unicode__(self):
        return u'%s' % self.status_name

    class Meta:
        verbose_name = '状态'
        verbose_name_plural = '状态'