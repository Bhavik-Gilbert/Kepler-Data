import numpy as np
import matplotlib.pyplot as plt
z,x,y = np.loadtxt("../DATA/KIC007950644.tbl", unpack = True, skiprows = 3)
period = 10.291
for n in range(0,len(x)):
    x[n] = x[n] - 137.03
    
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0,50*period , period)
ax.set_xticks(major_ticks)
plt.grid()


ax.plot(x,y,"bo",markersize=1)
plt.show()
