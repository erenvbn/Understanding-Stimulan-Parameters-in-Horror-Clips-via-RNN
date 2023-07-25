

#parameters(sound_level_at_that_second,
           #number_of_peaks_before_that_second, brightness_level_of_that_second,
           #video_duration_multiplier, fear_level_at_the_last_peak_before_that_second, second_as_a_time)

#TIME(SECOND) PARAMETERS
time_seconds_uzun =[0, 7, 14, 44, 75, 88, 125, 147, 158, 203, 248, 265, 288, 299]#
time_seconds_kısa =[0, 7, 33, 44, 60, 75, 88, 95, 129, 140, 155, 190, 216, 229]#



#|-------------------------------------------------------------------------------------------------------------------
#BRIGHTNESS LEVEL and TIME
brightness_level_uzun= [0.11, 0.11, 2.18, 10.49, 8.12, 10.4, 10.32, 10.63, 0.11, 10.82, 7.62, 10.34, 4.11, 13.24]
brightness_level_kısa= [0.11, 0.11, 7.29, 10.75, 10.56, 10.6, 9.52, 10.32, 0.12, 10.83, 0.11, 8.36, 4.04, 13.06]




#|-------------------------------------------------------------------------------------------------------------------
#SOUND DATA SETS
#LONG VIDEO
v0_emregny_s =     [12, 32, 126, 108, 134, 74, 131, 26, 120, 65, 131, 90, 131,140]#
v1_adnangny_s =    [10, 24, 105, 90, 111, 62, 109, 21, 100, 53, 109, 75, 109, 116]#
v1_sunapkr_s =     [10, 24, 105, 90, 111, 62, 109, 21, 100, 53, 109, 75, 109, 116]#
v2_nslhn_s =       [3, 6, 25, 23, 27, 16, 28, 5, 25, 13, 28, 19, 28, 29]#
v4_trgy_s =        [10, 24, 105, 90, 111, 62, 109, 21, 100, 53, 109, 75, 109, 116]#
#v3_meryem_mtl_s =  [10, 24, 90, 70, 111, 45, 109, 15, 100, 39, 109, 60, 109, 116]]#
v8_srvtgny_s =     [10, 24, 107, 67, 42, 49, 56, 40, 48, 39, 44, 60, 45, 54]#

#SHORT VIDEO
#v7_sener_mtl_s =   [9, 31, 93, 25, 25, 16, 20, 27, 49, 71, 45, 41, 42, 31]#
v5_hsyngzl_s =     [3, 6, 25, 6, 25, 5, 5, 27, 49, 18, 12, 41, 42, 31] #
v9_engnpkr_s =     [9, 31, 93, 25, 25, 16, 20, 50, 60, 71, 45, 63, 80, 46]#





#|-------------------------------------------------------------------------------------------------------------------
#PEAK NUMBER BEFORE THAT POINT
#LONG VIDEO
#peak_number_before_that_point_uzun=  [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]#
#peak_number_before_that_point_kısa = [0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 5]#

v0_emregny_p =     [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]#
v1_adnangny_p =    [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]#
v1_sunapkr_p =     [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]#
v2_nslhn_p =       [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]#
v4_trgy_p =        [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]#
#v3_meryem_mtl_p = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]#
v8_srvtgny_p =     [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]#

#SHORT VIDEO
#v7_sener_mtl_p =  [0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 5]#
v5_hsyngzl_p =     [0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 5] #
v9_engnpkr_p =     [0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 5]]#




#|-------------------------------------------------------------------------------------------------------------------
#FEAR LEVEL AT POINTS
#LONG VIDEO
v0_emregny_f =    np.array([10,20,40,40,80,30,80,70,100,70,100,70,100,90])
v1_adnangny_f =   np.array([10,7,20,10,50,30,100,50,60,30,40,20,40,40])
v1_sunapkr_f =    np.array([10,20,30,45,60,40,125,50,50,50,60,35,50,80])
v2_nslhn_f =      np.array([20,15,20,17,15,25,20,17,15,17,20,10,20,25])
v4_trgy_f =       np.array([20,15,20,40,100,50,100,30,60,30,100,30,60,75])
v8_srvtgny_f =    np.array([20,30,30,60,50,50,50,30,50,60,50,40,50,60])
#LONG VIDEO
v5_hsyngzl_f =    np.array([20,15,10,10,12,15,17,20,20,10,10,20,25,20])
v9_engnpkr_f =    np.array([20,30,20,20,50,20,30,50,80,30,20,60,20,60])


#|-------------------------------------------------------------------------------------------------------------------
#THE TIME (Seconds) BETWEEN THAT PEAK and the PREVIOUS PEAK
#LONG VIDEO
#time_between_peaks_uzun =[0, 0, 0, 0, -0-, 13, -50-, 22, -33-, 45, -45-, 17, -40-, -11-]#
#time_between_peaks_kısa =[0, 0, 0, 0, -0-, 15, 28, -35-, -34-, 11, 26, -61-, -26-, -13-]#
#time_between_peaks_uzun =[0, 0, 0, 0, 0, 13, 50, 22, 33, 45, 45, 17, 40, 11]#
#time_between_peaks_kısa =[0, 0, 0, 0, 0, 15, 28, 35, 34, 11, 26, 61, 26, 13]#

#LONG VIDEO
v0_emregny_tbp =    np.array([0, 0, 0, 0, 0, 13, 50, 22, 33, 45, 45, 17, 40, 11])
v1_adnangny_tbp =   np.array([0, 0, 0, 0, 0, 13, 50, 22, 33, 45, 45, 17, 40, 11])
v1_sunapkr_tbp =    np.array([0, 0, 0, 0, 0, 13, 50, 22, 33, 45, 45, 17, 40, 11])
v2_nslhn_tbp =      np.array([0, 0, 0, 0, 0, 13, 50, 22, 33, 45, 45, 17, 40, 11])
v4_trgy_tbp =       np.array([0, 0, 0, 0, 0, 13, 50, 22, 33, 45, 45, 17, 40, 11])
v8_srvtgny_tbp =    np.array([0, 0, 0, 0, 0, 13, 50, 22, 33, 45, 45, 17, 40, 11])
#SHORT VIDEO
v5_hsyngzl_tbp =    np.array([0, 0, 0, 0, 0, 15, 28, 35, 34, 11, 26, 61, 26, 13])
v9_engnpkr_tbp =    np.array([0, 0, 0, 0, 0, 15, 28, 35, 34, 11, 26, 61, 26, 13])
#|-------------------------------------------------------------------------------------------------------------------

