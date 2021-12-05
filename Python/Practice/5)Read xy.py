import numpy as np
x,y = np.loadtxt("C:/Users/Owner/Documents/School/A Levels/Planet Hunting/QMUL Project - Exoplanet Hunting With Python 2019/PlanetHuntingWithPython2019/DATA/xy.txt", unpack = True)
length = (len(x))
n=0
while n<length:
    print(x[n],y[n])
    n=n+1
