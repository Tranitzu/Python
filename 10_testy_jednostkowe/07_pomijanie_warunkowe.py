# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:05:48 2024

@author: pawel
"""

"""
Opis metod:
    
    unittest.skip(reason)
        pomija oznaczony test
        
    unittest.skipIf(condition, reason)
        pomija oznaczonyu test jeżeli warunek jest prawdziwy
        
    unittest.skipUnless(condition, reason)
        pomija oznaczony test, chyba, że warunek jest prawdziwy
        
    unittest.expectedFailure()
        oznacza test jako oczekiwany błąd, jeżeli test będzie niepowodzeniem
        nie zostanie policzony jako błąd
"""
import unittest

class SimpleTest(unittest.TestCase):
    
    x = 6
    y = 8
    
    @unittest.skip('Pomiń')
    def test_add(self):
        wynik = self.x + self.y
        self.assertEqual(wynik, 8)
    
    @unittest.skipIf(x < y, 'Pomiń')
    def test_sub(self):
        wynik = self.x - self.y
        self.assertEqual(wynik, 4)
    
    @unittest.skipUnless(y == 0, 'Pomiń')
    def test_div(self):
        wynik = self.x / self.y
        self.assertEqual(wynik, 3.0)
    
    @unittest.expectedFailure
    def test_mul(self):
        wynik = self.x * self.y
        self.assertEqual(wynik, 10)
        
        
if __name__ == '__main__':
    unittest.main()
