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

