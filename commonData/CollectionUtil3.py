# -*- coding: utf-8 -*-

# /Users/xieyaxiong/Downloads/html
import sys
import urllib2
from xlwt import *
import CollectionUtil2

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import re
from bs4 import BeautifulSoup

totalArr = []
for j in range(1, 14):

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
                attMap = CollectionUtil2.getMap(url)
                attArr.append(attMap)
                titleArr.append(htag.a.string.strip())
        addressarr = soup.find_all('p')
        for aa in addressarr:
            aaarr = aa.contents
            if aaarr:
                if len(aaarr) > 7:
                    address = aa.contents[2].string.strip() + '-' + aa.contents[4].string.strip() + "-" + aa.contents[
                        7].string.strip()
                    addressArr.append(address.strip())

        price = soup.find_all('span')
        for sp in price:
            sparr = sp.contents
            if sparr:
                if len(sparr) > 1:
                    p1 = sparr[0].string
                    p2 = sparr[1].string
                    if p1 is None:
                        continue
                    if p2 is None:
                        continue
                    priceStr = p1 + ' ' + p2
                    if '元' in priceStr:
                        priceArr.append(priceStr.strip())


    finally:
        file_object.close()

    for i in range(len(titleArr)):
        map = {"title": titleArr[i], "address": addressArr[i], "price": priceArr[i]}
        newMap = dict(map.items() + attArr[i].items())

        totalArr.append(newMap)

    print j
count = 0

book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
for tl in range(len(totalArr)):
    o = totalArr[tl]
    print o
    sheet1.write(tl, 0, o.get("title"))
    sheet1.write(tl, 1, o.get("address"))
    sheet1.write(tl, 2, o.get("price"))
    try:
        sheet1.write(tl, 3, o.get("总楼层："))
    except:
        sheet1.write(tl, 3, 'aa')
    try:
        sheet1.write(tl, 4, o.get("建筑面积："))
    except:
        sheet1.write(tl, 4, 'aa')
    try:
        sheet1.write(tl, 5, o.get("得房率："))
    except:
        sheet1.write(tl, 5, 'aa')
    try:
        sheet1.write(tl, 6, o.get("客梯数："))
    except:
        sheet1.write(tl, 6, 'aa')
    try:
        sheet1.write(tl, 7, o.get("开发商："))
    except:
        sheet1.write(tl, 7, 'aa')
    try:
        sheet1.write(tl, 8, o.get("物业公司："))
    except:
        sheet1.write(tl, 8, 'aa')
    try:
        sheet1.write(tl, 9, o.get("已入驻企业："))
    except:
        sheet1.write(tl, 9, 'aa')

print str(count) + o.get("title") + o.get("address") + o.get("price")
book.save("/tmp/collectData.xls")
