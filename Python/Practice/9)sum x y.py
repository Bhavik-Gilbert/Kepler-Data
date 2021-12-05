import numpy as np
x,y = np.loadtxt("C:/Users/Owner/Documents/School/A Levels/Planet Hunting/QMUL Project - Exoplanet Hunting With Python 2019/PlanetHuntingWithPython2019/DATA/xy.txt", unpack = True)
length = len(x)
n=0
valuex = 0
valuey = 0
while n < length:
    valuex = valuex + x[n]
    valuey = valuey + y[n]
    n=n+1
print(valuex,valuey)
