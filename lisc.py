import matplotlib.pyplot as plt
import random as rnd
 
x =[0]
y = [0]
 
for i in range (1, 1000000):
    los = rnd.random()
    if los < 0.01:
        x.append(0)
        y.append(0.16 * y[i - 1])
    elif los < 0.86:
        x.append(0.85 * x[i - 1] + 0.04 * y[i - 1])
        y.append(-0.04 * x[i - 1] + 0.85 * y[i - 1] + 1.6)
    elif los < 0.93:
        x.append(0.2 * x[i - 1] - 0.26 * y[i - 1])
        y.append(0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6)
    else:
        x.append(-0.15 * x[i - 1] + 0.28 * y[i - 1])
        y.append(0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44)
plt.plot(x, y, '.', markersize = 0.05, color = 'green')
plt.xlim(-3, 3)
plt.ylim(0, 10)
plt.savefig("paproc.png")
plt.show()