# -*- coding: utf-8 -*-

class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'Jack'
    
class Polak:
    
    kraj = 'Polska'
    imie = 'Piotr'
    
class Pilkarz(Czlowiek, Polak):
    
    def info(self):
        print(f'Utworzony obiekt pochodzi z planety {self.pochodzenie}.\n'
              f'Kraj Pochodznie: {self.kraj}.\n'
              f'Nazwa obiektu: {self.imie}')


# %%
pilkarz_1 =  Pilkarz()        
pilkarz_1.info()
