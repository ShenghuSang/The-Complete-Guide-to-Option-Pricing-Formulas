# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:15:26 2020

@author: Shenghu Sang
"""

'''
Functions for option pricing, implied volatility, and greek calculation.
All algorithm descriptions are from the book The Complete Guide to Option Pricing Formulas (2006 2nd ed. Haug).
'''

# Generalized Black-Scholes-Merton Option Prcing Model (Section 1.1.6 P8):
# IMPORTS

# Standard library imports
from __future__ import division

# Related third party imports

import math
from scipy.stats import norm

# Local application/library specific imports

N = norm.cdf

def GBlackScholes(CallPutFlag, S, X, T, r, b, v):
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
    d2 = d1-v*math.sqrt(T)
    
    if CallPutFlag == 'c':
        GBlackScholes = S*math.exp((b-r)*T)*N(d1)-X*math.exp(-r*T)*N(d2)
        return(GBlackScholes)
    else:
        GBlackScholes = -S*math.exp((b-r)*T)*N(-d1)+X*math.exp(-r*T)*N(-d2)
        return(GBlackScholes)


if __name__ == "__main__":
    OptionPrice = round(GBlackScholes('p',75,70,0.5,0.1,0.05,0.35),4)
    print(OptionPrice)
