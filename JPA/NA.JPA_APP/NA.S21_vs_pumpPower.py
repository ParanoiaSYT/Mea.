import numpy as np
import asyncio
import lab
import matplotlib.pyplot as plt


class JPA_S21_vs_ppower(lab.Application):
    '''

    '''

    async def work(self):
        async for ppower in self.sweep['ppower']:
            app = lab.make_app('NA.S21', parent=self)
            x, re, im = await app.done()
            y = 20 * np.log10(np.abs(re + 1j * im))
            yield x, ppower, y

    async def set_ppower(self, f):
        await asyncio.sleep(0.1)
        self.rc['pump_sour'].setValue('Power', f)

    def pre_save(self, x, Freq, y):
        if self.data.rows > 1:
            x = x[0]
        return x, Freq, y

    @staticmethod
    def plot(fig, obj):
        x, y, z = obj
        ax = fig.add_subplot(111)
        if isinstance(y, np.ndarray):

            extent = (min(x), max(x), min(y), max(y))
            ax.imshow(z, extent=extent,
                      aspect='auto', origin='lower', interpolation='nearest')
        else:
            ax.plot(x, z)
        ax.set_xlabel('ProbFreq / Hz')
        ax.set_ylabel('Ppower / Hz')
        ax.set_title('NA.S21_vs_drivFreq')