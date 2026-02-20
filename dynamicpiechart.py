import numpy as np
import matplotlib.pyplot as plt
import time

categories = ['A', 'B', 'C', 'D']
n = len(categories)

values = np.array([25, 15, 40, 20])


plt.ion()
fig, ax = plt.subplots(figsize=(6,6))

patches, texts, autotexts = ax.pie(
    values,
    labels=categories,
    autopct='%1.1f%%',
    startangle=90,
    colors=['skyblue','orange','green','red']
)
ax.set_title('Dynamic Pie Chart ')

for _ in range(20): 
   
    values = values + np.random.randint(-5, 6, size=n)
    values = np.clip(values, 0, None)  
    
    ax.clear()
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90,
           colors=['skyblue','orange','green','red'])
    ax.set_title('Dynamic Pie Chart ')
    
    plt.pause(1)  

plt.ioff()
plt.show()
