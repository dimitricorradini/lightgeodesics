import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp



k =(np.sqrt(5)+1)/(2*np.sqrt(5))
def chi(phi):
	return 2*sp.ellipj(np.sqrt(np.sqrt(5)/2)*phi/2,k)[3]
def s(phi):
	return (1/2+((np.sqrt(5)-1)/(2*np.sqrt(5))*1/(np.cos(chi(phi)/2)**2)))**-1

phi = np.arange(0.001, 4, 0.01)

r = s(phi)
#r = chi(phi)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(phi, r, color = 'blue')

ax.set_rmax(1.5)  
ax.set_rlabel_position(-22.5)  
ax.grid(True)


plt.show()