import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open('C:\Video-3-ses.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

#If Stereo
if spf.getnchannels() == 2:
    print ('Just Mono Files')
    sys.exit(0)

plt.figure(1)
plt.title('Value of Signal Wave')
plt.plot(signal)
plt.show()

#SOUND DATA SETS
time_seconds_uzun =[0, 7, 14, 44, 75, 88, 125, 147, 158, 203, 248, 265, 288, 299]#
v0_emregny_s =     [12, 32, 126, 108, 134, 74, 131, 26, 120, 65, 131, 90, 131,140]#
v1_adnangny_s =    [10, 24, 105, 90, 111, 62, 109, 21, 100, 53, 109, 75, 109, 116]#
v1_sunapkr_s =     [10, 24, 105, 90, 111, 62, 109, 21, 100, 53, 109, 75, 109, 116]#
v2_nslhn_s =       [3, 6, 25, 23, 27, 16, 28, 5, 25, 13, 28, 19, 28, 29]#
v4_trgy_s =        [10, 24, 105, 90, 111, 62, 109, 21, 100, 53, 109, 75, 109, 116]#
v3_meryem_mtl_s =  [10, 24, 90, 70, 111, 45, 109, 15, 100, 39, 109, 60, 109, 116]#
v8_srvtgny_s =     [10, 24, 107, 67, 42, 49, 56, 40, 48, 39, 44, 60, 45, 54]#

time_seconds_kısa =[0, 7, 33, 44, 60, 75, 88, 95, 129, 140, 155, 190, 216, 229]#
v7_sener_mtl_s =   [9, 31, 93, 25, 25, 16, 20, 27, 49, 71, 45, 41, 42, 31]#
#v5_hsyngzl_s =     [3, 6, 25, 6, -25-, 5, 5, -27-, -49-, 18, 12, -41-, -42-, -31-] #
v9_engnpkr_s =     [9, 31, 93, 25, 25, 16, 20, 50, 60, 71, 45, 63, 80, 46]#
