from PIL import Image
from PIL import ImageStat
import math

import numpy as np
import matplotlib.pyplot as plt


def brightness( im_file ):
   im = Image.open(im_file)
   stat = ImageStat.Stat(im)
   r,g,b = stat.mean
   print(im_file, round(math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)),2))

print ("Kısa_videonun_parlaklıkları")
brightness('C:\\Kısa-0.jpg')
brightness('C:\\Kısa-7.jpg')
brightness('C:\\Kısa-33.jpg')
brightness('C:\\Kısa-44.jpg')
brightness('C:\\Kısa-60.jpg')
brightness('C:\\Kısa-75.jpg')
brightness('C:\\Kısa-88.jpg')
brightness('C:\\Kısa-95.jpg')
brightness('C:\\Kısa-129.jpg')
brightness('C:\\Kısa-140.jpg')
brightness('C:\\Kısa-155.jpg')
brightness('C:\\Kısa-190.jpg')
brightness('C:\\Kısa-216.jpg')
brightness('C:\\Kısa-229.jpg')

print ("Uzun_videonun_parlaklıkları")
brightness('C:\\Uzun-0.jpg')
brightness('C:\\Uzun-7.jpg')
brightness('C:\\Uzun-14.jpg')
brightness('C:\\Uzun-44.jpg')
brightness('C:\\Uzun-75.jpg')
brightness('C:\\Uzun-88.jpg')
brightness('C:\\Uzun-125.jpg')
brightness('C:\\Uzun-147.jpg')
brightness('C:\\Uzun-158.jpg')
brightness('C:\\Uzun-203.jpg')
brightness('C:\\Uzun-248.jpg')
brightness('C:\\Uzun-265.jpg')
brightness('C:\\Uzun-288.jpg')
brightness('C:\\Uzun-299.jpg')

#-------------------------------------------------------------------------------------------------------------------
#Kısa_videonun_parlaklıkları
(float(0.11), 0)
(float(0.11), 7)
(float(7.29), 33)
(float(10.75), 44)
(float(10.56), 60)
(float(10.6), 75)
(float(9.52), 88)
(float(10.32), 95)
(float(0.12), 129)
(float(10.83), 140)
(float(0.11), 155)
(float(8.36), 190)
(float(4.04), 216)
(float(13.06), 229)
#-------------------------------------------------------------------------------------------------------------------
#Uzun_videonun_parlaklıkları
(float(0.11), 0)
(float(0.11), 7)
(float(2.18), 14)
(float(10.49), 44)
(float(8.12), 75)
(float(10.4), 88)
(float(10.32), 125)
(float(10.63), 147)
(float(0.11), 158)
(float(10.82), 203)
(float(7.62), 248)
(float(10.34), 265)
(float(4.11), 288)
(float(13.24), 299)

#-------------------------------------------------------------------------------------------------------------------
brightness_level_kısa=[0.11, 0.11, 7.29, 10.75, 10.56, 10.6, 9.52, 10.32, 0.12, 10.83, 0.11, 8.36, 4.04, 13.06]
time_seconds_kısa =[0, 7, 33, 44, 60, 75, 88, 95, 129, 140, 155, 190, 216, 229]

plt.scatter(time_seconds_kısa, brightness_level_kısa)
plt.ylabel("Brightness Level(0-20)")
plt.xlabel('Time(seconds)')
plt.title("Brightness Level-Time")
ax = plt.gca()
ax.set_ylim([0, 20])
ax.set_xlim([0, 304])
plt.show()
#|-------------------------------------------------------------------------------------------------------------------
brightness_level_uzun=[0.11, 0.11, 2.18, 10.49, 8.12, 10.4, 10.32, 10.63, 0.11, 10.82, 7.62, 10.34, 4.11, 13.24]
time_seconds_uzun =[0, 7, 14, 44, 75, 88, 125, 147, 158, 203, 248, 265, 288, 299]

plt.scatter(time_seconds_uzun, brightness_level_uzun)
plt.ylabel("Brightness Level(0-20)")
plt.xlabel('Time(seconds)')
plt.title("Brightness Level-Time")
ax = plt.gca()
ax.set_ylim([0, 20])
ax.set_xlim([0, 304])
plt.show()