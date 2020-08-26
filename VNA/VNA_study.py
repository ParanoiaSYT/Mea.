import pyvisa
import numpy as np
# p=input()
rm=pyvisa.ResourceManager()
rc=rm.open_resource('TCPIP0::192.168.1.2::inst0::INSTR')


# Power part
# rc.write('SOUR:POW1 %s dBm'%p) #source power for port1
# rc.write('SOUR:POW1:SLOP %s'%p) #source power slope for port1
# rc.write('SOUR:POW1:PORT:STAR %s dBm'%p) #source power start for port1
# rc.write('SOUR:POW1:PORT:STOP %s dBm'%p) #source power stop for port1
# rc.write('SOUR:POW:STAR %s dBm'%p) #source power start for all ports
# rc.write('SOUR:POW:STOP %s dB,'%p) #source power stop for all ports
# rc.write('SOUR:POW:CENT 20 dBm') #power center
# rc.write('SOUR:POW:SPAN 20 dBm') #power span
# rc.write('OUTP 1')#{1|0} turn on/off the RF power


# Frequency part
# rc.write('SENS:FREQ:CENT 5e9 Hz') #frequency center
# rc.write('SENS:FREQ:SPAN 5e6 Hz') #frequency range
# rc.write('SENS:FREQ:STAR 9e6 Hz') #frequency start
# rc.write('SENS:FREQ:STOP 9e9 Hz') #frequency stop
# rc.write('SENS:SWE:TYPE CW; :SENS:FREQ:CW 15e9') # set the continuous wave frequency, unit is Hz

# Sweep part
# rc.write('SENS:SWE:POIN 2000') #the number of points sweep
# rc.write('SENS:SWE:TIME 10 s') #the scale of time sweep
# rc.write('SENS:SWE:TYPE CW') # {LIN|LOG|SEGM|POW|CW} sweep type
# rc.write('SENS:SWE:MODE SING ') # sweep one time
# rc.write('SENS1:SWE:GRO:COUN 200; :SENS1:SWE:MODE GRO ')# sweep how many times

# Trigger part
# rc.write('SENS:SWE:MODE CONT' ) #{HOLD|CONT} trigger's mode
# rc.write('TRIG:SEQ:SOUR MAN')#{IMM|EXT|MAN} trigger's source from internal/external/manual

# IF bandwidth part
# rc.write('SENS:BAND 15e6 Hz') #IF bandwidth

# Ports part
# rc.write('SENS:CORR:EXT:STAT 0') #{1|0} turn on/off the port extensions

# Table part
# rc.write('DISP:ARR QUAD')#{TILE|CASCade|OVERlay one |STACk two |SPLit three|QUAD four} tables
# rc.write('DISP:VIS 1')#{1|0} visible or not
# rc.write('DISP:WIND1 0')#{1|0} table open or not
# rc.write('DISP:WIND1:TITL 0')#{1|0} title open or not
# rc.write('DISP:WIND1:TITL:DATA "100"')#Set / Get the data in the window title area




# print(rc.write('FORMAT:DATA REAL'))

#rc.write('FORMAT:DATA ASCII')



# rc.write('CALC{Measurement}:SEL:DATA:SDAT?;CALC{Measurement}:DATA? SDATA  ')


# rc.write('MMEM:STOR .csa ')


# rc.write('SENS:CORR:PREF:ECAL:ORI 1')#{1|0}





# rc.write('DISP:TMAX 1') #{1|0}
# rc.write('DISP:WIND1:TRAC :Y:RPOS')



# rc.write('SENS1:CORR:EXT:PORT1:TIME? ')




# rc.write('SYST:FPReset')
# rc.write('DISPlay:WINDow1:STATE ON')


# rc.write('CALCulate:PARameter:DEFine:EXT "TCPIP0::192.168.1.2::inst0::INSTR",S21')







# import pyvisa
# import numpy as np
# import time
# import matplotlib.pyplot as plt
#
# rm = pyvisa.ResourceManager()
# rc = rm.open_resource('TCPIP0::192.168.1.2::inst0::INSTR')
#
# def sweep_power():
#     power_list = range(10)
#     for i, p in enumerate(power_list):
#         rc.write('SOUR:POW %s dBm'%p)
#         DATA = rc.write(':FORM:DATA ASC')
#         time.sleep(1)
#         print(DATA)
# sweep_power()
# 师兄所给



#
# rc.write('SENS:FREQ:CENT 5e9 Hz') #frequency center
# rc.write('SENS:FREQ:SPAN 5e6 Hz') #frequency range
# rc.write('CALCulate1:PARameter:CATalog?')
# # rc.write('SOUR:POW1 15 dBm')
#rc.write('CURV?')
# trace1=rc.read_bytes(1)
# # trace2=rc.read_bytes(3)
# trace3=rc.read_raw()
# # values=rc.query_ascii_values('CURV?', container=np.array)
# # values=rc.query_binary_values('CURV?', datatype='d', is_big_endian=True)
# print(trace1)
# # print(trace2)
# print(trace3)
# # print(values)
# trace=rc.query("trace:data?")
# print(trace)
# rc.write('MMEMory:STORe:DATA "WXH.cti", "Citifile Data Data","AUTO","RI",1')#save data on th NA
# f = open( '/Users/michael/test.txt', 'r' )


f = open( 'C://Users//Administratro//Desktop//WXH.cti', 'r' )
print(f)