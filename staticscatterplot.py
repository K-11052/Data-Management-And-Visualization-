import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0) 
x = np.random.rand(50) * 10 
y = np.random.rand(50) * 20 

plt.figure(figsize=(8,6))
plt.scatter(x, y, color='blue', marker='o', s=50, alpha=0.7, edgecolors='black')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Static Scatter Plot ')

plt.grid(True)

plt.show()
