import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# x = np.array([1, 2, 3, 4, 5, 6])
# plt.plot(x, marker='o')
# plt.show()


# x = np.array([1, 2, 3, 4, 5, 6])
# plt.plot(x, marker='o')
# plt.show()
# x = np.array([1, 2, 3, 4, 5, 6])
# x2 = np.array([12, 13 ,74, 80, 123, 126])
# plt.plot(x, ls = "--")
# plt.plot(x2, ls = "-.")
# plt.show()

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y, marker='o')

plt.title("My First Plot")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.show()


