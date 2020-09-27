from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math


# x=symbols('x')
# y=symbols('y')
x,y,omega=symbols('x y omega')


fx=1+7*x**2-4*x*((1+3*x**2)**(0.5))
fx1=diff(fx,x)
print(fx1)
# -12.0*x**2*(3*x**2 + 1)**(-0.5) + 14*x - 4*(3*x**2 + 1)**0.5
print(solve(fx1, x))
# [1.00000000000000, 1.15470053837925*I]



plt.figure()

R=50
Cj=3.4e-12
κ0=(Cj*R)**-1

# x=np.linspace(0,0.9,1001)
x=0.88
ß_equ=1+(7*x**2)-4*x*((1+3*x**2)**0.5)

Gmax=1+1/(3*ß_equ)
# plt.plot(x,Gmax)


# ΓBW=0.5*κ0*(Gmax**-0.25)
ΓBW=κ0*(Gmax**-0.25)

f=np.linspace(-1e9,1e9,1001)
omega=2*np.pi*f
G_omega=Gmax*(1+(omega/ΓBW)**4)**-1
G=10*np.log10(G_omega)


# plt.plot(x,Gmax)
# plt.xlabel('β')
# plt.ylabel('Gmax')

# plt.plot(ΓBW,Gmax)
# plt.xlabel('ΓBW')
# plt.ylabel('Gmax')

plt.plot(f,G)
plt.xlabel('omega/2π (detuning)')
plt.ylabel('Gain (dB)')

plt.show()
