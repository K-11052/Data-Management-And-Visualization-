import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-0.1*x) * np.sin(2*x)
y4 = np.log1p(x) 

fig, axs = plt.subplots(2, 2, figsize=(10,8))

axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title('y = sin(x)')
axs[0, 0].grid(True)

axs[0, 1].plot(x, y2, color='green')
axs[0, 1].set_title('y = cos(x)')
axs[0, 1].grid(True)

axs[1, 0].plot(x, y3, color='red')
axs[1, 0].set_title('y = exp(-0.1x) * sin(2x)')
axs[1, 0].grid(True)

axs[1, 1].plot(x, y4, color='orange')
axs[1, 1].set_title('y = log(1+x)')
axs[1, 1].grid(True)

plt.tight_layout()
plt.suptitle('Static Subplots ', fontsize=16, y=1.02)

plt.show()
