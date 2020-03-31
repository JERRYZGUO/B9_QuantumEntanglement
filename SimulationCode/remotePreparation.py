#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:13:39 2020

@author: shirongbao
"""

import numpy as np
from numpy import linalg as LA
from scipy import optimize
import matplotlib.pyplot as plt
from generalFit import generate_seq

def sin(x):
    return np.sin(x/180*np.pi)

def cos(x):
    return np.cos(x/180*np.pi)

def tan(x):
    return sin(x)/cos(x)
def HWP(a):
#    a = 90 + b
    return np.array([[-cos(2*a), -sin(2*a)], [-sin(2*a), cos(2*a)]])

def QWP(a):
    op = np.zeros([2,2], complex)
    op[0,0] = np.complex(sin(a)**2, cos(a)**2)
    op[1,0] = np.complex(sin(a)*cos(a), -sin(a)*cos(a))
    op[0,1] = np.complex(sin(a)*cos(a), -sin(a)*cos(a))
    op[0,0] = np.complex(cos(a)**2, sin(a)**2)

    return op

def PBS():
    return np.array([[1], [0]])

# HWP 1 in angle x with vert
# HWP 2 in angle y with vert
# QWP 2 in angle z with vert
    
def calc_alpha(x, y, z):
    end_state = LA.multi_dot([LA.pinv(QWP(90-z)), LA.pinv(HWP(90 - y)), PBS()])
    
#    print(end_state)
    
    beta = 90 - x
    
#    print(beta)
    
    ang = np.angle((end_state[1,0]/end_state[0, 0])/tan(2*beta))/3.14 * 180

    if ang < 0:
        return ang+360
    else:
        return ang
#print(calc_alpha(22.5, 87, 23))
#
#x_list = [0, 15, 22.5, 45]
#y_list = [40, 78, 87, 16]
#z_list = [292, 8, 23, 246]
#
#for i in range(len(x_list)):
#    print(calc_alpha(x_list[i], y_list[i], z_list[i]))
    

def func(x, Amp, psi):
    H = np.array([[1], [0]])

    initial = np.zeros([4,1], complex)
    initial[0] = 1/(2**0.5)
    initial[3] = np.exp(psi/180 * np.pi * 1j)/(2**0.5)
#    print(x)
#    angle_comb = [0, 292]
#    angle_comb = [45, 246]
#    angle_comb = [22.5, 23]

    HWP_1 = angle_comb[0]
    QWP_2 = angle_comb[1]

    if type(x) == float:
        return np.abs(np.dot(np.kron(np.dot(H.T, HWP(HWP_1 + 2.2)), np.dot(H.T, np.dot(HWP(x + 4.3), QWP(QWP_2)))), initial)) ** 2
    else:
        if x.size > 1:
            y = np.zeros([x.size])
            for i in range(x.size):
                y[i] = Amp * (np.abs(np.dot(np.kron(np.dot(H.T, HWP(HWP_1 + 2.2)), np.dot(H.T, np.dot(HWP(x[i] + 4.3), QWP(QWP_2)))), initial)) ** 2)
            return y
#    else:
#        
#        return Amp * np.abs(np.dot(np.kron(np.dot(H.T, HWP(HWP_1 + 2.2)), np.dot(H.T, np.dot(HWP(x + 4.3), QWP(QWP_2)))), initial)) ** 2
#print(func(0, 0))


#
#x_data = np.array([0.0, 10, 20, 30, 40, 50, 60, 70, 80])
#y_data = np.array([2.98, 2.44, 1.35, 0.43, 0.016, 0.34, 1.21, 2.18, 2.91])

#x_data = np.array([0, 10, 16, 20, 40, 60, 80])
#y_data = np.array([0.6, 0.098, 0.015, 0.049, 1.25, 2.22, 1.39])

x_data = np.array([0, 20, 40, 60, 80, 87])
y_data = np.array([0.08, 1.37, 2.28, 1.41, 0.11, 0.015])


#
#
#errors = np.array([0.1 for i in range(x_data.size)])
#errors[4] = 0.01
#
#params, params_covariance = optimize.curve_fit(func, x_data, y_data, bounds = (0, [100, 180]),
#                                           p0=[6, 50])
#
#print(params)
#
#Amp = params[0]
#psi = params[1]
#
#
#x_sim = generate_seq(np.amin(x_data), np.amax(x_data), x_data.size * 10)
#y_sim = func(x_sim, Amp, psi)
#plt.figure(figsize=(6, 4))
##plt.scatter(angles, det_A, label='Data')
#plt.errorbar(x_data, y_data, yerr=errors, label='Measured data', fmt = 'none')
#plt.plot(x_sim, y_sim, label='Fitted function')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('title')
#plt.legend(loc='best')
#
#plt.show()

#x_sim = generate_seq(np.amin(x_data), np.amax(x_data), x_data.size * 10)
#plt.figure(figsize=(6, 4))
#for psi in range(0, 180, 10):
#    y_sim = func(x_sim, 1, psi)
#
#    #plt.scatter(angles, det_A, label='Data')
#    plt.plot(x_sim, y_sim, label= 'phase = ' + str(psi))
#plt.xlabel('HWP2 angle')
#plt.ylabel('Coincidence')
#plt.title('Simulation for coincidence vs HWP2 angle')
#plt.legend(loc='best')
#
#plt.show()



x_sim = generate_seq(np.amin(x_data), np.amax(x_data), x_data.size * 10)
plt.figure(figsize=(6, 4))
#plt.scatter(angles, det_A, label='Data')
plt.errorbar(x_data, y_data, yerr=errors, label='Measured data', fmt = 'none')
plt.xlabel('HWP2 angle')
plt.ylabel('Coincidence')
plt.title('Measured data for coincidence vs HWP2 angle')
plt.legend(loc='best')

plt.show()


