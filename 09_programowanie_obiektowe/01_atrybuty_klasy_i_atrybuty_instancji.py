# -*- coding: utf-8 -*-

class Drzewo:
    
    nazwa = 'Sosna'
    wiek = 40
    wysokosc = 25
    
drzewo_1 = Drzewo()
drzewo_2 = Drzewo()

# %%
print(id(drzewo_1))
print(id(drzewo_2))

# %%
dir(drzewo_1)

# %%
print(drzewo_1.nazwa)
print(drzewo_1.wiek)
print(drzewo_1.wysokosc)

# %%
print(drzewo_2.nazwa)
print(drzewo_2.wiek)
print(drzewo_2.wysokosc)

# %%
drzewo_1.stan = 'dobry'

print(dir(drzewo_1))

# %%
Drzewo.miejsce = 'las'

# %%
#print(dir(drzewo_2))
#print(drzewo_2.miejsce)

drzewo_2.miejsce = 'park'

print(drzewo_2.miejsce)





















