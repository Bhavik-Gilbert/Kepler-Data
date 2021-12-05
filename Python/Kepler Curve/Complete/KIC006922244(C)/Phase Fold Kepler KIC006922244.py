import numpy as np
import matplotlib.pyplot as plt
z,x,y = np.loadtxt("D:\Stuff\School\A Levels\Planet Hunting\QMUL Project - Exoplanet Hunting With Python 2019\PlanetHuntingWithPython2019\DATA/KIC006922244.tbl", unpack = True, skiprows = 3)
period = 3.52254
count = 0
add = 0
hold = 0
extra = 0

for n in range(0,len(x)):
    x[n] = x[n] - 131.679
    if y[n] < -0.0009:
        if (x[n] > hold+(period/2)):
            count = count + 1
            add = x[n] + add - hold
            hold = x[n]
        elif (x[n] < x[n-1]+1) and (x[n] > x[n-1]-1):
            pp=1+1
            extra = extra + 1
            if y[n] < y[n-1]:
                add = x[n] + add - x[n-1]
                hold = x[n]
        else:
            extra = extra + 1
    x[n] =  x[n] + (0.5*period)
    x[n] = x[n] % period
    x[n] = x[n] - (0.5*period)

print("")
print(count)
print(add)
if count == 0:
    count = 1
print(add/count)

print("")
print(pp)
print(extra)
plt.plot(x,y,"bo",markersize=1)
plt.show()
