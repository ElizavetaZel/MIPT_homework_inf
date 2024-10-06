import numpy as np
import matplotlib.pyplot as plt
import math
amount = [15, 21, 23, 19, 20]
labels = ["кусок 1", "кусок 2", "кусок 3", "кусок 4", "кусок 5"]

colors = plt.cm.viridis(np.linspace(0, 1, len(amount)))

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(amount, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90)

for i, wedge in enumerate(wedges):
    wedge.set_edgecolor('purple')
    wedge.set_alpha(0.7)

plt.title("Пирог")
plt.pie(amount, labels=labels, colors='pink', autopct='%1.f%%')

plt.show()