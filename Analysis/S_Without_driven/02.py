# 这一部分存在问题



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter



# omega_d = 2*np.pi*7.45e9
Ic0 = 2.8e-6 # unit A
phi_0 = 2.068e-15
C_p = 3e-12
R = 50 # unit Ohm
Z4 = 38 # unit Ohm
Z2 = 56 # unit Ohm
Z_aux = (np.pi/4)*(Z4*(1-(Z4**2)/(R**2))+2*Z2*(1-(Z4**2)/(R**2*Z2**2)))
omega_aux = 2*np.pi*6.45e9
# alphi = 2*Z_aux/omega_aux
# alphi = 2*np.pi*omega_d

phi_num=101
omega_d_num=8


phi=np.linspace(-1.5*phi_0,1.5*phi_0,phi_num)
omega_d=np.linspace(2*np.pi*4.5e9,2*np.pi*8e9,omega_d_num)

Ic = Ic0*abs(np.cos(np.pi*phi/phi_0))
L_p = phi_0/(2*np.pi*Ic)
omega_p = np.sqrt(1/(L_p*C_p))
LineSpec = ['r', 'g', 'b', 'c', 'm', 'y', 'k', '.']

omega1=np.zeros((omega_d_num,phi_num))
omega2=np.zeros((omega_d_num,phi_num))


for i in range(len(omega_d)):
    wd = omega_p - omega_d[i]
    alphi = 2*Z_aux/omega_d[i]
    omega1[i] = (wd/2 + np.sqrt((wd+1j*R/alphi)**2 + 2/(alphi*C_p))/2 - 1j*R/(2*alphi)).real/(2*np.pi)
    omega2[i] = (wd/2 - np.sqrt((wd+1j*R/alphi)**2 + 2/(alphi*C_p))/2 - 1j*R/(2*alphi)).real/(2*np.pi)
    # fig,ax=plt.subplots()
    plt.plot(phi/phi_0, omega1[i], LineSpec[i%8])
    plt.plot(phi/phi_0, omega2[i], LineSpec[i%8])
#     xlim([-1.0 1.0])
#     ylim([-2e9 2e9])
    plt.ylim(-2e9,2e9)

# a1 = imag(wd/2 + np.sqrt((wd+1j*R/alphi)**2 + 2/(alphi*C_p))/2 - 1j*R/(2*alphi))
# a2 = imag(wd/2 - sqrt((wd+1j*R/alphi)**2 + 2/(alphi*C_p))/2 - 1j*R/(2*alphi))

# figure(1)
# LineSpec = ['r', 'g', 'b']
# plot(phi/phi_0, omega1(1, :), LineSpec(1), phi/phi_0, omega2(1, :), LineSpec(1))
# f_p = omega_p/(2*np.pi)
# figure(2)
# plot(phi/phi_0, a1, '. r', phi/phi_0, a2, '. b')


plt.show()