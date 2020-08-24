import numpy as np
import lab

class JPA_Spec_vs_pFreq_Flux_SYT(lab.Application):
    '''

    '''
    async def work(self):
        async for Flux in self.sweep['Bias']:
            app = lab.make_app('NA.JPA_S21_vs_pumpFreq', parent=self)
            signal_freq, pumpFreq, y = await app.done()
            yield signal_freq, pumpFreq, Flux, y


    async def set_Bias(self,f):
        self.rc['flux_sour'].setValue('Output', 'ON', ch=8)
        self.rc['flux_sour'].setValue('Offset', f, ch=8)


    def pre_save(self, signal_freq, pumpFreq, Flux, z):
        if self.data.rows > 1:
            signal_freq = signal_freq[0]
            pumpFreq = pumpFreq[0]
        return signal_freq, pumpFreq, Flux, z

#     @staticmethod
#     def plot(fig, data):

#         signal_freq, pumpFreq, pumpPower, zr, zi = data

#         z=20*np.log10(np.abs(zr+1j*zi))
#         lab.imshow(fig, x/1e9, y, z, 'pumpFreq / GHz', 'pumpPower / V')