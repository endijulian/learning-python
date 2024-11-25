import matplotlib.pyplot as plt
import numpy as np

# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.show()

### Labels ###
# y = np.array([35, 25, 25, 15])
# mylables = ["Apples", "Bananas", "Cheries", "Dates"]

# plt.pie(y, labels=mylables)
# plt.show()


### Start Angle ###
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels=mylabels, startangle=90)
# plt.show()


### Explode and Shadow###
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# myexplode = [0.2, 0, 0, 0]

# # plt.pie(y, labels=mylabels, explode=myexplode)
# plt.pie(y, labels=mylabels, explode=myexplode, shadow= True)
# plt.show()


### Colors ###


# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# mycolors = ["black", "hotpink", "b", "#4CAF50"]

# plt.pie(y, labels= mycolors, colors=mycolors)
# plt.show()


### Legend ###
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
# plt.legend()
plt.legend(title = "Four Fruits:")
plt.show()