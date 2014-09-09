# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 22:05:26 2014
 basic structure for remote controlling the Wayne Kerr
@author: Alois_W
"""
#Import necessary things and setup variables
import numpy as np
from init_instrument import init
debug_status=np.int_()
      
# Start the Process by intializing the instrument
  
debug_status =init;
print ("Return status: ", debug_status )
