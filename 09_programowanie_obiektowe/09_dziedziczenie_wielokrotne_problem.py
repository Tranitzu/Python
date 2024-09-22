# -*- coding: utf-8 -*-

class A:
    def metoda(self):
        print('Metoda z klasy A')
      
        
class B(A):
    # def metoda(self):
    #     print('Metoda z klasy B')
    pass
    
        
class C(A):
    # def metoda(self):
    #     print('Metoda z klasy C')
    pass
    
        
class D(B, C):
    # def metoda(self):
    #     print('Metoda z klasy D')
    pass    

        
# %%
d = D()
d.metoda()