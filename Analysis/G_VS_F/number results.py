import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter


lambda1 = 2*np.pi*0.83e9
omega_d = 2*np.pi*6.82e9
Ic0 = 2.6e-6 # unit A
phi_0 = 2.068e-15 # unit wb
C_p = 3e-12 # unit F
R = 50 # unit Ohm
# Z4 = 39 # unit Ohm
Z2 = 57 # unit Ohm
omega_aux = 2*np.pi*6.82e9
phi = 0.0*phi_0
Ic = Ic0*np.abs(np.cos(np.pi*phi/phi_0))
print(Ic)
L_p = phi_0/(2*np.pi*Ic)
Z_p = np.sqrt(L_p/C_p)
omega_p = np.sqrt(1/(L_p*C_p))
wd = omega_p - omega_d - 2*lambda1

f=np.linspace(-1e9,1e9,2001)
w=2*np.pi*f
gain=np.zeros(2001)


for Z4 in range(38,41):
    Z4_1 = Z4*(R+1j*Z4*np.tan((np.pi/2)*(1+w/omega_aux)))/(Z4+1j*R*np.tan((np.pi/2)*(1+w/omega_aux)))
    Zin = Z2*(Z4_1+1j*Z2*np.tan(np.pi*(1+w/omega_aux)))/(Z2+1j*Z4_1*np.tan(np.pi*(1+w/omega_aux)))
    epsilon = -1j/(2*C_p*np.conj(Zin))

    for i in range(len(w)):
        xi_dash = -1j*np.array([[w[i]-wd-epsilon[i],1j*lambda1],[1j*lambda1,w[i]+wd-epsilon[i]]])
        xi = np.linalg.inv(xi_dash)
        gain[i]=np.abs(1+2*(epsilon[i]).imag*xi[1, 1])**2

    plt.figure(1)
# plot(w/(2*np.pi), 10*log10(gain))
    plt.plot(f, 10*np.log10(gain))

    omega_p/(2*np.pi)


# L = legend('$Z_{\lambda/4}=38$ Ohm', '$Z_{\lambda/4}=39$ Ohm', '$Z_{\lambda/4}=40$ Ohm')
# set(L, 'Interpreter', 'latex')
# figure(2)
# plot(w/(2*np.pi), imag(Zin))

plt.legend(['Z4=38 ohm','Z4=39 ohm','Z4=40 ohm'])
plt.show()