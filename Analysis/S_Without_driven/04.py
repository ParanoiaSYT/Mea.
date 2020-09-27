import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter



Ic0 = 2.8e-6 # unit A
phi_0 = 2.068e-15 # unit wb
C_p = 5.5e-12 # unit F
L_g = 0.3e-9 # unit H
phi=np.linspace(-1.5*phi_0,1.5*phi_0,201)

Ic = Ic0*abs(np.cos(np.pi*phi/phi_0))
L_p = phi_0/(2*np.pi*Ic)
L_a = L_p*L_g/(L_p+L_g)
f_p = np.sqrt(1/(L_a*C_p))/(2*np.pi)
plt.figure(2)
plt.plot(phi/phi_0, f_p/(1e9))
plt.show()