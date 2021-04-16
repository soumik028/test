# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:12:07 2021

@author: dasso
"""
import time

import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
st.write(screensize)
