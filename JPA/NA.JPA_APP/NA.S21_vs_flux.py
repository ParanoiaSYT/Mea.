import numpy as np
import asyncio
import lab

class S21_vs_flux(lab.Application):
    ''' 变磁通读S21 '''

    async def work(self):
        async for flux in self.sweep['flux']:
            app = lab.make_app('NA.S21',parent=self)
            freq,re,im = await app.done()
            if self.rc['NA'].getValue('Format')=='MLOG':
                z=20*np.log10(np.abs(re+1j*im))
            if self.rc['NA'].getValue('Format')=='PHAS':
                z=90*np.arctan(im/re)
            yield freq, flux, z

    async def set_flux(self, f):
        self.rc['flux_sour'].setValue('Offset', f)
        await asyncio.sleep(0.1)

    def pre_save(self, freq, flux, z):
        if self.data.rows > 1:
            freq = freq[0]
        return freq, flux, z

    @staticmethod
    def plot(fig, obj):
        freq,flux,z = obj
        ax = fig.add_subplot(111)
        if isinstance(flux, np.ndarray):
            extent=(min(freq), max(freq), min(flux), max(flux))
            ax.imshow(z, extent=extent,
                aspect='auto', origin='lower', interpolation='nearest')
        else:
            ax.plot(freq,z)
        ax.set_xlabel('Frequency / Hz')
        ax.set_ylabel('Flux / V')
        ax.set_title('NA.S21_vs_flux')