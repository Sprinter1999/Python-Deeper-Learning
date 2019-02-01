# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:26:17 2019

@author: 21543
"""

#day2
"""
注释段：
day2样例函数：
tempstr=input("输入带符号的温度")
if tempstr[-1] in ['f','F']:
    C=(eval(tempstr[0:-1])-32)/1.8
    print("转化后的温度为{:.2f}C".format(C))
elif tempstr[-1] in ['C','c']:
    F=(eval(tempstr[0:-1]))*1.8+32
    print("转化后的温度为{:.2f}F".format(F))
else:
    print("Error input\n")
    
    
python中处理字符串[N:M]前闭后开，若为负数表示倒数第几个，正数还是从0开始
赋值方式
单步赋值；
同步赋值：x，y=2，3
input函数返回字符串
eval函数，自动解析转化为值
考虑向eval函数喂入如下数据
1.temp="102c"--->eval(temp[0:-1])得到102;
2.eval("hello")->解析为符号hello，能否有值取决于之前是否定义过这个符号
3.eval("'hello'")->解析为字符串'hello'
4.eval("1.1+2.2")-->3.3
自定义函数：
先定义说明，后使用，比如
def tempconvert(ValueStr)
    if ValueStr[-1] in ['M','m']:
        c=eval(tempconvert)
        print("the result is{:.2f}".format(c))
    else:
        print("Error\n")

TempStr=input("输入待处理的字符串：")
tempconvert(TempStr)

from turtle import *,*为通配符

from turtle import *
setup(600,350,200,200) 
#分别是width,height,startx,starty参数，前两者若为整数，
#说明是像素值，若为小数则说明宽度和高度与屏幕的比例，后两者决定
#这个窗口放在距离屏幕左边、上面的距离，正中间的话设置None
penup()
#penup(简称pu)表示抬起画笔，不绘出形状；pendown(pd)表示绘出形状
fd(-250)
#fd即forward，表示前进的距离
pendown()
pensize(25)
#表示画笔宽度，别名叫width()
pencolor("purple")
#"purple","red",or((R,G,B))比如白色就是255，255，255，因为白色的RGB值为#FFFFFF
seth(-40)
#全名为setheading，表示改变方向，方向的描述和极坐标描述一样，里面为度数
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
#circle(radius,extent=None),radius为正数表示画圈圆心在turtle左，负数表示在右
fd(40)
circle(16,180)
fd(40*2/3)

"""




