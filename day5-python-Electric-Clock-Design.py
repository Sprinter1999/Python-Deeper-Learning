# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 22:42:01 2019

@author: 21543
"""
"""
#lambda函数
f=lambda x,y:x+y
x=type(f)
print(x)
g=f(10,23)
print (g)

#可变数量参数加*号
def vfunc(a,*b):
    print(type(b))
    for n in b:
        a += n
    return a
print(vfunc(1,2,3,4,4,5))
参数调用的时候，顺序可以任意给出，但是必须一一匹配，如func(x2=1，x1=3)
函数返回的时候，可以有多个返回值，以元组形式保存
5.2.4节暂时跳过，学完组合数据类型再回过来看

from datetime import datetime
#today =datetime.now()
print("{}".format(datetime.now()))
print(datetime.now())
print(datetime.utcnow())
someday=datetime(2016,3,5,23,4,5,8)
#someday.min,max,year,month,day,hour...
#someday.isoformat,isoweekday,strftime("%Y-%m-%d %H:%M:%S")
"""
#e7.2DrawSevenSegDisplay.py绘制七段时间译码器
import turtle, datetime
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()    
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)#单行if-else
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) 
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40) 
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.hideturtle()
main()    
#另外，计算机的计时功能是利用主板的一个纽扣电池给硬件时钟供电，依靠硬件计时电路实现





