# -*- coding: utf-8 -*-
#Example of for-loop with variable step size
"""
Created on Tue Sep  9 22:43:32 2014

@author: Alois_W
"""
#Highest reached number is 23
#for i in range(1, 25, 2): 
#    print (i)

step_size=2


for i in range(1, 25, step_size):
    ausgabe=str(i)+"0"+"a"
    print (ausgabe)
input("Press Enter to continue...")
quit()