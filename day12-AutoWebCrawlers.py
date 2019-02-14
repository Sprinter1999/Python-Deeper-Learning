# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:07:41 2019
Today is for web crawlers"
@author: 21543
"""
'''
eg1
import requests
r=requests.get('http://www.baidu.com')
print(r.status_code)
print(r.encoding)
r.encoding='utf-8'
print(r.encoding)
print(r.text)
eg2
import requests
def getHTMLText(r):
    try:
        r = requests.get(url, timeout=200)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text
    except:
        return ""
url = "http://www.baidu.com"
print(getHTMLText(url))


import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.baidu.com')
r.encoding='utf-8'
soup=BeautifulSoup(r.text)
print(soup.head)
bs对象有常用的几个属性，比如head是HTML界面的<head>content
title is HTMl UI's <title> part in <head> part
body is namely the body part
p is the first <p> content shown in this HTML UI
而比如soup.a也是一个新的对象,比如他是一个标签，他也有一些属性，比如name，attrs，contents，string
import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.baidu.com')
r.encoding='utf-8'
soup=BeautifulSoup(r.text)
print(soup.a.name)
而这个a只是第一次出现，如果要求出所有出现，则用findAll方法

import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.baidu.com')
r.encoding='utf-8'
soup=BeautifulSoup(r.text)
a=soup.find_all('a')
print(len(a))
#而findALL方法的全部参数是name查找名，attrs属性键值对，recursive设置查找层次，string，limit限制查找个数
#find方法也是之查找第一个
#eg CrawUnivRanking.py针对某个特定的网站的爬虫，并不具有普适性
import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        #r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
def printUnivList(num):
    print("{:^4}{:^10}{:^5}{:^8}{:^10}".format("排名","学校名称","省市","总分","培养规模"))
    for i in range(num):
        u=allUniv[i]
        print("{:^4} {:^10} {:^5} {:^8} {:^10}".format(u[0],u[1],u[2],u[3],u[6]))
def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(20)
main()

https://blog.csdn.net/qq_41686130/article/details/79856474 配合食用
要想以后再深入爬虫实践，必须对HTML结构有一个更清楚的认识，改天再开个HTML库8


'''
#自动搜索引擎爬虫
import requests
from bs4 import BeautifulSoup
#import re
import json
def getKeywordResult(keyword):
    url = 'http://www.baidu.com/s?wd='+keyword
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def parserLinks(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for div in soup.find_all('div', {'data-tools': re.compile('title')}):
        data = div.attrs['data-tools']  #获得属性值
        d = json.loads(data)        #将属性值转换成字典
        #json javascript object notation
        links.append(d['title'])    #将返回链接的题目返回
    return links
def main():
    html = getKeywordResult('邱建鑫')
    ls = parserLinks(html)
    count = 1
    for i in ls:
        print("[{:^3}]{}".format(count, i))
        count += 1
main()












