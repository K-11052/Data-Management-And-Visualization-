import numpy as np
import matplotlib.pyplot as plt
import time
n_points = 50

x = np.random.rand(n_points) * 10
y = np.random.rand(n_points) * 10

plt.ion() 
fig, ax = plt.subplots(figsize=(8,6))
scat = ax.scatter(x, y, color='blue', s=50, alpha=0.7, edgecolors='black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Dynamic Scatter Plot ')
ax.grid(True)

for _ in range(50):  
    x += np.random.uniform(-0.5, 0.5, n_points)
    y += np.random.uniform(-0.5, 0.5, n_points)
    
    x = np.clip(x, 0, 10)
    y = np.clip(y, 0, 10)
    
    scat.set_offsets(np.c_[x, y])
    
    plt.pause(0.1) 

plt.ioff()
plt.show()
