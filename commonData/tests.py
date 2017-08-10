# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import DownloadImages

DownloadImages.save_img('http://fang-oss.haozu.com/cms/index/2017/03/21/WfBKRS4mRH.jpg',"test","/tmp/images/")