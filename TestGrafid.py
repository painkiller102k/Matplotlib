import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0, 10, 1)
y=x**2-5*x+6
plt.figure(facecolor='green')
plt.title("Joonise pealkiri")
plt.xlabel("X telg")
plt.ylabel("Y telg")
plt.grid(True)
plt.plot(x, y, color='blue', linestyle='-', marker='D', markersize='8', linewidth='2', label='Joonise json')
plt.show()