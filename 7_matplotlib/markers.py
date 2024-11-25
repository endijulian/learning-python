import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o')
# plt.plot(ypoints, marker = '*')
# plt.plot(ypoints, marker = 'x')
# plt.plot(ypoints, marker = '_')
# plt.plot(ypoints, 'o:r')
# plt.plot(ypoints, 'o--')

# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')

plt.show()