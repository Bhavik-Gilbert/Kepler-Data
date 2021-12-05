import numpy as np
import matplotlib.pyplot as plt
z,x,y = np.loadtxt("D:\Stuff\School\A Levels\Planet Hunting\QMUL Project - Exoplanet Hunting With Python 2019\PlanetHuntingWithPython2019\DATA/KIC010418224.tbl", unpack = True, skiprows = 3)
period = 6.8732
for n in range(0,len(x)):
        x[n] = x[n] - 138.147

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0,50*period , period)
ax.set_xticks(major_ticks)
plt.grid()


ax.plot(x,y,"bo",markersize=1)
plt.show()
