# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:57:45 2020

@author: sortiz
"""

import webbrowser

from tkinter import *

root = Tk()

root.title("web browser")
root.geometry("300x200")
def copyasignment():
    webbrowser.open("www.copyassignment.com")
    
def google():
    webbrowser.open("www.google.com")
    
copyasignment = Button(root, text="visit copyassignment",command=copyasignment).pack(pady=20)
mygoogle = Button(root, text="open Google",command=google).pack(pady=20)
root.mainloop()