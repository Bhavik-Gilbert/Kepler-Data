import numpy as np
import matplotlib.pyplot as plt
z,x,y = np.loadtxt("../DATA/KIC007950644.tbl", unpack = True, skiprows = 3)
period = 10.291
count = 0
add = 0
hold = 0
extra = 0

for n in range(0,len(x)):
    x[n] = x[n] - 137.03
    if y[n] < -0.008:
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


    
