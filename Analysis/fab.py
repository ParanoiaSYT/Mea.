import numpy as np


# 设定电容
C_p = 2.5e-12 #unit pF
# 常温junction电阻
Rn=100 #unit ohm
# Al的带隙
delta=0.182e-3
# 临界电流
Ic=(np.pi*delta)/(2*Rn)
print(Ic)
# 计算电感
phi_0 = 2.068e-15 # unit wb
L_p = phi_0/(2*np.pi*Ic)


# JPA频率f
omega=((L_p*C_p)**(-0.5))/1e9
f=omega/(2*np.pi)
print(f)

# 电容所需长度Length
Length=C_p/(0.68423e-12)
print(Length)