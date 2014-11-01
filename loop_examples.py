# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 10:37:13 2014

@author: Alois_W
"""
import numpy as np
##########################
#Bias Values Parameter #############
##########################
#Sart Value for Bias Measurement
Bias_low_Value=0
Bias_high_Value=2
#Step size for loop use . for comma
#Example: 0.2 eq 0,2A eq 200mA
#Smallest availabel is 0.05
Bias_Step=0.2

#Support Values
#Bias actual value
actual_bias_value=0


#While Version

while actual_bias_value<= Bias_high_Value:
    actual_bias_value=actual_bias_value+Bias_Step
    #This step is necessary because some times a lot of decimals appear
    #Limit decimal places
    actual_bias_value=np.around(actual_bias_value, decimals=4);
    print(actual_bias_value)
    #Convert to str
    #actual_bias_value='%d'.format(actual_bias_value)
    #for debugging check output after formating
    print(actual_bias_value)
    

#For loop version
#Does not work because float values are not allowed in this Version
#==============================================================================
# 
# for i in range(Bias_low_Value,Bias_high_Value, Bias_Step):
#     print (i)    
#==============================================================================
