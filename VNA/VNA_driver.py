import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import skrf as rf


class VNA():

    rm = pyvisa.ResourceManager()
    rc = rm.open_resource('TCPIP0::192.168.1.2::inst0::INSTR')
    ch = 1

    def __init__(self,power=0,num=201,center=6,span=4):
        self.power=power
        self.num=num
        self.center=center
        self.span=span

    def __setattr__(self, key, value):
        super(VNA, self).__setattr__(key,value)

    def __getattribute__(self, item):
        if item=='power':
            return "%d dBm"%self.power
        elif item=='num':
            return self.num
        elif item=='center':
            return "Center:%d GHz"
        elif item=='span':
            return "Span:%d GHz"
        else:
            return "NoneType"


    def set_value(self):
        self.rc.write('SOUR:POW %d dBm'%self.power)
        self.rc.write('SENS:FREQ:CENT %se9 Hz'%self.center)
        self.rc.write('SENS:FREQ:SPAN %se9 Hz' % self.span)
        self.rc.write('SENS:SWE:POIN %d' % self.num)


if __name__=='__main__':
    a=VNA()
    a.power=2
    a.num=4001
    a.set_value()
    print(a)