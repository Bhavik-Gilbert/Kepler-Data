import numpy as np
import matplotlib.pyplot as plt
z,x,y = np.loadtxt("DATA/KIC002571238.tbl", unpack = True, skiprows = 3)
print(z,x,y)
plt.plot(x,y,"bo",markersize=1)
plt.show()

