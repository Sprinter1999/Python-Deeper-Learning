# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:02:31 2019

@author: 21543
"""

'''
列表比较常用，用[]表征，比如 ls=[123,213,132,"adsasd",[1,2,3,3]]
list()可以将元组或者字符串转化为列表类型
值得注意的是，简单将一个列表赋值给另一个列表，lis2=lis1并不会产生新的列表，而是引用
所以二者指向的是同一个对象
列表特有的方法：
ls[i]=x
ls[i:j]=lt
ls[i:j:k]=lt
del ls[i:j]
del ls[i:j:k]
ls+=lt or ls.extend(lt)
ls*=n
ls.append(x)
ls.clear()
ls.copy()拷贝一份
ls.insert(i,x)
ls.pop(i)
ls.remove(x)
ls.reverse()

字典类型：
country={"zhongguo":'beijing','faguo':'bali'}
print(country['zhongguo'])#访问字典键值
初始化一个空字典的方式是{}，初始化一个空集合方式是set（）

对于一个字典而言，有如下的方法：
keys()
values()
items()#一个键值对为一项
get(键名，默认值)键存在则返回键值，否则返回默认值
pop（键名，默认值）存在该键则返回键值并将该键值对出栈，若不存在则返回默认值
popitem()随机取出一项
clear()
向字典添加元素有如下几种方法：
>>> d = {'a': 1}
>>> d.update(b=2)
>>> d
{'a': 1, 'b': 2}
>>> d.update(c=3, d=4)
>>> d
{'a': 1, 'c': 3, 'b': 2, 'd': 4}
>>> d['e'] = 5
>>> d
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> d.update({'f': 6, 'g': 7})
>>> d
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6}

估计在NLP中队jieba库要求比较高，于是安装了jieba库，顺带更新了一发pip
jieba库了解就行，暂时不多看

import this
明天开始学习文件和数据格式化这一节

'''
#e10.2CalHamlet.py词频统计
excludes = {"the","and","of","you","a","i","my","in","to"}
def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
hamletTxt = getText()
words  = hamletTxt.split()
counts = {}
for word in words:			
    counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])    
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))


