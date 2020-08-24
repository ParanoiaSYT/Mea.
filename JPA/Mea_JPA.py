
# 此处修改为对应的app
app = lab.make_app('JPA_S21_vs_ppower', package='NA').with_rc({
    'NA': 'Agilent_E8363B',
    'pump_sour': 'SGS733',
    #     'pump_sour':'PSG_E8257C',
    'flux_sour': 'SRS_SIM',
}).sweep(
    [lab.Sweep('Freq', np.linspace(6.2e9, 7.0e9,401), unit='Hz'),
     lab.Sweep('pumpPower', np.linspace(-10, 17, 28), unit='dBm'),
     lab.Sweep('Bias', np.linspace(0,-0.5,10), unit='V')

     #    ('ppower', np.linspace(9, 11, 21), unit='dBm'),
     # ('pumpAmp', np.linspace(0, 5, 21), 'dBm'),
     # ('flux', np.linspace(0.15, 0.25, 101), 'V'),
     # ('pumpFreq', np.linspace(6.84e9, 6.9e9, 41), 'Hz'),
     ]).with_settings({
    'MarkerIndex': 201,  ### span points. 2*index + 1
    'repeat': 1,
    'SRS_SIM_ch': 7,
    'with_single_freq_point': False,
    'CavityType': 'custom',
    'Meas_freq point': 6.8e9,  ### center frequency
    'freq_span': 50e6,  #### frequency span

}).with_params(
    power=[-20, 'dBm'],
    # bias=[0.33, 'V'],
    pumpfreq=[6.825e9, 'Hz'],
    ppower=[10,'dBm']


).with_tags(*tags0, '1000 ohmu')


def setUp(app=app):
    # app.rc['flux_sour'].setValue('Output', 'ON', ch=8)
    # app.rc['flux_sour'].setValue('Offset', app.params.['bias'][0], ch=8)

    app.rc['pump_sour'].init({
        'Frequency': app.params['pumpfreq'][0],
        'Output': 'ON',
        #         'Output': 'OFF',
        'Power':app.params['ppower'][0],
    })


def tearDown(app=app):
    app.rc['pump_sour'].init({'Output': 'OFF'})
    app.rc['flux_sour'].setValue('Output', 'OFF', ch=1)

    res = lab.query('NA.JPA_S21_vs_ppower')
    cou = res.count()
    print(res[cou - 1].id)


# 这个是画上面图的
lab.make_figure_for_app(app)
# 下面这个是画S21的
lab.make_figures_for_App('S21')
app.setUp(setUp).tearDown(tearDown).run()