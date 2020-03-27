#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:54:49 2020

@author: shirongbao
"""
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

#def test_func(x, a, b, c, d):
#    return a * np.sin(b * x + c) + d

def generate_seq(min0, max0, nbr_steps):
    
    step = (max0 - min0)/nbr_steps
    out = [min0]
    cur = min0
    for i in range(nbr_steps):
        cur += step
        out.append(cur)
        
    return np.array(out)
    
    
    
    
def fit_data(x_data, y_data, errors, func, guess, text):
    
    [xlabel, ylabel, title] = text


#
#    angles = np.array([i * 10 for i in range(10)])
#    errors = np.array([1 for i in range(10)])
#    det_A = np.array([2.6, 7.1, 18.3, 30.6, 37.9, 37.1, 28.5, 16.6, 6.4, 2.4])
#    det_B = np.array([3.2, 12.2, 26.7, 39.6, 44.6, 40.4, 28.3, 14.4, 4.4, 3.4])

    params_A, params_covariance = optimize.curve_fit(func, x_data, y_data,
                                               p0=guess)

    a, b, c, d = params_A[0], params_A[1], params_A[2], params_A[3]
    x_sim = generate_seq(np.amin(x_data), np.amax(x_data), x_data.size * 10)
    y_sim = func(x_sim, a, b, c, d)
    plt.figure(figsize=(6, 4))
    #plt.scatter(angles, det_A, label='Data')
    plt.errorbar(x_data, y_data, yerr=errors, label='Measured data', fmt = 'none')
    plt.plot(x_sim, y_sim, label='Fitted function')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc='best')
    
    plt.show()

    return params_A

def fit_data_multi(x_data, y_data_1, y_data_2, errors, func, guess1, guess2, text, ifFindCross = False):
    
    [xlabel, ylabel, title] = text


#
#    angles = np.array([i * 10 for i in range(10)])
#    errors = np.array([1 for i in range(10)])
#    det_A = np.array([2.6, 7.1, 18.3, 30.6, 37.9, 37.1, 28.5, 16.6, 6.4, 2.4])
#    det_B = np.array([3.2, 12.2, 26.7, 39.6, 44.6, 40.4, 28.3, 14.4, 4.4, 3.4])

    params_1, params_covariance = optimize.curve_fit(func, x_data, y_data_1,
                                               p0=guess1)

    a1, b1, c1, d1 = params_1[0], params_1[1], params_1[2], params_1[3]
    
    params_2, params_covariance = optimize.curve_fit(func, x_data, y_data_2,
                                               p0=guess2)

    a2, b2, c2, d2 = params_2[0], params_2[1], params_2[2], params_2[3]
    
    
    x_sim = generate_seq(np.amin(x_data), np.amax(x_data), x_data.size * 10)
    y_1 = func(x_sim, a1, b1, c1, d1)
    y_2 = func(x_sim, a2, b2, c2, d2)


    plt.figure(figsize=(6, 4))
    #plt.scatter(angles, det_A, label='Data')
    plt.errorbar(x_data, y_data_1, yerr=errors, label='Measured data', fmt = 'none')
    plt.errorbar(x_data, y_data_2, yerr=errors, label='Measured data', fmt = 'none')

    plt.plot(x_sim, y_1, label='Fitted function')
    plt.plot(x_sim, y_2, label='Fitted function')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc='best')
    
    plt.show()

    if ifFindCross:
        diff = np.absolute(y_2 - y_1)
        print(diff)
        min_angle_1 = x_sim[np.argmin(diff[:int(diff.size/2)])]
        min_angle_2 = x_sim[np.argmin(diff)]

        return [min_angle_1, min_angle_2]
    else:
        return None
