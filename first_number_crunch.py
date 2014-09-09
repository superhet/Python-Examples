"""
Created on Fri Jul 18 21:23:08 2014

@author: Alois_W
"""
"""
import numpy as np
x=np.int_(5)
y=np.int_(4)
z=np.int_()
z=x+y
print(z)

#Example for writing into csv

a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
np.savetxt("foo.csv", a, delimiter=",")
"""

#Example of a function call


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function:", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)

print("Done")