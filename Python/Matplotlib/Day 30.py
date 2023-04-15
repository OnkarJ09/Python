import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from turtle import color, title



x = np.random.normal(198, 160, 103)

#print(x)
plt.hist(x)
plt.show()


water = np.array([44.5, 14.5, 14.4, 6.3, 7.6, 5, 5.2, 2.5])
mylabels = np.array(["Residential(Single-Family)", "Residential(Multi-Family)", "Commertial/Industrial", "Resorts", "Golf Courses", "Schools/Government/Parks", "Common Area's", "Others"])
myexplode = np.array([0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1])

plt.pie(water, labels = mylabels, startangle = 270, explode = myexplode, shadow=True)
plt.legend()
plt.title("Water Distribution on Earth")
plt.show()

#Completed with Matplotlib
