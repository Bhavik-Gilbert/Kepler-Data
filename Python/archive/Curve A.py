import numpy as np
import matplotlib.pyplot as plt
y = np.loadtxt("Data/Test-A.txt", unpack = True, skiprows = 3)
for n in range(0,len(y)):
    y[n] = y[n]
plt.plot(y,"bo",markersize=1)
plt.show()

