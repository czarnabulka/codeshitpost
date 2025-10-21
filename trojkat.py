import matplotlib.pyplot as plt
import random as rnd

x = [0]
y = [0]

for i in range (1, 1000000):
    los = rnd.random()
    if los < 0.3333:
        x.append(0.5 * x[i - 1] - 0.5)
        y.append(0.5 * y[i - 1] + 0.5)
    if los < 0.6666:
        x.append(0.5 * x[i - 1] - 0.5)
        y.append(0.5 * y[i - 1] - 0.5)
    else:
        x.append(0.5 * x[i - 1] + 0.5)
        y.append(0.5 * y[i - 1] - 0.5)

plt.plot(x,y , ".", markersize = 0.02, color = 'blue')
plt.savefig("trojkat.png")
plt.show()