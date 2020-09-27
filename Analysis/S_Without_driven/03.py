import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter


Ic0 = 2.6e-6 # unit A
phi_0 = 2.068e-15 # unit wb
C_p = 7.5e-12 # unit F
# L_g = 0.3e-9 # unit H
R = 50 # unit Ohm
# R1 = 0.0001 #unit Ohm, corresponding to the R0 expression in line 136. The
# reflection amplitude should be 1 if R1 is strictly equal to 1. 
Z4 = 39 # unit Ohm
Z2 = 57 # unit Ohm
omega_aux = 2*np.pi*6.82e9
phi=np.linspace(-1.5*phi_0,1.5*phi_0,301)
w=np.linspace( 2*np.pi*4e9,2*np.pi*8e9,4001)

Ret = np.zeros((len(phi), len(w)))
Gamma_dash=np.zeros((len(phi), len(w)))

for i in range(len(phi)):
    Ic = Ic0*abs(np.cos(np.pi*phi[i]/phi_0))
    L_p = phi_0/(2*np.pi*Ic)
#     L_p = L_p*L_g/(L_p+L_g)
#     R0 = 1/(1/(1i*w*L_p)+1i*w*C_p+R1)
    R0 = (1j*L_p*w)/(1-L_p*C_p*w**2)
    Z2_1 = Z2*(R0+1j*Z2*np.tan(np.pi*(w/omega_aux)))/(Z2+1j*R0*np.tan(np.pi*w/omega_aux))
    Zin = Z4*(Z2_1+1j*Z4*np.tan((np.pi/2)*w/omega_aux))/(Z4+1j*Z2_1*np.tan((np.pi/2)*w/omega_aux))
    Gamma = (Zin-R)/(Zin+R)
    Ret[i:] = abs(Gamma)**2
    Gamma_dash[i, :] = (np.arctan2(Gamma.imag, Gamma.real))
Ret=Ret.T
Gamma_dash=Gamma_dash.T

plt.figure(1)
plt.pcolormesh(phi/phi_0, w/(2*np.pi*1e9), 20*np.log10(Ret),cmap='hsv')
# plt.colormaps('hsv')
# mesh(phi/phi_0, w/(2*np.pi*1e9), (Ret'))
# view(0, 90)

# plt.gca('FontSize',20)
plt.xlim(-1.5,1.5)
plt.ylim(4,8)
plt.xlabel('Flux (Phi_0)')
plt.ylabel('Probe Frequency (GHz)')

plt.figure(3)
plt.pcolormesh(phi/phi_0, w/(2*np.pi*1e9), Gamma_dash,cmap='hsv')
# plt.colormaps('hsv')
# view(0, 90)
# plt.gca('FontSize',20)
plt.xlim(-1.5,1.5)
plt.ylim(4,8)
plt.xlabel('Flux (Phi_0)')
plt.ylabel('Probe Frequency (GHz)')

# Ic = Ic0*abs(np.cos(np.pi*phi(151)/phi_0))
# L_p = phi_0/(2*np.pi*Ic)
# L_p = L_p*L_g/(L_p+L_g)
# f_p = np.sqrt(1/(L_p*C_p))/(2*np.pi)

plt.show()