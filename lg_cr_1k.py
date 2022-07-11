import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

def s(phi):
	return abs((-1/3+np.tanh(phi/2)**2)**(-1))

phi = np.arange(0.9, 20, 0.01)

r = s(phi)
#r = chi(phi)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(phi, r, color = 'blue')

ax.set_rmax(5)  
ax.set_rlabel_position(-22.5)  
ax.grid(True)


plt.show()