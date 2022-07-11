import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

D = np.sqrt(5)
k=(D+2)/(2*D)
def csi(x):
    return 2*np.arctan(x**(-1)-1)
def psi(x):
	return np.arcsin(np.sqrt((D-np.sin(csi(x))-2*np.cos(csi(x)))/(D+2)))
def psi_ot(x):
	return np.arcsin(-np.sqrt((D-np.sin(csi(x))-2*np.cos(csi(x)))/(D+2)))
def s(r):
	return (1/np.sqrt(D)*(sp.ellipk(k)-sp.ellipkinc(psi(r),k)))
def s_ot(r):
	return (1/np.sqrt(D)*(sp.ellipk(k)-sp.ellipkinc(psi_ot(r),k)))

r = np.arange(0.001, 0.81, 0.01)
r_ot = np.arange(0.81, 30, 0.01)

phi = s(r)
phi_ot=s_ot(r_ot)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(phi, r, color ='blue')
ax.plot(phi_ot, r_ot, color ='blue')
ax.set_rmax(5)
 
ax.set_rlabel_position(-22.5) 
ax.grid(True)


plt.show()
