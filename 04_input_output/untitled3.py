# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:53:49 2024

@author: pawel
"""

with open('data.txt', 'r') as data:
    dane = data.readlines()
    pairs = [dane1.strip().split(',') for dane1 in dane]
   # tablica = {key: {float(value)} for key, value in pairs}
    power = pairs