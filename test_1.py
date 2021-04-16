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
