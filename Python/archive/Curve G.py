import numpy as np
import matplotlib.pyplot as plt
y = np.loadtxt("Data/Test-G.txt", unpack = True, skiprows = 1)
plt.plot(y,"bo",markersize=1)
plt.show()

