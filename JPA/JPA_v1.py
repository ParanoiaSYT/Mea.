import lab
lab.login('zw','12345678')

# The single qubit measurement procedure of VNA is as follows:
# Finding probe parameters:
#     1. cavity spectroscopy measurement,
#     2. cavity spectroscopy vs probe power,
#     3. cavity spectroscopy vs flux amplitude(for SQUID),
#     4.
#     finally, we get probe parameters have probe power, probe frequency, flux bias(for SQUID)
#
# Finding qubit spectroscopy:
#     according by chosing appropriate probe parameters, we could find qubit spectroscopy by
#         1. fixed appropriate driving power, sweep driving frequency,
#         2. get spectroscopy pattern by qubit frequency vs flux bias
# By VNA measurement, we ultimate aim is getting the qubit basic paramters like
# f01_frequency, f01_frequency_vs_flux(for SQUID), and the readout_parameters.
# NOTE:
# 1. VNA mesurement only supports continuous mesurement.
# 2. These APPs has not supported multi-qubits simultaneously mesuring due to thet VNA E8257D has not such function.


# measuring_settings
settings_dict = {

    'instrument': {
        'NA': 'Agilent_E8363B',
        'driv_sour': 'SGS733',
        'flux_sour': '3202A_slot7',
        #         'flux_sour': 'SRS_SIM',
    },

    'VNA_settings': {
        'VNA_Power': -15,  # unit: dBm
        'VNA_repeat': 1,  # repeats

        'basicParameters': {
            'userDefine_VNA_settings': True,
            'cavity_point_set': ['custom', 6.670e9],
            'center_freq': 7.83e9,
            #             'center_freq': 7.133e9,
            'sweep_Bandwidth': 50,
            'sweep_points': 201,
            'freq_start': 6.750e9,
            'freq_stop': 6.760e9,
            'sweep_span_freq': 4e6,
        },
    },

    'drive_settings': {
        'drive_power': 10,  # unit: dBm
        'drive_freq': 5e9,  # unit: Hz
    },

    'flux_settings': {
        #         'flux_settings_visualization': True,
        'fluxSourceType': 'awg_withFourChannels',
        'fluxBiasChannels': [1, 2, 3, 4],
        #         'fluxSourceType': 'SRS_SIM',
        #         'fluxBiasChannels':[8],
        'fluxWaveformType': 'DC_like',
        'flux_legenth_ref': 10e-6,
        'awg_sRate': 1e9,
        'awg_amplitude': 1.5,

        'sweepFlux_ch': 4,  # channel = 1, 2, 3, 4
        'staticfluxVoltageActual': [[0], [0], [0], [0]],

        'staticfluxCrosstalkMat': [[1, 0, 0, 0],
                                   [0, 1, 0, 0],
                                   [0, 0, 1, 0],
                                   [0, 0, 0, 1]],
    },

    #     'shut_down_all_instruments': False,
    #     'S21_fit': True,
}

# measurement_execute_code
% matplotlib
notebook
import numpy as np
import lab

sweep_list = [
    lab.Sweep('VNA_power', np.linspace(-20, 5, 26), unit='dBm'),
    lab.Sweep('flux_bias', np.linspace(-1.5, 1.5, 31), unit='V'),
    lab.Sweep('drive_freq', np.linspace(4e9, 5e9, 1001), unit='Hz'),
]

app_str = ['S21', 'S21_vs_VNApower', 'S21_vs_flux', 'qSpec']
app = lab.make_app(app_str[0], package='VNA').sweep(sweep_list
                                                    ).with_rc(settings_dict['instrument']).with_settings(settings_dict)

lab.make_figure_for_app(app)
app.setUp(app.init_set).tearDown(app.tear_down).run()

# Image(value=b'', format='svg+xml')
# HBox(children=(Button(description='Pause', style=ButtonStyle()), Button(description='Interrupt', style=ButtonS…
# S21_idx: 5f1ceebbbfde9e062c58b2f1


# 测量腔频
    '''腔频'''
import numpy as np
import skrf as rf
import lab

from cqed_toolbox.qulab_app.toolbox_zw import general_funcs_for_app  as gfa
from cqed_toolbox.qulab_app.toolbox_zw import fit_model  as fm


class S21(lab.Application):
    """
    Aquire S21 data from VNA.

    return:
        Frequency, Re(S21), Im(S21)
    """

    async def work(self):
        x = self.rc['NA'].get_Frequency()
        for i in range(self.settings.get('VNA_repeat', 1)):
            if self.settings.get('Push process', True):
                self.processToChange(100.0 / self.settings.get('VNA_repeat', 1))
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
        ax.set_xlabel('Frequency [GHz]')
        ax.set_ylabel('Amplitude [dB]')
        ax.set_title('S21')

        ax2 = fig.add_subplot(122)
        ax2.plot(x / 1e9, np.rad2deg(np.angle(z)))
        ax2.set_xlabel('Frequency [GHz]')
        ax2.set_ylabel('Angle [Deg]')
        ax2.set_title('S21')

    def init_set(self):
        """ instrument initial settings """
        gfa.VNA_init_set(obj=self)

    def tear_down(self):
        if self.settings.get('shut_down_all_instruments', True):
            self.rc['NA'].init({'Output': 'OFF'})

        res = lab.query('VNA.S21')
        cou = res.count()
        print('S21_idx: %s' % res[cou - 1].id)

        if self.settings.get('S21_fit', False):
            idx = res[cou - 1].id
            res = lab.query(id__in=['%s' % idx])
            r = res[0]
            fm.S21_fit(r, method='UCSB')
#             fm.S21_fit(r, params=globals().get('params', None), method='UCSB', level=3, skep=2)
S21.save(package='VNA')