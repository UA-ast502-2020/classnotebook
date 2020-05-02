#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import numpy as np
#np.set_printoptions(threshold=np.inf)

try:
    bin=int(sys.argv[1])
except:
    bin=1
    
RAD=180./3.1415926
D=1.E7/1066

ALP=(9.22+.032)/RAD
ALP=ALP+3.46465e-5 # 11-1-99 ADJUSTMENT
BET=(np.arange(1024)-511.5)*.025*.99815/300.
BET=np.arctan(BET)+.032/RAD+3.46465e-5  # 11-1-99 ADJUSTMENT
LAM=D*(np.sin(ALP)+np.sin(BET))

e_wavelength=LAM

# if bin !=1:
    # e_wavelength=np.zeros(1024/bin) #make floating array of all zeroes
    # for k in range(len(e_wavelength)):
        # e_wavelength[k]=sum(LAM[k*bin:(k+1)*bin-1])/bin

#print 'F_wavelengths', e_wavelength

"""
Created on Wed Jan 23 15:53:20 2019

@author: mypalmer
"""

