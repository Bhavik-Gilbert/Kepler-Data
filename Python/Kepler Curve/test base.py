import numpy as np
import matplotlib.pyplot as plt
import time
z,x1,y = np.loadtxt("DATA/filename", unpack = True, skiprows = 3)
x=np.empty(len(x1))
period = "get period"
while period < 8.8:
    z,x,y = np.loadtxt("DATA/filename", unpack = True, skiprows = 3)
    for n in range(0,len(x)):
         x[n] = x[n] - 134.0258 +(0.5*period)
         x[n] = x[n] %  (period)
         x[n] = x[n] - (0.5*period)
    plt.plot(x,y,"bo",markersize=1)
    plt.show()
    plt.close()
    print(period)
    period=period+0.00001




    
