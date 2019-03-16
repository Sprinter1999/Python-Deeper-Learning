import winsound
import time
import os
import re

'''
    @帮电子院小姐姐写的一个电子钢琴实验
    @Scripted by Xuefen
'''

def function(instruction):

    if instruction=='1':
        A=input('起始频率\n')
        A=int(A)
        C=int((2000-A)/100)
        for j in range(0,C+1):
            winsound.Beep(A+100*j,500)
            time.sleep(0.5)
    elif instruction=='2':
        print("键盘上1~7表示低音1~7，q~u表示中音1~7，a~j、z~m亦然")
        str=input("输入音谱，发出基准为0.5s的节拍,如1 2 3 4 5 6 7 q w e")
        str=str.split(" ")
        #没有必要非要按老师的那个/，用空格就好啦，你们文档里面写的例如就是举个例子的意思
        for i in range(len(str)):
            if str[i]=='1':
                winsound.Beep(131,500)#这里131是频率，500代表0.5s
            elif str[i]=='2':
                winsound.Beep(147,500)
            elif str[i]=='3':
                winsound.Beep(165,500)
            elif str[i]=='4':
                winsound.Beep(175,500)
            elif str[i]=='5':
                winsound.Beep(196,500)
            elif str[i]=='6':
                winsound.Beep(220,500)
            elif str[i]=='7':
                winsound.Beep(247,500)
            elif str[i]=='q':
                winsound.Beep(262,500)
            elif str[i]=='w':
                winsound.Beep(296,500)
            elif str[i]=='e':
                winsound.Beep(330,500)
            elif str[i]=='r':
                winsound.Beep(349,500)
            elif str[i]=='t':
                winsound.Beep(392,500)
            elif str[i]=='y':
                winsound.Beep(440,500)
            elif str[i]=='u':
                winsound.Beep(494,500)
            elif str[i]=='a':
                winsound.Beep(523,500)
            elif str[i]=='s':
                winsound.Beep(587,500)
            elif str[i]=='d':
                winsound.Beep(659,500)
            elif str[i]=='f':
                winsound.Beep(698,500)
            elif str[i]=='g':
                winsound.Beep(784,500)
            elif str[i]=='h':
                winsound.Beep(880,500)
            elif str[i]=='j':
                winsound.Beep(988,500)
            elif str[i]=='z':
                winsound.Beep(1047,500)
            elif str[i]=='x':
                winsound.Beep(1175,500)
            elif str[i]=='c':
                winsound.Beep(1319,500)
            elif str[i]=='v':
                winsound.Beep(1397,500)
            elif str[i]=='b':
                winsound.Beep(1568,500)
            elif str[i]=='n':
                winsound.Beep(1760,500)
            elif str[i]=='m':
                winsound.Beep(1976,500)

    elif instruction=='3':
        print("进入节拍弹琴模式，音调有ABCDEFG七个音调，1~4四个音高")
        sequen=input("请按照节拍+音调+音高格式输入，比如1A1 2b2 3.5c2 5d3格式").split()
        #print(sequen)
        for sub in sequen:
            substring=''
            substring=sub
            isMatch1=re.search(r"\d+\.?\d*",substring)#剥离出前面的节拍
            if isMatch1:
                tempo=eval(isMatch1.group(0))#剥离出节拍，并将他转化为数字
                substring=substring[len(isMatch1.group(0)):]#前面的甩掉不要，继续分析后面的
            isMatch2=re.search(r'\w',substring)
            if isMatch2:
                tune=isMatch2.group(0) #代表哪个音调,ABCDEFG七个音调
                substring=substring[len(isMatch2.group(0)):]#再甩一部分，只留下最后的音高
            highness=pow(2,eval(substring)-1)#将音高转化为数字1 2 4 8---1 2 3 4
            
            ConvertTempo=int(tempo*1000)#1000表示计算机内部一个时间参数指标，用C语言就是CLOCK_PER_SEC
            #print(ConvertTempo)

            if (tune=='a' or 'A'):
                winsound.Beep(131*highness,ConvertTempo)#注意到其实这张音调表是有大概的1：2：4：8的关系的
            elif(tune=='b'or'B'):
                winsound.Beep(147*highness,ConvertTempo)#第一个参数表示频率，第二个参数表示持续节拍
            elif(tune=='c'or'C'):
                winsound.Beep(165*highness,ConvertTempo)#这个系统函数只能接收整数参数，所以应该提前*1000
            elif(tune=='d'or'D'):
                winsound.Beep(175*highness,ConvertTempo)
            elif(tune=='e'or'E'):
                winsound.Beep(196*highness,ConvertTempo)
            elif(tune=='f'or'F'):
                winsound.Beep(220*highness,ConvertTempo)
            elif(tune=='G'or'g'):
                winsound.Beep(247*highness,ConvertTempo)

            




while(1):
    instruction=input("请选择，\"1\"表示递进音节,\"2\"表示基准弹琴,\"3\"表示节拍弹琴,\"0\"表示停止:")
    if(instruction=='0'):
        exit()
    function(instruction)   



