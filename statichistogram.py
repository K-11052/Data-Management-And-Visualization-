import matplotlib.pyplot as plt


data = [10, 12, 15, 18, 20, 22, 25, 25, 28, 30, 30, 32, 35, 38, 40]


plt.hist(data, bins=5)


plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Static Histogram")


plt.show()
