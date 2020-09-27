import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter



omega_d = 2*np.pi*6.82e9
Ic0 = 2.6e-6 # unit A
phi_0 = 2.068e-15
C_p = 7.5e-12
R = 50 # unit Ohm
Z4 = 39 # unit Ohm
Z2 = 57 # unit Ohm
Z_aux = (np.pi/4)*(Z4*(1-Z4**2/R**2)+2*Z2*(1-Z4**2/(R**2*Z2**2)))
omega_aux = 2*np.pi*6.82e9
alphi = 2*Z_aux/omega_aux
# alphi = 2*np.pi*omega_d

phi=np.linspace(-1.5*phi_0,1.5*phi_0,1001)

Ic = Ic0*abs(np.cos(np.pi*phi/phi_0))
L_p = phi_0/(2*np.pi*Ic)
omega_p = np.sqrt(1/(L_p*C_p))
wd = omega_p - omega_d
omega1 = (wd/2 + np.sqrt((wd+1j*R/alphi)**2 + 2/(alphi*C_p))/2 - 1j*R/(2*alphi)).real/(2*np.pi)
omega2 = (wd/2 - np.sqrt((wd+1j*R/alphi)**2 + 2/(alphi*C_p))/2 - 1j*R/(2*alphi)).real/(2*np.pi)
# a1 = imag(wd/2 + np.sqrt((wd+1i*R/alphi)**2 + 2/(alphi*C_p))/2 - 1i*R/(2*alphi))
# a2 = imag(wd/2 - np.sqrt((wd+1i*R/alphi)**2 + 2/(alphi*C_p))/2 - 1i*R/(2*alphi))

plt.figure(1)
# plot(phi/phi_0, omega1, 'r', phi/phi_0, omega2, 'b')
plt.plot(phi/phi_0, omega1+6.82e9, 'r', phi/phi_0, omega2+6.82e9)
# omega_p(151)/(2*np.pi)
# f_p = omega_p/(2*np.pi)
# figure(2)
# plot(phi/phi_0, a1, '. r', phi/phi_0, a2, '. b')

plt.show()