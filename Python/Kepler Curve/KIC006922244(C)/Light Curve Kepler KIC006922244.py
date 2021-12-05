import numpy as np
import matplotlib.pyplot as plt
z,x,y = np.loadtxt("../DATA/KIC006922244.tbl", unpack = True, skiprows = 3)
plt.plot(x,y,"bo",markersize=1)
plt.show()

