import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

k =(np.sqrt(5)+1)/(2*np.sqrt(5))
def chi(r):
	return np.arccos(8/(np.sqrt(5)+1)*(-1/r+1/2)-1)
def s(r):
	return 2*np.sqrt(2/np.sqrt(5))*(sp.ellipk(k)-sp.ellipkinc(chi(r)/2, k))

r = np.arange(2, 30, 0.01)

phi = s(r)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(phi, r, color = 'blue')
ax.plot(-phi, r, color = 'blue')
ax.set_rmax(20)  
ax.set_rlabel_position(-22.5) 
ax.grid(True)

plt.show()