import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

def s(phi):
	return (2/3+4*np.exp(phi/2)/(np.exp(phi/2)-1)**2)**(-1)

phi = np.arange(0.001, 20, 0.01)

r = s(phi)
#r = chi(phi)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(phi, r, color = 'blue')

ax.set_rmax(2)  
ax.set_rlabel_position(-22.5)  
ax.grid(True)


plt.show()