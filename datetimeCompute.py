import datetime
import re
#import numpy
str2=''#表征含有你所说的x，y，z的值
a=datetime.datetime#startTime
str2=(str)(datetime.datetime.now())#这个now是你的第二个参数transTime
match = re.search(r'\d{1,2}:\d{1,2}:\d{1,2}',str2)
pattern=''
if(match):
    pattern=match.group(0)
lis=[]
lis=re.split(r':',pattern)
Hour=(int)(lis[0])
Min=(int)(lis[1])
#Sec=(int)(lis[2])
a=(a+datetime.timedelta(minutes=Hour*60+Min)).strftime('%Y-%m-%d %H:%M')