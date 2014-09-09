# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 19:05:23 2014

@author: Alois_W
"""

from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        self.stat_msg1 = Button(frame, text="Stat1", fg="blue", command=self.say_msg1)
        self.stat_msg1.pack(side=LEFT)
        
        self.stat_msg2 = Button(frame, text="Stat2", fg="green", command=self.say_msg2)
        self.stat_msg2.pack(side=LEFT)

    def say_hi(self):
        print ("Status Message 3")
        
    def say_msg1(self):
        print ("Status Message 1")
    
    def say_msg2(self):
        print ("Status Message 2")

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below