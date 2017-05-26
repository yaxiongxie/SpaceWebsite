# coding: UTF-8

from __future__ import unicode_literals

from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     question_body = models.TextField(max_length=300, default='')
#     question_image = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
#
#     def __str__(self):
#         return self.question_text
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text



class Country(models.Model):
    country_name = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.country_name

    class Meta:
        verbose_name = '区'
        verbose_name_plural = '区'


class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200,blank=True)
    age=models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Subway(models.Model):
    subway_name = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.subway_name

    class Meta:
        verbose_name = '地铁'
        verbose_name_plural = '地铁   '

class CmsStatus(models.Model):
    status_name = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.status_name


class OfficeBuilding(models.Model):
    title = models.CharField('名称',max_length=200)
    address = models.CharField(max_length=200,default='')
    subwayDescription=models.CharField(max_length=200,default='')
    rent_price = models.IntegerField()
    sale_price = models.IntegerField()
    seats = models.CharField(max_length=200,default='')
    decoration = models.CharField(max_length=200)
    userTime = models.CharField(max_length=200)
    floorNum = models.IntegerField()
    priceInclude = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200, default='')
    totalArea = models.IntegerField()
    blockNum = models.IntegerField()
    carNum = models.IntegerField()
    level = models.CharField(max_length=200,default='')
    floorHeight = models.IntegerField()
    elevatorNum = models.IntegerField()
    propertyCompany = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    subway = models.ForeignKey(Subway, on_delete=models.CASCADE)
    createTime = models.DateTimeField('date published')
    buildTime = models.DateTimeField('date published')
    sortNum = models.IntegerField(default=0)
    seeNum = models.IntegerField(default=0)
    status= models.ForeignKey(CmsStatus, on_delete=models.CASCADE,default=1)
    location = models.CharField(max_length=200,default='0.0')
    image1 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image2 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image3 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image4 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image5 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image6 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = '写字楼'
        verbose_name_plural = '写字楼'


class RoomType(models.Model):
    room_type = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.room_type


class RoomDirection(models.Model):
    room_direction = models.CharField(max_length=200)
    sort_int = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.room_direction


class Rent(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    area = models.IntegerField()
    subway_str = models.CharField(max_length=200,default='')
    country_str = models.CharField(max_length=200,default='')
    telephone = models.CharField(max_length=200)
    rentType = models.CharField(max_length=200)
    payType = models.CharField(max_length=200)
    currentStatus = models.CharField(max_length=200)
    heatingType = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    subway = models.ForeignKey(Subway, on_delete=models.CASCADE)
    roomType = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    roomDirection = models.ForeignKey(RoomDirection, on_delete=models.CASCADE)
    createTime = models.DateTimeField('date published')
    sortNum = models.IntegerField(default=0)
    seeNum = models.IntegerField(default=0)
    status = models.ForeignKey(CmsStatus, on_delete=models.CASCADE,default=1)
    location = models.CharField(max_length=200,default='0.0')
    image1 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image2 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image3 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image4 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image5 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image6 = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __unicode__(self):
        return u'%s' % self.title
