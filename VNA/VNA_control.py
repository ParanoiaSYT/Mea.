import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
ch=1
rm = pyvisa.ResourceManager()
rc= rm.open_resource('TCPIP0::192.168.1.2::hislip0::INSTR')


center=10e9
span=5e9
number=2000
# rc.write('INIT:CONT ON')
# rc.write('CALC:FORM LIN')
# rc.write('SEN:SWE:TYPE LIN')
# rc.write('INIT:IMM')
# rc.write('*WAI')
rc.write('SOUR:POW 15 dBm')
rc.write('SENS:FREQ:CENT %s Hz'%center)
rc.write('SENS:FREQ:SPAN %s Hz'%span)
rc.write('SENS:SWE:POIN %d'%number)
# rc.write('FORM:BORD NORM')
# rc.write('FORMAT ASCII')


cmd=("CALC%d:DATA? SDATA"%ch)


data1=np.asarray(rc.query_ascii_values(cmd))

data1=data1[::2]+1j*data1[1::2]
# print(data1)
# print(len(data1))
data2=np.array(np.linspace(center-span,center+span,number))
fig, axes = plt.subplots(1, 1, figsize=(10, 6))

# axes.plot(data2,rf.mag_2_db(np.abs(data1)))
axes.plot(data2,data1)
axes.legend('hjsafkjafg')
axes.set_xlabel('frequency')
axes.set_ylabel('S')
axes.set_title('S_vs_frequency')
plt.show()