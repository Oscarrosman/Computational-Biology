import numpy as np
import matplotlib.pyplot as plt

alpha = [0.01, 0.1, 0.2, 0.5, 1, 2]
uFunction1 = lambda a, u: a + (u**2)/(1+u**2)
uFunction2 = lambda u: u/2

x = np.linspace(-10, 10, 1000)
y2 = uFunction2(x)
y1 = []
for a in alpha:
    y1.append(uFunction1(a, x))

plt.plot(x, y2, label='F2', linewidth=2, color='black')
for i, a in enumerate(alpha):
    plt.plot(x, y1[i], label=f'F1: alpha = {a}')

#plt.hlines(alpha+1, 0, 10, linestyles='--', color='black', label='alpha+1')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend()
plt.show()