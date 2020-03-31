#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:05:10 2020

@author: shirongbao
"""

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
from generalFit import fit_data, fit_data_multi, fit_data_triple

def cos(x):
    return np.cos(x/180 * np.pi)
def test_func(x, a, b, c, d):
    
    return a * (cos(x/b * 360 + c) ** 2) + d

def findMax(params):
    period = params[1]
    phase = params[2]
    maxAt = (180 - phase)/360 * period
    print(params)
    print(maxAt)
    return None
    
    
    
### PB is H


## Set WP1 to max
#errors = np.array([1 for i in range(10)])
#
#angles = np.array([i * 10 for i in range(10)])
#det_2 = np.array([4.1, 24.3, 64.5, 102.5, 120.8, 115.2, 86.5, 48.9, 14.4, 3.7])
#guess = [100, 180, 90, 0]
#text = ['HWP2 angle with vertical direction/degrees', 'Detector 1 photon counts/kHz', '']
#findMax(fit_data(angles, det_2, errors, test_func, guess, text))
##print(fit_data(angles, det_2, errors, test_func, guess, text))
##print('[Amp, Period, Phase Shift, Y bias]')
#
#
#errors = np.array([0.1 for i in range(10)])
#errors[0] = 0.05
#coinc = np.array([0.07, 1.68, 5.01, 8.32, 10.20, 9.85, 7.45, 4.09, 1.08, 0.047])
#text = ['HWP2 angle with vertical direction/degrees', 'Coincidence counts/kHz', '']
#
#findMax(fit_data(angles, coinc, errors, test_func, guess, text))
##print(fit_data(angles, coinc, errors, test_func, guess, text))
##print('[Amp, Period, Phase Shift, Y bias]')


## Set WP2 to max
#errors = np.array([1 for i in range(10)])
#
#angles = np.array([i * 10 for i in range(10)])
#det_1 = np.array([8.2, 32.0, 68.7, 100.8, 113.0, 102.3, 72.2, 35.4, 9.5, 7.8])
#guess = [100, 180, 90, 0]
#text = ['HWP1 angle with vertical direction/degrees', 'Detector 1 counts/kHz', '']
#findMax(fit_data(angles, det_1, errors, test_func, guess, text))
##print(fit_data(angles, det_1, errors, test_func, guess, text))
##print('[Amp, Period, Phase Shift, Y bias]')
#
#text = ['HWP1 angle with vertical direction/degrees', 'Coincidence counts/kHz', '']
#errors = np.array([0.2 for i in range(10)])
#coinc = np.array([0.34, 2.57, 5.85, 8.65, 10.11, 9.18, 6.35, 3.15, 0.68, 0.37])
#findMax(fit_data(angles, coinc, errors, test_func, guess, text))
#
##print(fit_data(angles, coinc, errors, test_func, guess, text))
##print('[Amp, Period, Phase Shift, Y bias]')



### PB is V

## Set WP1 to max
#errors = np.array([1 for i in range(10)])
#
#angles = np.array([i * 10 for i in range(10)])
#det_2 = np.array([100.4, 85.5, 56.9, 25.1, 6.2, 10.2, 33.1, 64.0, 85.5, 91.6])
#guess = [100, 180, 0, 0]
#text = ['HWP2 angle with vertical direction/degrees', 'detectpr 2 counts/kHz', '']
#findMax(fit_data(angles, det_2, errors, test_func, guess, text))
##print(fit_data(angles, det_2, errors, test_func, guess, text))
##print('[Amp, Period, Phase Shift, Y bias]')
#
#text = ['HWP2 angle with vertical direction/degrees', 'Coincidence counts/kHz', '']
#errors = np.array([0.2 for i in range(10)])
#coinc = np.array([7.40, 6.5, 4.13, 1.61, 0.14, 0.46, 2.43, 4.9, 6.95, 7.45])
#guess = [10, 180, 0, 0]
#findMax(fit_data(angles, coinc, errors, test_func, guess, text))
##print(fit_data(angles, coinc, errors, test_func, guess, text))
##print('[Amp, Period, Phase Shift, Y bias]')


## Set WP2 to max
#errors = np.array([1 for i in range(10)])
#
#angles = np.array([i * 10 for i in range(10)])
#det_2 = np.array([72.7, 58.6, 36.2, 14.9, 4.5, 11.7, 32.6, 56.7, 72.0, 73.6])
#guess = [100, 180, 0, 0]
#text = ['HWP1 angle with vertical direction/degrees', 'Detector 1 counts/kHz', '']
#findMax(fit_data(angles, det_2, errors, test_func, guess, text))
##print(fit_data(angles, det_2, errors, test_func, guess, text))
##print('[Amp, Period, Phase Shift, Y bias]')
#
#text = ['HWP1 angle with vertical direction/degrees', 'Coincidence counts/kHz', '']
#errors = np.array([0.2 for i in range(10)])
#coinc = np.array([7.28, 5.85, 3.44, 1.21, 0.1, 0.78, 2.84, 5.42, 7.1, 7.3])
#guess = [10, 180, 0, 0]
#findMax(fit_data(angles, coinc, errors, test_func, guess, text))
##print(fit_data(angles, coinc, errors, test_func, guess, text))
##print('[Amp, Period, Phase Shift, Y bias]')


### Rotate PB (Draw these two on the same graph)
    
#errors = np.array([0.2 for i in range(10)])
#angles = np.array([i * 10 for i in range(10)])
#
#HH = [0.38, 2.43, 4.80, 6.79, 7.22, 6.01, 3.80, 1.42, 0.12, 0.39]
#VV = [9.05, 6.5, 3.52, 0.76, 0.062, 1.65, 4.6, 7.45, 8.95, 8.42]
#
#guess1 = [10, 180, 90, 0]
#text = ['HWP0 angle with vertical direction/degrees', 'Coincidence counts/kHz', '']
#print(fit_data(angles, HH, errors, test_func, guess1, text))
#print('[Amp, Period, Phase Shift, Y bias]')
#
#guess2 = [10, 180, 0, 0]
#print(fit_data(angles, VV, errors, test_func, guess2, text))
#print('[Amp, Period, Phase Shift, Y bias]')
#
#VH = [0.125, 0.18, 0.18, 0.13, 0.095, 0.12, 0.16, 0.13, 0.091, 0.12]
#
#print(fit_data_multi(angles, HH, VV, VH, errors, test_func, guess1, guess2, text, ifFindCross = True))



# Remote state prep
data = []
# HWP1 @ 0

errors = np.array([0.1 for i in range(9)])
errors[4] =0.01

angles = np.array([i * 10 for i in range(9)])
coinc = np.array([2.98, 2.41, 1.35, 0.43, 0.016, 0.34, 1.21, 2.18, 2.91])
guess = [2, 180, 0, 0]
text = ['HWP2 angle with vertical direction/degrees', 'Coincidence counts/kHz', '']
#findMax(fit_data(angles, coinc, errors, test_func, guess, text))

data.append([angles, coinc, errors, guess])
# HWP1 @ 22.5

errors = np.array([0.1 for i in range(6)])
errors[0] =0.03
errors[5] =0.02

angles = np.array([0, 20, 40, 60, 80, 87])
coinc = np.array([0.08, 1.37, 2.28, 1.41, 0.11, 0.015])
guess = [6, 180, 40, 0]
text = ['HWP2 angle with vertical direction/degrees', 'Coincidence counts/kHz', '']
#findMax(fit_data(angles, coinc, errors, test_func, guess, text))

data.append([angles, coinc, errors, guess])


# HWP1 @ 45
    
errors = np.array([0.1 for i in range(7)])
errors[0] =0.03
errors[5] =0.02

angles = np.array([0, 10, 16, 20, 40, 60, 80])
coinc = np.array([0.6, 0.098, 0.015, 0.049, 1.25, 2.22, 1.39])
guess = [2, 180, 70, 0]
text = ['HWP2 angle with vertical direction/degrees', 'Coincidence counts/kHz', '']
#findMax(fit_data(angles, coinc, errors, test_func, guess, text))

data.append([angles, coinc, errors, guess])

#fit_data_triple(x_data, y_data_1, y_data_2, y_data_3, errors, func, guess1, guess2, guess3, text, ifFindCross = False)


fit_data_triple(data, test_func, text)








