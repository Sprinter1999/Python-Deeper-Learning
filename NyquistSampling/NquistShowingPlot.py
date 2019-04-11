import numpy as np
import matplotlib.pyplot as plt 
import time
#from scipy.optimize import curve_fit
#from scipy import interpolate
#plt.figure(figsize=(10, 8))


f = np.append(np.arange(5,11,5),np.arange(12,42,5))
t = np.arange(0,2,0.005)
y = np.sin(2*np.pi*10*t+0.3)
t1 = np.arange(0,2,0.1) 
#print(type(t1))
le = []
st = []
for fi in f:
    plt.figure(figsize=(12,8))
    #plt.subplot(212)
    plt.plot(t,y)
    #plt.title("")

    yi = np.sin(2*np.pi*fi*t1+0.3)
    #print(type(yi))
    #plt.subplot(212)
    title="Original Signal Freq=10Hz,Sampling Freq="+(str)(fi)+"Hz"
    plt.title(title)

    plt.xlabel("X")
    plt.ylabel("Y")
    time.sleep(0.5)
    hd, = plt.plot(t1,yi,linewidth=1)
 
    le.append(hd)
    st.append(str(fi)+"hz")
    plt.show()
    plt.close()
#plt.legend(handles = le,labels = st)
plt.ylim(-1,1)
#plt.show()
