# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:46:38 2024

@author: pawel
"""

empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'Usa', 'Technology', 2)

# %%
name_google = google[0]

# %%
data = (amazon, google)
print(data)

# %%
a = ('Paweł', 'Falis')
print(a)

# %%

imie = 'Paweł'
nazwisko = 'Krakowiak'

# %%
imie, nazwisko, id_user = ('Paweł', 'Falis', '001')

# %%
amazon_name, country, sector, rank = amazon

# %%
stocks = 'Amazon', 'Apple', 'IBM'

print(type(stocks))

# %%
nested = 'Europa', 'Polska', ('Warszawa','Kraków', 'Wroclaw')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c
print(a, b)

# %%
x, y, = 10, 15

x, y = y, x
print(x, y)

# %%
fruits = ('apple', 'banana', 'cherry', 'banana', 'banana')

fruits_count = fruits.count('banana')
print('Number of bananas:', fruits_count)

# %%
fruits = ('apple', 'banana', 'cherry')
fruit1 = fruits[0]
fruit2 = fruits[1]
fruit3 = fruits[2]
print('Tupple', fruits)
print('Fruit 1: ', fruit1)
print('Fruit 2: ', fruit2)
print('Fruit 3: ', fruit3)

# %%
# to samo prostsza wersja
fruits = ('apple', 'banana', 'cherry')
fruit1, fruit2, fruit3 = fruits
print('Tuple:', fruits)
print('Fruit 1: ', fruit1)
print('Fruit 2: ', fruit2)
print('Fruit 3: ', fruit3)