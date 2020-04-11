# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:14:33 2020

@author: Shenghu Sang
"""
# Standard library imports
from __future__ import division

'''
Functions for option pricing, implied volatility, and greek calculation.
All algorithm descriptions are from the book The Complete Guide to Option Pricing Formulas (2006 2nd ed. Haug).
'''
# Generalized Delta Formula (Section 2.1.1 P27):
# IMPORTS


# Related third party imports

import math
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from scipy.stats import norm

# Local application/library specific imports

N = norm.cdf

def GDelta(CallPutFlag, S, X, T, r, b, v):
    '''
    :param S: underlying asset price
    :type S: float
    :param X: strike price
    :type X: float
    :param v: annualized standard deviation, or volatility
    :type v: float
    :param T: time to expiration in years
    :type T: float
    :param r: risk-free interest rate
    :type r: float
    :param b: cost-of-carry rate
    :type b: float
        b = r Black-Scholes 1973 stock option model
        b = r-q Merton 1973 stock option model with contimuous dividend yield q 
        b = 0 Black 1976 futures option model
        b = 0 and r = 0 Asay 1982 margined futures option model
        b = r-r_f Garman and Kohlhagen 1983 currency option model
    
    '''
    d1 = (math.log10(S/X)+(b+v**2/2)*T)/(v*math.sqrt(T))
    # d2 = d1-v*math.sqrt(T)
    
    if CallPutFlag == 'c':
        GDelta = math.exp((b-r)*T)*N(d1)
    else:
        GDelta = math.exp((b-r)*T)*(N(d1)-1)

    return (GDelta)


if __name__ == "__main__":
    S = np.arange(5,205,5)
    K = 100
    T = np.arange(0,1.1,0.1)
    r =0.05
    b = 0.3
    v = 0.25
    
    OptionDelta = np.zeros((len(S),len(T)))
    for i in range(len(S)):
        for j in range(len(T)):
            OptionDelta[i,j] = round(GDelta('c',S[i],K,T[j],r,b,v),4)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    X,Y = np.meshgrid(S,T)
    # zs = np.array(GDelta('c',np.ravel(X),K,np.ravel(Y),r,b,v))
    Z = OptionDelta.reshape(X.shape)
    
    ax.plot_surface(X, Y, Z)
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Surface plot')    
    plt.show()



