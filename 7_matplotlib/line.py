import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linestyle = 'dotted')
# plt.plot(ypoints, linestyle = 'dashed')
# plt.plot(ypoints, color = 'r')
# plt.plot(ypoints, c = '#4CAF50')
# plt.plot(ypoints, linewidth = '20.5')
# plt.show()


# Multiple Lines
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)
# plt.show()


x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()