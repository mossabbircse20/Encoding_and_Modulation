#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     09-12-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#unipolar
data=input()
data1=[int(i) for i in data]
#x,y asix
Time=np.arange(len(data1)+1)
signal=np.zeros(len(data1)+1,dtype=int)

for i in range(len(data1)):
    if data1[i]==0:
        signal[i]=0
    else:
        signal[i]=1
#plotting
plt.subplot(3,2,1)
plt.title("Unipolar encoding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.step(Time,signal,where="post")
plt.xticks(Time)
plt.yticks([-3,-2,-1,0,1,2,3])
plt.grid(True)
plt.text(2,2,data)

#NRZ_L

data1=[int(i) for i in data]
Time=np.arange(len(data1)+1)
signal=np.zeros(len(data1)+1,dtype=int)

for i in range(len(data1)):
    if data1[i]==0:
        signal[i]=1
    else:
        signal[i]=-1

#plotting
plt.subplot(3,2,2)
plt.title("NRZ_L Encoding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.step(Time,signal,where="post")
plt.text(2,2,data)
plt.xticks(Time)
plt.yticks([-3,-2,-1,0,1,2,3])
plt.grid(True)

#NRZ_I

data1=[int(i) for i in data]
signal=[1]
bit=1
for i in range(len(data1)):
    if data1[i]==1:
        if bit==1:
            bit=-1
        else:
            bit=1
    signal.append(bit)

Time=np.arange(len(signal))

#plotting
plt.subplot(3,2,3)
plt.title("NRZ_I Encoding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.step(Time,signal,where="post")
plt.text(2,2,data)
plt.xticks(Time)
plt.yticks([-3,-2,-1,0,1,2,3])
plt.grid(True)

#RZ

Time=np.arange(0,len(data),0.5)
signal=np.array([])

for i in range(len(data)):
    if data[i]=='1':
        signal=np.append(signal,[1,0])
    else:
        signal=np.append(signal,[-1,0])
#plotting
plt.subplot(3,2,4)
plt.title("RZ Encoding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.text(2,2,data)
plt.step(Time,signal,where="post")
plt.xticks(np.arange(0,len(data)))
plt.yticks([-3,-2,-1,0,1,2,3])
plt.grid(True)

#Manchester

Time=np.arange(0,len(data),0.5)
signal=np.array([])

for i in range (len(data)):
    if data[i]=='1':
        signal=np.append(signal,[-1,1])
    else:
        signal=np.append(signal,[1,-1])
#plotting
plt.subplot(3,2,5)
plt.title("Manchester Encoding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.step(Time,signal,where="post")
plt.text(2,2,data)
plt.xticks(np.arange(0,len(data)))
plt.yticks([-3,-2,-1,0,1,2,3])
plt.grid(True)

#Differential manchester

Time=np.arange(0,len(data),0.5)
signal=np.array([])

temp=1
for i in range(len(data)):
    if data[i]=='1':
        signal=np.append(signal,[temp,temp*-1])
        temp=temp*-1
    else:
        signal=np.append(signal,[temp*-1,temp])
#plotting
plt.subplot(3,2,6)
plt.title("Differential Manchester Encoding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.step(Time,signal)
plt.text(2,2,data)
plt.xticks(np.arange(0,len(data)))
plt.yticks([-3,-2,-1,0,1,2,3])
plt.grid(True)

plt.tight_layout()
plt.show()