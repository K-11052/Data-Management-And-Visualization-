import numpy as np
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = np.array([25, 15, 40, 20]) 

percentages = values / np.sum(values) * 100

plt.figure(figsize=(6,6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['skyblue','orange','green','red'])
plt.title('Static Pie Chart ')
plt.axis('equal') 

plt.show()
