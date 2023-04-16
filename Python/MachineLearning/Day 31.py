import numpy as np
from scipy import stats

x = np.array([99,86,87,88,86,103,87,94,78,77,85,86,111,67])
y = np.mean(x)
#print(x)
print(y)

z = np.median(x)
print(z)

a = stats.mode(x, keepdims=True)
print(a)