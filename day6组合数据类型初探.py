# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:17:30 2019

@author: 21543
"""
'''
Python中组合数据类型分为三类序列、集合、映射
序列类型是一个元素向量通过序号访问，比如str，tuple，list
集合类型是一个元素集合，无序，具有不重复性，即set
映射类型是一个键值对组合体，即map字典

#序列类型：一维元素向量，具有成员关系操作符in、len（），分片【】操作，有索引体系
x in s
x not in s
s+t catenation
s*n
s[i]
s[i:j]
s[i:j:k]
len(s)
min(s)
max(s)
s.count(x)
s.index(x,i,j)
#元组tuple特殊在一旦创建就不允许修改一般我们这么创建：（）
creature=("ren","dog","mao")
color=("red","white","jade",creature)#creature is another tuple
print(color[-1])
元组使用的情况很少，主要是三个途径使用
1.函数有多个返回值，返回值形式就是元组
def func(x):
    return x,x**3
2.多个变量同步赋值是隐式元组形式
3.循环遍历的时候，比如遍历数对、向量的时候，如下：
import math
for x,y in ((1,3),(2,4),(3,4)):
    print(math.hypot(x,y))

集合类型的元素只能是确定的，比如整数浮点数字符串元组，不能是字典，列表，
集合这种可变数据类型，可以进行哈希运算的元素都可以作为集合元素
我们一般用{}表征一个集合，比如：
group=set("apple")---内含aple四个元素,set()用于生成一个集合
S={342,342，3543，231，"billy","boy next door",("van","dark","holme")}
集合类型有如下的关系操作符号：
S-T 差集 or S.difference(T)
S-=T S.difference_update(T)更新S集合，后面同理
S&T S.intersection(T)
S&=T
S^T S.Symmetric_difference(T)对称差
S<=T S.issubset(T)S是否是T的子集
S>=T S.issuperset(T)
S.disjoint(T)是否不交
如下的个体操作：
S.add(x)
S.clear()“析构”
S.copy()
S.pop()随机pop一个
S.discard(x)若不存在不报错
S.remove(x)若不存在则报错
len(S)
x in S
x not in S
有如下的三种情形，在前面的oj我也提到过，应该在数据结构与算法的repo
里面那个奇数次单词oj就是用的集合结构解题：
1.成员关系测试 返回x in {"shajdhak",...} True or false
2.元素去重，比如将一个元组tup用set(tup)方式去重
3.删去数据项，比如：newtup=tuple(set(tup)-{"Python"})
映射类型：主要是dict类型，后面再说
列表类型用的也比较多，我们后面再说，今天先到这里为止

'''
