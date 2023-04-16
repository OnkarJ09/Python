import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.array([99,86,87,88,86,103,87,94,78,77,85,86,111,67])
y = np.mean(x)
#print(x)
print(y)

z = np.median(x)
print(z)

a = stats.mode(x, keepdims=True)
print(a)

b = np.std(x)
print(b)

c = np.var(x)
print(c)

ages = np.array([5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31])

#x = np.percentile(ages, 75)
x = np.percentile(ages, 99.999)
print(x)





d = np.random.uniform(0.0, 67.0, 10000000)
#print(d)
plt.hist(d, 100)
#plt.show()


e = np.random.normal(5.0, 1.0, 1000000)
print(e)
plt.hist(e, 100)
plt.show()
