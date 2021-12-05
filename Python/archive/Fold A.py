import numpy as np
import matplotlib.pyplot as plt
y = np.loadtxt("Data/Test-A.txt", unpack = True, skiprows = 1)
period = 515
while period <550:
    for n in range(0,len(y)):
        y[n] = y[n] - 135.988 +(0.5*period)
        y[n] = y[n] %  (period)
        y[n] = y[n] - (0.5*period)
    plt.plot(y,"bo",markersize=1)
    print(period)
    plt.show()
    period = period + 0.1


