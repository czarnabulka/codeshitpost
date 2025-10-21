import matplotlib.pyplot as plt 
import random

x = [0]
y = [0]

for i in range (1, 1000000):
    los = random.random()
    if los < 0.142:
        x.append(0.05 * x[i - 1] - 0.06)
        y.append(0.4 * y[i - 1] - 0.47)
    elif los < 0.284:
        x.append(-0.05 * x[i - 1] - 0.06)
        y.append(-0.4 * y[i - 1] - 0.47)
    elif los < 0.426:
        x.append(0.03 * x[i - 1] - 0.14 * y[i - 1] - 0.16)
        y.append(0.26 * y[i - 1] - 0.01)
    elif los < 0.568:
        x.append(-0.03 * x[i - 1] + 0.14 * y[i - 1] - 0.16)
        y.append(-0.26 * y[i - 1] - 0.01)
    elif los < 0.710:
        x.append(0.56 * x[i - 1] + 0.44 * y[i - 1] + 0.3)
        y.append(-0.37 * x[i - 1] + 0.51 * y[i -1] + 0.15)
    elif los < 0.852:
        x.append(0.19 * x[i - 1] + 0.07 * y[i - 1] - 0.2)
        y.append(-0.1 * x[i - 1] + 0.15 * y[i - 1] + 0.28)
    else:
        x.append(-0.33 * x[i - 1] - 0.34 * y[i - 1] - 0.54)
        y.append(-0.33 * x[i - 1] + 0.34 * y[i - 1] + 0.39)


plt.plot(x,y,'.',markersize=0.2,color='brown')
plt.savefig("drzewo.png")
plt.show()