import numpy as np
import skrf as rf
from lab import Application


class JPA_S21(Application):
    '''从网分上读取 JPA_S21
    require:
        rc : NA
        settings: repeat(optional)

    return: Frequency, Re(S21), Im(S21)
    '''

    async def work(self):
        if self.params.get('power', None) is None:
            self.params['power'] = [self.rc['NA'].getValue('Power'), 'dBm']
        else:
            self.rc['NA'].setValue('Power', self.params['power'][0])
        x = self.rc['NA'].get_Frequency()
        for i in range(self.settings.get('repeat', 1)):
            if self.settings.get('Push process', True):
                self.processToChange(100.0 / self.settings.get('repeat', 1))
            y = np.array(self.rc['NA'].get_S())
            yield x, np.real(y), np.imag(y)
            if self.settings.get('Push process', True):
                self.increaseProcess()

    def pre_save(self, x, re, im):
        if self.data.rows > 1:
            x = x[0]
            re = np.mean(re, axis=0)
            im = np.mean(im, axis=0)
        return x, re, im

    @staticmethod
    def plot(fig, data):
        x, re, im = data
        z = re + 1j * im
        ax = fig.add_subplot(121)
        ax.plot(x / 1e9, rf.mag_2_db(np.abs(z)))
        ax.set_xlabel('Frequency / GHz')
        ax.set_ylabel('S21 / dB')
        ax.set_title('NA.JPA_S21')

        ax2 = fig.add_subplot(122)
        ax2.plot(x / 1e9, np.rad2deg(np.angle(z)))
        ax2.set_xlabel('Frequency/ GHz')
        ax2.set_ylabel('Angle / Deg')
        ax2.set_title('NA.JPA_S21')

