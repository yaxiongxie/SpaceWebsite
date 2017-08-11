# -*- coding: utf-8 -*-

# /Users/xieyaxiong/Downloads/html
import sys
import urllib2
import urllib
from xlwt import *
import CollectionUtil4

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import re
import os
import redis
from bs4 import BeautifulSoup


def save_img(img_url,file_name,file_path='book\img'):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print '文件夹',file_path,'不存在，重新建立'
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
       #下载图片，并保存到文件夹中
        urllib.urlretrieve(img_url,filename=filename)
    except IOError as e:
        print '文件操作失败',e
    except Exception as e:
        print '错误 ：',e

r = redis.Redis(host='118.31.46.32',password='Xieyaxiong9', port=6379, db=0)
totalArr = []
for j in range(1, 11):

    titleArr = []
    addressArr = []
    priceArr = []
    attArr = []
    file_object = urllib2.urlopen('http://www.haozu.com/wh/zuxiezilou/o' + str(j) + '/')
    try:
        all_the_text = file_object.read()
        soup = BeautifulSoup(all_the_text)

        arr = soup.find_all('h1')
        for a in arr:
            htag = BeautifulSoup(str(a))
            if htag.a:
                url = "http://www.haozu.com" + htag.a["href"]
                attMap = CollectionUtil4.getMap(url)
                # attArr.append(attMap)
                titleArr.append(htag.a.string.strip())
                print attMap
                for li in attMap:
                    r.sadd('buildings_' + htag.a.string.strip(), li)
        # addressarr = soup.find_all('p')
        # for aa in addressarr:
        #     aaarr = aa.contents
        #     if aaarr:
        #         if len(aaarr) > 7:
        #             address = aa.contents[2].string.strip() + '-' + aa.contents[4].string.strip() + "-" + aa.contents[
        #                 7].string.strip()
        #             addressArr.append(address.strip())
        #
        # price = soup.find_all('span')
        # for sp in price:
        #     sparr = sp.contents
        #     if sparr:
        #         if len(sparr) > 1:
        #             p1 = sparr[0].string
        #             p2 = sparr[1].string
        #             if p1 is None:
        #                 continue
        #             if p2 is None:
        #                 continue
        #             priceStr = p1 + ' ' + p2
        #             if '元' in priceStr:
        #                 priceArr.append(priceStr.strip())


    finally:
        file_object.close()



    # for i in range(len(titleArr)):
    #     # map = {"title": titleArr[i], "address": addressArr[i], "price": priceArr[i]}
    #     # newMap = dict(map.items() + attArr[i].items())
    #     #
    #     # totalArr.append(newMap)
    #     # r.sadd('building_'+titleArr[i],attArr[i].get('images'))
    #     print titleArr[i]
    #     print attArr[i].get("images")


    print j
count = 0


