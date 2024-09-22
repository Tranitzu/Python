# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:21:42 2024

@author: pawel
"""

"""
assertRaises(exception, callable, *args, **kwargs)
    testuje czy błąd zostanie wyrzucony. Test jest zdany, gdy oczekiwanty błąd
    zostanie podniesiony, w przeciwnym razie test jest nie zdany
"""

import unittest


def div(a, b):
    return a / b


class RaiseTest(unittest.TestCase):
    
    def test_raise(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)
    
 
if __name__ == '__main__'    :
    unittest.main()