# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:13:53 2019

@author: 21543
"""

'''
Python打开文件的方式是：
textfile = open("5.txt","rt") t means text-type file,rt is the default pattern
print(textfile.readline())
textfile.close()

binfile=open("6.txt","rb")
print(binfile.readline())
binfile.close()

选项有r w a b etc
读写方法：
readall() read(size=-1) readline(...) readlines(hint..)
eg:
    fname = input("请输入要打开的文件: ")
fo = open(fname, "r")
for line in fo.readlines():
    print(line)
fo.close()
但是文件过大了就占内存不少，所以也可以这么：
fname=input()
fo=open(fname,"r")
for line in fo:
    print(line)
fo.close()
逐行处理
写入方法：
write(string)
writelines(lines)
seek(offset) offset denotes file-operate location 0 is beginning 1 is present
location and 2 is the final location in this file
eg:
fname = input("请输入要写入的文件: ")
fo = open(fname, "w+")
ls = ["唐诗", "宋词", "元曲"]
fo.writelines(ls)
fo.seek(0)#think about this saying's meanning
for line in fo:
    print(line)
fo.close()

Then let's see PIL library

from PIL import Image
im=Image.open("D:\\pycodes\\birds.jpg")
#but using relative file path is commended

Image类包含了五个图像读取和创建方法，2个序列图像（gif...etc)操作方法
    3个图像转化和保存方法（save、convert、thumbnail缩略图），
    resize、rotate，还有像素和rgb颜色通道处理方法，比如：#exchange-color
#GIF
 from PIL import Image
im = Image.open('pybit.gif')      # 读入一个GIF文件
try:
    im.save('picframe{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save('picframe{:02d}.png'.format(im.tell()))
except:
    print("处理结束")

#exchange-color
from PIL import Image
im = Image.open('birdnest.jpg')
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save('birdnestBGR.jpg')

#轮廓处理
from PIL import Image
from PIL import ImageFilter
im = Image.open('birdnest.jpg')
om = im.filter(ImageFilter.CONTOUR)
om.save('birdnestContour.jpg')

#字符画方法：
from PIL import Image
ascii_char = list('"$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-/+@<>i!;:,\^`.')
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256 / len(ascii_char)
    return ascii_char[int(gray//unit)]
def main():
    im = Image.open('astro.jpg')
    WIDTH, HEIGHT = 100, 60
    im = im.resize((WIDTH, HEIGHT))
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    fo = open("pic_char.txt","w")
    fo.write(txt)
    fo.close()
main()

#python的所有数据类型转化函数
1	int(x [,base])	将x转换为decimal型整数。
如果x是字符串，则要base指定基数。base是来形容这个x是什么进制的。
2	float(x)	将x转换为浮点数。
3	complex(real [,imag])	创建一个复数。
4	str(x)	将对象x转换为字符串表示形式。
5	repr(x)	将对象x转换为表达式字符串。
6	eval(str)	评估求值一个字符串并返回一个对象。
7	tuple(s)	将s转换为元组。
8	list(s)	将s转换为列表。
9	set(s)	将s转换为集合。
10	dict(d)	创建一个字典，d必须是(key，value)元组的序列
11	frozenset(s)	将s转换为冻结集
12	chr(x)	将整数x转换为字符
13	unichr(x)	将整数x转换为Unicode字符。
14	ord(x)	将单个字符x转换为其整数值。
15	hex(x)	将整数x转换为十六进制字符串。
16	oct(x)	将整数x转换为八进制字符串。





'''
#e12.1DrawCharImage

