# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:01:38 2024

@author: pawel
"""

class Student:
    
    lista_studentow = []
    
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_studentow.append(self)
    
    @classmethod    
    def liczba_studentow(cls):
        print(len(Student.lista_studentow))
        
# %%
student_1 = Student('Jan', 'Kowalski', 18)        
student_2 = Student('Tomasz', 'Nowak', 23)

# %%
Student.liczba_studentow()