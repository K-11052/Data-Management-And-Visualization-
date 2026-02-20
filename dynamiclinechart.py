import matplotlib.pyplot as plt
import random


plt.ion()

x = []
y = []

plt.figure()

for i in range(10):
    x.append(i)
    y.append(random.randint(1, 50))

    plt.clf() 
    plt.plot(x, y)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Dynamic Line Chart")

    plt.pause(1)  
plt.ioff()
plt.show()
