# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:35:51 2024

@author: pawel
"""

# %%
def parabola(x):
    return x**2 + 3

print(type(parabola))
parabola(30)

# %%

funkcja_1 = parabola

funkcja_1(30)

# %%
f = lambda x: x**2 +3
f(30)

# %%
f_2 = lambda word: word.upper()

f_2('python')

# %%
f_3 = lambda x, y: x + y
f_3(2, 5)

# %%
f_4 = lambda word_1, word_2: word_1 + ' ' + word_2

f_4('cycki', 'dupa')

# %%

lista = ['python', 'java', 'r', 'sql']

list(map(lambda word: word.upper(), lista))

# %%
def make_upper(word):
    return word.upper()

list(map(make_upper, lista))

# %%
list(map(str.upper, lista))

# %%
lista = ['python', 'java', 'r', 'sql']
list(map(lambda word: word.title(), lista))

# %%
list(map(lambda word: (word, len(word)), lista))

# %%
def apply_function(x, fn):
    return fn(x)

apply_function(5, lambda x: x**2)
apply_function([12, 42], lambda x: sum(x))

# %%
numbers = [6, 3 ,1, 8, 3, 0]

sorted(numbers)

# %%
numbers = [-3, -2, -1, 0, 1, 2, 3]

sorted(numbers, key=lambda x: abs(x))

# %%
lista = [('jeden', 'one'), ('dwa', 'two'), ('trzy', 'three')]

sorted(lista)
sorted(lista, key=lambda x: x[1])

# %% Ćwiczenie z kodowania 89: Ćwiczenie 13
cities = ['Warsaw', 'London', 'Berlin', 'New York']
#list(map(lambda word: word.title(), lista))

first_three_letter = list(map(lambda city: city[:3] , cities))
print(first_three_letter)

# %% Ćwiczenie z kodowania 90: Ćwiczenie 14
def sort_by_lenght(lista):
    return sorted(lista, key=lambda x: len(x))

owoce = ['apple', 'pear', 'banana', 'pineapple', 'orange']
sprzet = ['laptop', 'mouse', 'keyboard', 'screen']

#sorted(owoce, key=lambda x: len(x))
#sorted(sprzet, key=lambda x: len(x))

sort_by_lenght(owoce)



