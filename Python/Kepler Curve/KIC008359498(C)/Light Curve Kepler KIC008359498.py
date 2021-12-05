import numpy as np
import matplotlib.pyplot as plt
z,x,y = np.loadtxt("../DATA/KIC008359498.tbl", unpack = True, skiprows = 3)
plt.plot(x,y,"bo",markersize=1)
plt.show()

