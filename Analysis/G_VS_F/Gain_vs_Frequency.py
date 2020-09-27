import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter


lambda1 = 2*np.pi*0.48e9
# kappa1 = 2*np.pi*500e6
omega_d = 2*np.pi*6.45e9
Ic0 = 2.6e-6 # unit A
phi_0 = 2.068e-15 # unit wb
C_p = 3.4e-12 # unit F
R = 50 # unit Ohm
Z4 = 40 # unit Ohm
Z2 = 140 # unit Ohm
Z_aux = (np.pi/4)*(Z4*(1-(Z4**2)/(R**2))+2*Z2*(1-(Z4**2)/(R**2*Z2**2)))
omega_aux = 2*np.pi*6.45e9
alphi = 2*Z_aux/omega_aux

phi = 0.0*phi_0

Ic = Ic0*np.abs(np.cos(np.pi*phi/phi_0))
L_p = phi_0/(2*np.pi*Ic)
Z_p = np.sqrt(L_p/C_p)
omega_p = np.sqrt(1/(L_p*C_p))
wd = omega_p - omega_d - 2*lambda1

f=np.linspace(-1e9,1e9,2001)
w=2*np.pi*f
# w=0

delta = (1/(2*alphi*C_p))*(w/(w**2 + (R**2/alphi**2)))
kappa = (R/(alphi**2*C_p))*(1/(w**2 + R**2/alphi**2))

w_dash = w - delta
kappa_p = kappa + 2*np.sqrt(lambda1**2-wd**2)
kappa_m = kappa - 2*np.sqrt(lambda1**2-wd**2)
x11 = (-1j*(w+wd-delta)+kappa/2)/((-1j*w_dash+kappa_m/2)*(-1j*w_dash+kappa_p/2))
gain = np.abs(1 - kappa*x11)**2
plt.figure(1)

ax1=plt.subplot(111)
plt.plot(w/(2*np.pi), 10*np.log10(gain))

xmajLocator=MultipleLocator(0.2e9)
ymajLocator=MultipleLocator(1)
ax1.xaxis.set_major_locator(xmajLocator)
ax1.yaxis.set_major_locator(ymajLocator)


# xminLocator=


# plt.locator_params('y',nbins=15)
plt.show()
omega_p = omega_p/(2*np.pi)

