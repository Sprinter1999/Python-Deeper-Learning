# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 13:10:22 2019
Matplotlib其实就很像mathematica
@author: 21543
"""

'''
modify inner setting
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']


import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.plot([1,2,4], [1,2,3])
plt.title("坐标系标题")
plt.xlabel('时间 (s)')
plt.ylabel('范围 (m)')
plt.xticks([1,2,3,4,5],[r'$\pi/3$', r'$2\pi/3$', r'$\pi$',\
                   r'$4\pi/3$', r'$5\pi/3$'])
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
y = np.cos(2*np.pi*x) * np.exp(-x)+0.8
plt.plot(x,y,'k',color='r',label="$exp-decay$",linewidth=3)
plt.axis([0,6,0,1.8])
ix = (x>0.8) & (x<3)
plt.fill_between(x, y ,0, where = ix, 
                         facecolor='grey', alpha=0.25)
plt.text(0.5*(0.8+3), 0.2, r"$\int_a^b f(x)\mathrm{d}x$",
                horizontalalignment='center')
plt.legend()
plt.show()

##eg   PlotDamping.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
def Draw(pcolor, nt_point, nt_text, nt_size):
    plt.plot(x, y, 'k', label="$exp_decay$", color=pcolor, linewidth=3, linestyle="-")
    plt.plot(x, z, "b--", label="$cos(x^2)$", linewidth=1)
    plt.xlabel('时间(s)')
    plt.ylabel('幅度(mV)')
    plt.title("阻尼衰减曲线绘制")
    plt.annotate('$\cos(2 \pi t) \exp(-t)$', xy=nt_point, xytext=nt_text, fontsize=nt_size,\
               arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.1"))
def Shadow(a, b):
    ix = (x>a) & (x<b)
    plt.fill_between(x,y,0,where=ix,facecolor='grey', alpha=0.25)
    plt.text(0.5 * (a + b), 0.2, "$\int_a^b f(x)\mathrm{d}x$", \
             horizontalalignment='center')
def XY_Axis(x_start, x_end, y_start, y_end):
    plt.xlim(x_start, x_end)
    plt.ylim(y_start, y_end)
    plt.xticks([np.pi/3, 2 * np.pi/3, 1 * np.pi, 4 * np.pi/3, 5 * np.pi/3], \
               ['$\pi/3$', '$2\pi/3$', '$\pi$', '$4\pi/3$', '$5\pi/3$'])
x = np.linspace(0.0, 6.0, 100)
y = np.cos(2 * np.pi * x) * np.exp(-x)+0.8
z = 0.5 * np.cos(x ** 2)+0.8
note_point,note_text,note_size = (1, np.cos(2 * np.pi) * np.exp(-1)+0.8),(1, 1.4), 14
fig = plt.figure(figsize=(8, 6), facecolor="white")
plt.subplot(111)
Draw("red", note_point, note_text, note_size)
XY_Axis(0, 5, 0, 1.8)
Shadow(0.8, 3)
plt.legend()
plt.savefig('sample.JPG')
plt.show()

#eg  DrawHollandRadar
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
radar_labels = np.array(['研究型(I)','艺术型(A)','社会型(S)','企业型(E)','常规型(C)','现实型(R)'])
nAttr = 6
data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                 [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                 [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                 [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                 [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                 [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]]) #数据值
data_labels = ('工程师', '实验员', '艺术家', '推销员', '社会工作者','记事员')
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
#plt.plot(angles,data,'bo-',color ='gray',linewidth=1,alpha=0.2)
plt.plot(angles,data,'o-', linewidth=1.5, alpha=0.2)
plt.fill(angles,data, alpha=0.25)
plt.thetagrids(angles*180/np.pi, radar_labels,frac = 1.2)
plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='small')
plt.grid(True)
plt.show()

#eg DrawRadar
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
labels = np.array(['综合', 'KDA', '发育', '推进', '生存','输出'])
nAttr = 6
data = np.array([7, 5, 6, 9, 8, 7]) #数据值
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles,data,'bo-',color ='g',linewidth=2)
plt.fill(angles,data,facecolor='g',alpha=0.25)
plt.thetagrids(angles*180/np.pi, labels)
plt.figtext(0.52, 0.95, 'DOTA能力值雷达图', ha='center')
plt.grid(True)
plt.show()
'''









