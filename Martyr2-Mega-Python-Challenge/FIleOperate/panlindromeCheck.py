s=''
s=input("please input a str,then we check if it's a panlindrome")
#method 1 list列表判断
listA=list(s)
listB=list(s[::-1])
print(listA,"",listB)
print("result:",listA==listB)
#method 2 string判断
reverseStr=s[::-1]
print("result:",s==reverseStr)
#method 3 循环判断，时间复杂度低一些
counter,flag=0,True
print("length is:",len(s))
while counter<len(s)/2:
    if flag==True:
        if(s[counter]==s[len(s)-1-counter]):
            pass
        else:
            flag=False
            break
    counter+=1

if flag==True:
    print("result is TRUE")
else:
    print("result is FALSE")