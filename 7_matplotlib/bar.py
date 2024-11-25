import matplotlib.pyplot as plt
import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# x = ["APPLES", "BANANAS"]
# y = [400, 350]

# plt.bar(x, y)
# plt.show()


### Horizontal Bars ###

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y)
# plt.show()


### Bar Color ###

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# # plt.bar(x, y, color = "red")
# # plt.bar(x, y, color = "hotpink")
# plt.bar(x, y, color = "#4CAF50")
# plt.show()


### Bar Width ###

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# plt.bar(x,y, width=0.1)
plt.barh(x,y, height=0.1)  #for horizontal
plt.show()