from turtle import speed
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

#x = np.random.normal(5.0, 1.0, 1000)
#y = np.random.normal(10.0, 2.0, 1000)
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.xlabel("ages")
plt.ylabel("speeds")
plt.show()

print(r)
speed = myfunc(10)
print(speed)