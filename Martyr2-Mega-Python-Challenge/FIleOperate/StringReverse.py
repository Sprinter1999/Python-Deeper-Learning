'''
文本操作第一题：
'''
s,result1='',''
s=input("Please input a string,then output its reverse: ")
result1=s[::-1]
print("first method:",result1)

list_string=list(s)
list_string.reverse()
print("second method interval,此时仍然是列表",list_string)
result2="".join(list_string)
'''
Python中字符串的join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串 【列表】【字符串】
'''
print("second method:",result2)

# third method: 模拟一个栈
stack=''
stack=list(stack)
print("方法三模拟一个栈，入栈")
counter=0
for each in s:
    counter+=1
    print(counter,end='')
    stack.append(each)
print("current stack:",stack)
print("弹栈")
count=0
result3=''
#for each in stack:
while(len(stack)>0):
    count+=1
    print(count,end='')
    result3+=stack.pop(-1)
    print("current stack",stack)
print("last stack",stack)
print("third method:",result3)