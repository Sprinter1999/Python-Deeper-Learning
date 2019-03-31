#如果你需要遍历一个数字序列，可以是使用python中内建的函数range()

#如下面要遍历一个列表test_list
test_list = [1,3,4,'Hongten',3,6,23,'hello',2]
for i in range(len(test_list)):
    print(test_list[i],end=',')
    print()#表示换行

for i in range(5):
    print(i,end=',')#0 1 2 3 4,生成从0开始的n个数

print('range(10)表示：',range(10),'And...')
listA = [i for i in range(10)]
print(listA)

#当然，我们可以自定义我们需要的起始点和结束点
#我们定义了一个从5开始的起始点，到100结束的结束点
print('range(5,100)表示：',range(5,100))
listB = [i for i in range(5,100)]
print(listB)

#定义了这些后，我们还可以定义步长
#下面我们定义一个从1开始到30结束，步长为3的列表
print('range(1,30,3)表示：',range(1,30,3))
listC = [i for i in range(1,30,3)]
print(listC)

'''
菜鸟教程：
>>>range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)     # 从 1 开始到 11
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)  # 步长为 5
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)  # 步长为 3
[0, 3, 6, 9]
>>> range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]

>>>x = 'runoob'
>>> for i in range(len(x)) :
...     print(x[i])
... 
r
u
n
o
o
b
>>>
'''

aTuple=('python','is','on','the''way')
print("输出元组：",aTuple)
print("输出列表：",list(aTuple))
'''
输出元组： ('python', 'is', 'on', 'theway')
输出列表： ['python', 'is', 'on', 'theway']
元组中只包含一个元素时，需要在元素后面添加逗号,如tup1 = (50,)
list、元组与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
'''