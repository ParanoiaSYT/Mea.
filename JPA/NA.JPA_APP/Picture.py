import lab


res = lab.query('NA.JPA_Spec_vs_ppower_pfreq_SYT')
print(res[-1].id)

res=lab.query(id__in=['5f34adc2bfde9e2c6080b4c9'])
rd = res[0].data

len(rd)

signal_freq, pump_freq, pump_power, z = rd
signal_freq
pump_freq
pump_power
# z


import numpy as np
import asyncio
import lab
import matplotlib.pyplot as plt

signal_freq, pump_freq, pump_power, z = rd

# 画出所有图
for i in range(len(z)):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    if isinstance(z[i], np.ndarray):
        extent=(min(signal_freq/1e9), max(signal_freq/1e9), min(pump_freq/1e9), max(pump_freq/1e9))
        im=ax.imshow(z[i], extent=extent,aspect='auto', origin='lower', interpolation='nearest')
        plt.colorbar(im)

    else:
        ax.plot(signal_freq,z[i])

    ax.set_xlabel('SingnalFreq / GHz')
    ax.set_ylabel('PumpFreq / GHz')
    ax.set_title('NA.JPA_Spec_vs_ppower_pfreq_SYT+pump_power=(%d-40)dBm'%pump_power[i])


# 切单条画出来
res=lab.query(id__in=['5f352de9bfde9e1f50c266ec'])
rd = res[0].data
signal_freq, pump_freq, pump_power, z = rd
for num in range(210,221):
    z8=z[18][num]
    print(pump_freq[num]/1e9)
    plt.figure()
    plt.plot(signal_freq, z8)
# plt.set_xlabel('Signal_Frequency / GHz')
# plt.set_ylabel('S21 / dB')
# plt.set_title('NA.JPA_S21')