#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:38:11 2020

@author: shirongbao
"""

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
from generalFit import fit_data

def cos(x):
    return np.cos(x/180 * np.pi)
def test_func(x, a, b, c, d):
    
    return a * (cos(x/b * 360 + c) ** 2) + d



angles = np.array([i * 10 for i in range(10)])
errors = np.array([1 for i in range(10)])
det_A = np.array([2.6, 7.1, 18.3, 30.6, 37.9, 37.1, 28.5, 16.6, 6.4, 2.4])
guess = [36, 180, 90, 0] # [Amp, Period, Phase Shift, Y bias]
text = ['x', 'y', 'title']

print(fit_data(angles, det_A, errors, test_func, guess, text))
print('[Amp, Period, Phase Shift, Y bias]')

det_B = np.array([3.2, 12.2, 26.7, 39.6, 44.6, 40.4, 28.3, 14.4, 4.4, 3.4])
guess = [36, 180, 90, 0] # [Amp, Period, Phase Shift, Y bias]
print(fit_data(angles, det_B, errors, test_func, guess, text))
print('[Amp, Period, Phase Shift, Y bias]')


#
#params_A, params_covariance = optimize.curve_fit(test_func, angles, det_A,
#                                               p0=[36, 0.07, 5, 2])
#
#print(params_A)
#
#a, b, c, d = params_A[0], params_A[1], params_A[2], params_A[3]
#
#print('Amplitude ' + str(a) + ', Minimum count ' + str(d - a) + ', Maximum count ' + str(d + a) 
#            + ', Period ' + str(2 * np.pi/b) + ', Peak at angle ' + str(((np.pi * 5/2)-c)/b))
#print('Covariance: ' + str(params_covariance))
#fig = plt.figure()
#
#angles_1 = np.array(list(range(0, 90, 1)))
#
#plt.figure(figsize=(6, 4))
##plt.scatter(angles, det_A, label='Data')
#plt.errorbar(angles, det_A, yerr=errors, label='Data', fmt = 'none')
#plt.plot(angles_1, test_func(angles_1, a, b, c, d),
#         label='Fitted function')
#plt.xlabel('Wave plate angle/degrees')
#plt.ylabel('Detector counts')
#plt.title('Detector counts vs wave plate angle for detector A')
#plt.legend(loc='best')
#
#plt.show()
#
#
#params_B, params_covariance = optimize.curve_fit(test_func, angles, det_B,
#                                               p0=[36, 0.07, 5, 2])
#
#print(params_B)
#
#a, b, c, d = params_B[0], params_B[1], params_B[2], params_B[3]
#
#print('Amplitude ' + str(a) + ', Minimum count ' + str(d - a) + ', Maximum count ' + str(d + a) 
#            + ', Period ' + str(2 * np.pi/b) + ', Peak at angle ' + str(((np.pi * 5/2)-c)/b))
#print('Covariance: ' + str(params_covariance))
#
#fig = plt.figure()
#
#plt.figure(figsize=(6, 4))
##plt.scatter(angles, det_A, label='Data')
#plt.errorbar(angles, det_B, yerr=errors, label='Data', fmt = 'none')
#plt.plot(angles_1, test_func(angles_1, a, b, c, d),
#         label='Fitted function')
#plt.xlabel('Wave plate angle/degrees')
#plt.ylabel('Detector counts')
#plt.title('Detector counts vs wave plate angle for detector B')
#plt.legend(loc='best')
#
#plt.show()
#
#
#
#
#
#
#
