# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:03:12 2024

@author: pawel
"""

def test_args(x, *args):
    print('Pierwszy parametr:', x)
    for arg in args:
        print('Kolejny parametr *args:', arg)
        
test_args(4, 3, 4, 5, 6, 7, 8, 9, 10)

# %%
def funkcja_1(x, y, *args):
    print('x=', x)
    print('y=', y)
    print('*args=', args)
    
funkcja_1(1, 2, 3)
funkcja_1(1, 2, 3, 4)

# %%
def suma(x, y):
    return x + y

def suma_dowol(*args):
    return sum(args)

# %%
suma(1, 2)  
suma_dowol(1, 1, 1, 1, 1, 1, 1,)

# %%

def calculate_average(*args):
    suma = sum(args)
    return suma / len(args)

calculate_average(1, 1, 1,)

# %%
def multiply(*args):
    if len(args) == 0:
        return None
    i = 1
    for arg in args:
        i *= arg
    return i

multiply(2, 2, 2, 2, 2)

# %%
def join_string(*words):
    return ' '.join(words)
    
join_string('cycki', 'dupa')





















    
    