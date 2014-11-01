# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 22:00:21 2014

@author: Alois_W
"""
import numpy as np

trailingremoved = []
#Set Precision

#Put in start frequency [Hz]
start_frequency=10000;
stop_frequency=11001;
divider=20;

raw_values=np.logspace(start_frequency, stop_frequency, num=divider);
#Elimniate decimal places
without_decimals=np.around(raw_values, decimals=0);
#Remove duplicates
unique_values=np.unique(without_decimals);
#Length of array
Length=len(unique_values);

for x in range(0, Length):
    #Set Precision
    t="{:.5E}".format(unique_values[x])
    #Remove Trailing Zeros
    while t[-1] == "0":
        t = t[:-1]
    trailingremoved.append(t)
    print(t)
#c='{:2E}'.format()
#print(c)