import numpy as np
import matplotlib.pyplot as plt
import math

t = np.linspace(-10, 10, 1000)
x = np.cos(t)
y = np.sin(t) + abs(np.cos(t))**0.5

plt.plot(x, y, color = 'red', marker='*', markersize=1)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
ax = plt.gca()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2)

plt.arrow(min(x)- 0.5, 0, max(x) - min(x) + 0.8, 0, head_width=0.1, head_length=0.2, fc='r', ec='k')
plt.arrow(0, min(y)- 0.5, 0, max(y) - min(y) + 0.6, head_width=0.05, head_length=0.3, fc='r', ec='k')
plt.gca().set_facecolor('lightpink')

plt.title('График')
plt.grid(True, which='both', linewidth=0.7, color = 'purple')
plt.show()