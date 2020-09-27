print(9//10)
print(10//10)
print(0//10)

a=[1,1]
b=2

c=a
print(c)
a=2
print(c)

import numpy as np
import matplotlib.pyplot as plt


plt.ion()
plt.figure(1)
x=0
x_list=[]
y_list=[]
while 1:
    if x>10:
        plt.clf()
        exit()
    else:
        y=np.sin(x)
        x_list.append(x)
        y_list.append(y)
        plt.plot(x_list, y_list, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
        x+=1
        plt.pause(0.1)
        plt.show()
