import numpy as np
import matplotlib.pyplot as plt
import time
z,x1,y = np.loadtxt("D:\Stuff\School\A Levels\Planet Hunting\QMUL Project - Exoplanet Hunting With Python 2019\PlanetHuntingWithPython2019\DATA/KIC008359498.tbl", unpack = True, skiprows = 3)
x=np.empty(len(x1))
period = 3.5784
while period < 8.8:
    z,x,y = np.loadtxt("D:\Stuff\School\A Levels\Planet Hunting\QMUL Project - Exoplanet Hunting With Python 2019\PlanetHuntingWithPython2019\DATA/KIC008359498.tbl", unpack = True, skiprows = 3)
    for n in range(0,len(x)):
         x[n] = x[n] - 134.0258 +(0.5*period)
         x[n] = x[n] %  (period)
         x[n] = x[n] - (0.5*period)
    plt.plot(x,y,"bo",markersize=1)
    plt.show()
    plt.close()
    print(period)
    period=period+0.00001




    
