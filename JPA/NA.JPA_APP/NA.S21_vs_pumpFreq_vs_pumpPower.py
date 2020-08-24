import numpy as np
import lab

class JPA_Spec_vs_ppower_pfreq_SYT(lab.Application):
    '''

    '''
    async def work(self):
        async for pumpPower in self.sweep['pumpPower']:
            app = lab.make_app('NA.JPA_S21_vs_pumpFreq', parent=self)
            signal_freq, pumpFreq, y = await app.done()
            yield signal_freq, pumpFreq, pumpPower, y

    async def set_pumpPower(self, p):
        self.rc['pump_sour'].setValue('Power', p)
        print('pump_power: %s'%p)

    def pre_save(self, signal_freq, pumpFreq, pumpPower, z):
        if self.data.rows > 1:
            signal_freq = signal_freq[0]
            pumpFreq = pumpFreq[0]
        return signal_freq, pumpFreq, pumpPower, z

#     @staticmethod
#     def plot(fig, data):

#         signal_freq, pumpFreq, pumpPower, zr, zi = data

#         z=20*np.log10(np.abs(zr+1j*zi))
#         lab.imshow(fig, x/1e9, y, z, 'pumpFreq / GHz', 'pumpPower / V')