import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

x = []
y = []

for i in range(n):
    xv = float(input(f"Enter X value {i+1}: "))
    yv = float(input(f"Enter Y value {i+1}: "))
    x.append(xv)
    y.append(yv)

plt.plot(x, y, marker='o')

plt.xlabel("X values (Independent Variable)")
plt.ylabel("Y values (Dependent Variable)")
plt.title("X-Y Axis Data Plot")

plt.grid(True)

plt.show()