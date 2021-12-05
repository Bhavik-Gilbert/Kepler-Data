import numpy as np
import matplotlib.pyplot as plt
y = np.loadtxt("Data/Test-C.txt", unpack = True, skiprows = 3)
for n in range(0,len(y)):
    y[n] = y[n] /100
plt.plot(y,"bo",markersize=1)
plt.show()

