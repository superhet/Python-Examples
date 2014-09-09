# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 19:05:23 2014

@author: Alois_W
"""

from tkinter import *
from tkinter.messagebox import *

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()