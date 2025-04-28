import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6), facecolor='lightgrey')

x1 = np.linspace(-12, 12, 400)
y1 = -(1/18) * x1**2 + 12
plt.plot(x1, y1, label='y=-(1/18)x**2+12', color='blue')

x2 = np.linspace(-4, 4, 400)
y2 = -(1/8) * x2**2 + 6
plt.plot(x2, y2, label='y=-(1/8)x**2+6', color='orange')

x3 = np.linspace(-12, -4, 400)
y3 = -(1/8) * (x3 + 8)**2 + 6
plt.plot(x3, y3, label='y=-(1/8)(x+8)**2+6', color='cyan')

x4 = np.linspace(4, 12, 400)
y4 = -(1/8) * (x4 - 8)**2 + 6
plt.plot(x4, y4, label='y=-(1/8)(x-8)**2+6', color='red')


x5 = np.linspace(-4, -0.3, 400)
y5 = 2 * (x5 + 3)**2 - 9
plt.plot(x5, y5, label='y=2(x+3)**2-9', color='purple')

x6 = np.linspace(-4, 0.2, 400)
y6 = 1.5 * (x6 + 3)**2 - 10
plt.plot(x6, y6, label='y=1.5(x+3)**2-10', color='darkblue')

plt.title('Zontik')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.show()