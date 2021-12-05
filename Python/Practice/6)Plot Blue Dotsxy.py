import numpy as np
import matplotlib.pyplot as plt
x,y = np.loadtxt("C:/Users/Owner/Documents/School/A Levels/Planet Hunting/QMUL Project - Exoplanet Hunting With Python 2019/PlanetHuntingWithPython2019/DATA/xy.txt", unpack = True)
plt.plot(x,y,"bo")
plt.show()
