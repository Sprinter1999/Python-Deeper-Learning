# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:56:26 2019

@author: 21543
"""
'''
#字符串反转设计：
def reverse(s):
    if s=="":
        return s
    else:
        return reverse(s[1:])+s[0]

str=input()
print(str[::-1],end="")#索引方法
print(reverse(str))#递归函数

'''
#e8.2DrawKoch.py：分形几何❄雪花绘制
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1)
def main():
    turtle.setup(600,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 5
    koch(400,level) 
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()


