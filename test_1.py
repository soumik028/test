# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:12:07 2021

@author: dasso
"""
import time
import win32gui, win32con

time.sleep(2)
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)



import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
st.write(screensize)
