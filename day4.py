# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:04:16 2019

@author: 21543
"""

"""
x1,y1=input("输入第一个点的横、纵坐标值:").split()这样只是将字符串分片
or
>>> x1,y1=eval(input())需保证xy的间隔不是一个无意义字符，比如space，返回一个数值
55,11
>>> x1
55
>>> y1
11

bmi1,bmi2=eval(input("please input you two's bmi value:"))
#must seperate bmi1 and bmi2 with a signal instead of "space"
who,dom="",""
if bmi1<18 and bmi2<18:
    who,dom="thin","thin"
elif 18<=bmi1<=24 and 18<=bmi2<=24:
    who,dom="healhty","healthy"
elif 24<=bmi1 and 24<=bmi2:
    who,dom="fat","fat"
    ...#codes above is just a test
    
string="yes sir,mr.van"
for p in string:
    print("now turns to:"+p)
else:
    print("done in here")    
    
string,index="van darkholme",0
while index < len(string):
    print(string[index])
    index+=1
else:
    print("we r done")    
    
continue,break一样的

random module:
    seed(a=None) 初始化随机种子，默认值为系统当前时间
    random() 产生一个0—~1zuobiyoukai的随即小数
    randint(a,b)
    getrandits(k)产生k 比特长度的随机整数
    randrange(start,stop,step)
    uniform(a,b)产生随即小数
    choice(序列，比如range（10）)
    shuffle（序列）返回打乱后的序列
    sample（pop，k）取样，用到的时候再说吧
    
然后是python的异常处理
关键字：try:, except NameError:（to name a few）,else,except:,finally:
"""
#here’s Monte Carlo Algorithm to solve pi
from random import random
from time import clock
Darts =100000
hits=0
#clock()
for i in range(0,Darts+1):
    x,y=random(),random()
    distance=x**2 +y**2
    if distance <=1.0:
        hits+=1
pai=4*hits/Darts
print("Run time is {:5.5}".format(clock()/1000))
print("The simulated pi is {:.5f}".format(pai))


