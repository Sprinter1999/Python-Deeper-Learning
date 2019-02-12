# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:14:26 2019
Today is for Numpy and part I for numpy in CV
@author: xuefen
"""
'''
import numpy as np
#there r many ways to create numpy arryays
a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

a = np.zeros((2,2))   # Create an array of all zeros,用empty也行
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"
b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"
c = np.full((2,2), 7)  # Create a constant array填充数组
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"
d = np.eye(2)         # Create a 2x2 identity matrix 创建二维单位矩阵
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"
e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"
Still,there r other ways,eg:
    arange(x,y,i)
    linspace(x,y,n)
    indices((m,n))
    总之，所有和创建m×n的数组，都要（（））这种format
    *********************************************************
    ndarray类总有一个基本属性表：
    ndim：数组轴的个数
    shape、size元素总个数、dtype、itemsize、data(包含实际数组元素的缓冲区地址)、
    flat（ndarray elemet iteratior）
    *****************************************************
    ndarray类的形态操作方法：
    reshape(n,m)不改变数组，只是返回一个n*m的数组
    resize(new_shape)直接修改数组，作用同上
    swapaxes（ax1，ax2）交换维度
    flatten（）同下，降维为一个折叠的一维数组
    ravel（）
    ravel（）返回的是视图，意味着改变元素的值会影响原始数组；
    flatten（）返回的是拷贝，意味着改变元素的值不会影响原始数组。
    也可以加参数：参数：{‘C’，‘F’，‘A’，‘K’}默认情况下‘C’以行为主的顺序展开，
    ‘F’（Fortran风格）意味着以列的顺序展开，‘A’表示如果a在内存中为Fortran连续，
    则按列展开，否则以行展开，‘K’按照元素在内存中出现的顺序展平a
    *******************************************************
    Array Indexing
    import numpy as np
# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"

import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Prints "[[ 2]
                             #          [ 6]
                             #          [10]] (3, 1)"
************************************************************
Numpy的基本算术运算库函数：
add(x1,x2[,y]) y=x1+x2
np.substract...multiply...divide...flooor_divide....negative...power.remainder
eg:
    >>> x = np.arange(5)
>>> np.true_divide(x, 4)
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
>>> x/4
array([0, 0, 0, 0, 1])
>>> x//4
array([0, 0, 0, 0, 1])

Basic compute eg：
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))
点乘用dot实现，而这种基本算术都是元素之间的算术
Note that unlike MATLAB, * is elementwise multiplication, 
not matrix multiplication. We instead use the dot function to compute inner
 products of vectors, to multiply a vector by a matrix, and to multiply
 matrices. dot is available both as a function in the numpy module and as 
 an instance method of array objects:
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))

其他例子：
import numpy as np

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

转置示例：
import numpy as np

x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"
**********************************************************
Numpy的比较运算与其他运算库函数：
equal（x1，x2[,y])
not_equal,less,less_equal,greater,greater_equal or
np.where(condition[x,y])根据条件判断输出x or y
eg:
    x=1,2  and y=2,2
    np.less(x,y)
    >>>array([true,false],dtype=bool)
    
abs(x),sqrt,squre,sign,ceil,floor,rint(x[,out])取最近的整数,exp,log,log10,log2
********************************************************
#GrayTransformation example
from PIL import Image
import numpy as np
im=np.array(Image.open("astro.jpg").convert('L'))
print(im.shape,im.dtype) #output=(1803, 1275, 3) uint8
#PIL库包含图像转化函数，可以改变单个像素的表示形式，
#比如用convert('L'),就可以把它转化由三通道色彩转化为单一数值表示，即灰度
#Formula:Gray=0.3R+0.59G+0.11B
#这时我们将图片转化为数组了，可以用py数组处理了，比如找出这个阵列的im.min()
#然后我们可以进行灰度变换
im1=255-im #inverse transform
im2=(100/255)*im+150#scale transform
im3=255*(im1/255)**2 #pixel square process
pil_im=Image.fromarray(np.uint(im2)) #有些变换可能会改变数据类型
pil_im.show()
********************************************************
#手绘滤镜
#e17.1HandDrawPic.py
from PIL import Image
import numpy as np
vec_el = np.pi/2.2 # 光源的俯视角度，弧度值
vec_az = np.pi/4. # 光源的方位角度，弧度值
depth = 10. # (0-100)
im = Image.open('astro.jpg').convert('L')
a = np.asarray(im).astype('float')
grad = np.gradient(a) #取图像灰度的梯度值
grad_x, grad_y = grad #分别取横纵图像梯度值
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
dx = np.cos(vec_el)*np.cos(vec_az) #光源对x 轴的影响
dy = np.cos(vec_el)*np.sin(vec_az) #光源对y 轴的影响
dz = np.sin(vec_el) #光源对z 轴的影响
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
a2 = 255*(dx*uni_x + dy*uni_y + dz*uni_z) #光源归一化
a2 = a2.clip(0,255)
im2 = Image.fromarray(a2.astype('uint8')) #重构图像
im2.save('astroHandDraw.jpg')
思想：用像素之间的梯度重构每个像素，为体现光照效果设计一个光源，建立光源
对于各个点的梯度值的影响函数，进而计算出新的像素值，从而体现强化后的梯度变化
实现手绘效果

'''













