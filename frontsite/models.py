# coding: UTF-8

from __future__ import unicode_literals

from django.db import models
from commonData.models import DecorateDegree, Status, Sex, Area, Subway, District, UseType
from publish.models import OfficeBuildingList, OfficeList


class Account(models.Model):
    telephone = models.CharField('手机号',max_length=200)
    password = models.CharField('密码',max_length=200)
    nickname = models.CharField('昵称',max_length=200)
    realname = models.CharField('真实姓名',max_length=200)
    IDNum = models.CharField('身份证号码',max_length=200)
    sex = models.ForeignKey(Sex, verbose_name='性别',default=1)
    age = models.IntegerField('年龄')
    card = models.CharField('银行卡号',max_length=200)
    address = models.CharField('地址',max_length=200)
    createTime = models.DateTimeField('时间','date published',auto_now=True)
    status = models.ForeignKey(Status,verbose_name='状态', default=1)

    def __unicode__(self):
        return u'%s' % self.telephone

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class HouseSource(models.Model):
    title = models.CharField('房源名称',max_length=200)
    area_type = models.ForeignKey(Area,verbose_name='所在地区',  default=1)
    district_type = models.ForeignKey(District,verbose_name='所在街道',  default=1)
    address = models.CharField('详细地址',max_length=200)
    use_type = models.ForeignKey(UseType, verbose_name='房源用途', default=1)
    areaNum = models.IntegerField('建筑面积')
    rent_all_type=models.CharField('出租户型',max_length=200)
    decorate_type=models.ForeignKey(DecorateDegree,verbose_name='装修程度',  default=1)
    description = models.CharField('房源描述',max_length=200)
    corporationList = models.CharField('入信企业', max_length=200)
    userid=models.ForeignKey(Account, verbose_name='创建用户',default=1)
    createTime = models.DateTimeField('时间', 'date published',auto_now=True)
    status = models.ForeignKey(Status,verbose_name='状态',  default=1)

    image1 = models.ImageField('图片1', upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image2 = models.ImageField('图片2', upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image3 = models.ImageField('图片3', upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image4 = models.ImageField('图片4', upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image5 = models.ImageField('图片5', upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image6 = models.ImageField('图片6', upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = '用户房源'
        verbose_name_plural = '用户房源'


class HouseRequirement(models.Model):
    name = models.CharField('用户姓名',max_length=200)
    telephone = models.CharField('用户手机号',max_length=200)
    description = models.CharField('需求描述',max_length=200)

    userid=models.ForeignKey(Account, verbose_name='创建用户',default=1)
    createTime = models.DateTimeField('时间', 'date published',auto_now=True)
    status = models.ForeignKey(Status,verbose_name='状态',  default=1)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = '用户需求'
        verbose_name_plural = '用户需求'


class ServiceRequirement(models.Model):
    name = models.CharField('用户姓名',max_length=200)
    telephone = models.CharField('用户手机号',max_length=200)
    description = models.CharField('需求描述',max_length=500)
    servicetype = models.CharField('需求类型', max_length=200,default='')

    createTime = models.DateTimeField('时间', 'date published',auto_now=True)
    status = models.ForeignKey(Status, verbose_name='状态', default=1)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = '服务需求'
        verbose_name_plural = '服务需求'


class Order(models.Model):
    officeBuilding=models.ForeignKey(OfficeBuildingList,verbose_name="房源",default=1)
    userid=models.ForeignKey(Account, verbose_name='创建用户',default=1)
    createTime = models.DateTimeField('时间', 'date published',auto_now=True)
    status = models.ForeignKey(Status, verbose_name='状态', default=1)

    def __unicode__(self):
        return u'%s' % self.officeBuilding.name

    class Meta:
        verbose_name = '所有订单'
        verbose_name_plural = '所有订单'


class Corporation(models.Model):
    businessLicence = models.ImageField('营业执照', upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    corporateCharter = models.ImageField('法人证件', upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    telephone = models.CharField('对接人电话',max_length=200)
    serviceContent = models.CharField('主要服务内容',max_length=200)

    userid = models.ForeignKey(Account, verbose_name="创建人", default=1)

    createTime = models.DateTimeField('信息发布时间','date published',auto_now=True)

    def __unicode__(self):
        return u'%s' % self.telephone

    class Meta:
        verbose_name = '注册企业'
        verbose_name_plural = '注册企业'


class Messages(models.Model):
    fromUser = models.ForeignKey(Account,verbose_name="发件人",related_name="message_fromuser_account")
    toUser = models.ForeignKey(Account,verbose_name="收件人",related_name="message_touser_account")
    title = models.CharField('信息标题', max_length=2000)
    body = models.CharField('信息内容',max_length=2000)

    userid = models.ForeignKey(Account,verbose_name="创建人",related_name="message_userid_account")

    createTime = models.DateTimeField('信息发布时间','date published',auto_now=True)
    status= models.ForeignKey(Status,verbose_name='状态')

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = '消息中心'
        verbose_name_plural = '消息中心'