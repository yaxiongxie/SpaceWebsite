# -*- coding: utf-8 -*-

# /Users/xieyaxiong/Downloads/html
import sys
import urllib2
from xlwt import *

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import re
from bs4 import BeautifulSoup


# totalArr=[]
# urlArr=[]
# for j in range(1,2):
#
#     titleArr=[]
#     addressArr=[]
#     priceArr=[]
#     file_object = urllib2.urlopen('http://www.haozu.com/wh/zuxiezilou/o'+str(j)+'/')
#     try:
#          all_the_text = file_object.read()
#          soup = BeautifulSoup(all_the_text)
#
#
#          arr=soup.find_all('h1')
#          for a in arr:
#              if a.a:
#                  urlArr.append(a.a["href"])
#         titleArr.append(htag.a.string.strip())
# addressarr=soup.find_all('p')
# for aa in addressarr:
#     aaarr=aa.contents
#     if aaarr:
#         if len(aaarr)>7:
#            print aa.contents[2].string.strip()
#            address=aa.contents[2].string.strip()+'-'+aa.contents[4].string.strip()+"-"+aa.contents[7].string.strip()
#            addressArr.append(address.strip())
#
# price = soup.find_all('span')
# for sp in price:
#     sparr = sp.contents
#     if sparr:
#         if len(sparr) > 1:
#                 p1 = sparr[0].string
#                 p2 = sparr[1].string
#                 if p1 is None:
#                     continue
#                 if p2 is None:
#                     continue
#                 priceStr=p1+' '+p2
#                 if '元' in priceStr:
#                    priceArr.append(priceStr.strip())


# finally:
#      file_object.close( )

#     for i in range(len(titleArr)):
#         map={"title":titleArr[i],"address":addressArr[i],"price":priceArr[i]}
#         totalArr.append(map)
#
#     print j
# print len(urlArr)
# for i in range(len(urlArr)):
#     print urlArr[i]

def getMap(url):
    map = {}
    file_object = urllib2.urlopen(url)
    try:
        all_the_text = file_object.read()
        soup = BeautifulSoup(all_the_text)

        ul = soup.find_all('ul', {'class': 'profile-box clearfix'})
        htag = BeautifulSoup(str(ul))
        liArr = htag.find_all('div')
        print liArr
        spanArr = htag.find_all('span')
        for li in range(len(liArr)):
            key = str(liArr[li].string).decode('unicode–escape')
            if key == '总楼层：':
                map['总楼层：'] = str(spanArr[li].string).decode('unicode–escape')
            if key == '建筑面积：':
                map['建筑面积：'] = str(spanArr[li].string).decode('unicode–escape')
            if key == '得房率：':
                map['得房率：'] = str(spanArr[li].string).decode('unicode–escape')
            if key == '客梯数：':
                map['客梯数：'] = str(spanArr[li].string).decode('unicode–escape')
            if key == '开发商：':
                map['开发商：'] = str(spanArr[li].string).decode('unicode–escape')
            if key == '物业公司：':
                map['物业公司：'] = str(spanArr[li].string).decode('unicode–escape')
            if key == '已入驻企业：':
                map['已入驻企业：'] = str(spanArr[li].string).decode('unicode–escape')


            # for info in infoArr:
            #     if info.li:
            #         infoLiArr=info.li;
            #         for li in infoLiArr:


            # tArr=soup.find_all('h1',{'class':'h1-title'})
            # print str(tArr[0].contents).decode('unicode–escape')
            #
            #
            # aArr=soup.find_all('p',{'class':'p2'})
            # for a in aArr:
            #
            #     print str(a.contents).decode('unicode–escape')

    finally:
        file_object.close()
    # print '======================'
    # if map.has_key('总楼层：'):
    #     print '总楼层：' + map.get('总楼层：')
    # if map.has_key('建筑面积：'):
    #     print '建筑面积：' + map.get('建筑面积：')
    # if map.has_key('得房率：'):
    #     print '得房率：' + map.get('得房率：')
    # if map.has_key('客梯数：'):
    #     print '客梯数：' + map.get('客梯数：')
    # if map.has_key('开发商：'):
    #     print '开发商：' + map.get('开发商：')
    # if map.has_key('物业公司：'):
    #     print '物业公司：' + map.get('物业公司：')
    return map;
# count=0
#
# book = Workbook()
# sheet1 = book.add_sheet('Sheet 1')
# for tl in range(len(totalArr)):
#     o=totalArr[tl]
#     sheet1.write(tl, 0, o.get("title"))
#     sheet1.write(tl, 1, o.get("address"))
#     sheet1.write(tl, 2, o.get("price"))
#
#     print str(count)+o.get("title")+o.get("address")+o.get("price")
# book.save("/tmp/collectData.xls")

