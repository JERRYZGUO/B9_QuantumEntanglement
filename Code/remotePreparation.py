#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:13:39 2020

@author: shirongbao
"""

import numpy as np
from numpy import linalg as LA


def sin(x):
    return np.sin(x/180*np.pi)

def cos(x):
    return np.cos(x/180*np.pi)

def tan(x):
    return sin(x)/cos(x)
def HWP(a):
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

x_list = [0, 15, 22.5, 45]
y_list = [40, 78, 87, 16]
z_list = [292, 8, 23, 246]

for i in range(len(x_list)):
    print(calc_alpha(x_list[i], y_list[i], z_list[i]))





