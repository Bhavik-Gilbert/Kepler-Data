import numpy as np
import matplotlib.pyplot as plt
z,x,y = np.loadtxt(" DATA/KIC002571238.tbl", unpack = True, skiprows = 3)
period = 9.2873
for n in range(0,len(x)):
    x[n] = x[n] - 135.988

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0,5000*period , period)
ax.set_xticks(major_ticks)
plt.grid()


ax.plot(x,y,"bo",markersize=1)
plt.show()
