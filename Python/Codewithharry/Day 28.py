#Revised Sets

from turtle import color
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


#x = np.array([8, 2, 324,24, 54, 25, 25, 68])
#y = np.array([5, 6, 467,45, 56, 78, 35, 47])
#plt.plot(x, y, marker = 'o')

#plt.title("My 1st PyGraph")
#plt.xlabel("hiii")
#plt.ylabel("byyyy")
##plt.grid(axis='both')
#plt.grid(color = 'red', linestyle = ':', linewidth = 0.5)
#plt.show()



#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("hello")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])


plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("hi")

plt.suptitle("My Graph")
plt.show()
