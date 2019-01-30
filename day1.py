# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:28:35 2019

@author: 21543
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:05:02 2019

@author: 21543
"""

"""
//ex1
r=25;
area=3.1415*r*r;
print(area)
print("{:.2f}".format(area))
//ex2
name=input("输入姓名：")
print("{}，你可听过这句歌词，鼓动我，卷走我，烤面筋融化我".format(name))
print("{}，你可听过这句歌词，鼓动我，卷走我，烤面筋融化我".format(name[0]))
print("{}，你可听过这句歌词，鼓动我，卷走我，烤面筋融化我".format(name[1:]))
//ex3
#Fibonacci array,Fn / Fn-1 ~ 1.618
a,b=0,1;#同时赋值语法
while a<100:
    print(a,end=',')
    a,b=b,a+b #再一次同时赋值
//ex4
#用到turtle可能不适合用IDE，还是用IDLE or terminal比较好
import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(100)
turtle.circle(80)
turtle.circle(50)
当然，也可以这么用
from turtle import *,这样后面就不必每次都加**模块.**功能这样复杂的前缀了
//ex5
from datetime import datetime
now=datetime.now()
print(now)
now.strftime("%x")
now.strftime("%x")
//ex6
python的版本差异较大，并不向后兼容老版本
2.x:print函数不带(),3.x:print函数带括号
2.x与3.x在进行比较时，比如1<"1"，在老版本会产生false，而在新版本会提示tyeperror
2.x中3/2得到1，同C语言，而在新版本中3/2得到1.5浮点数，而用3//2才表示整数除法
3.x版本八进制格式改成以0o开头
range()有修改，比如//range(a,b)前闭后开
2.x: range(10) ==>产生一个10以内的0~9的表
3.x:range(10)====>产生一个range(0,10)
3.x:list(range(10))==>产生一个表
//ex1.1
前面的不重要
core：print("yes,sir...".format(str1,str2))
1.2//九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}=={:2}".format(i,j,i*j),end=' ')
print(' ')

1.8
turtle模块的先不管了
"""
diet=['van','billy','魔男','bananajun','darkholme']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{} and {} r a philosophy match".format(diet[x],diet[y]))

