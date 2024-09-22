# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:26:38 2024

@author: pawel
"""

def add(x, y):
    """
    Zwraca sumę dwóch liczb.
    
    >>> add(3, 4)
    7
    
    >>> add(2, 8)
    10
    """
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testfile('test.txt')