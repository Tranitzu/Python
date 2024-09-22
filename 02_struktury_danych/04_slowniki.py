# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:51:13 2024

@author: pawel
"""

empty_dict = dict()
print(empty_dict)

d = {}
type(d)

e = set()

# %%
pol_to_eng = {'jeden' : 'one', 'dwa' : 'two', 'trzy' : 'three'}

name_to_digit = {'jeden' : 1, 'dwa' : 2, 'trzy' : 3}

len(name_to_digit)


# %%
# dict = {'key1' : 'value1', 'key2' : 'value2'}

# %%
pol_to_eng['cztery'] = 'four'

# %%
pol_to_eng.clear()

# %%
pol_to_eng_copied = pol_to_eng.copy()

# %%
list(pol_to_eng.keys())
list(pol_to_eng.values())

# %%
list(pol_to_eng.items())

# %%
pol_to_eng['jeden']
# pol_to_eng['zero']
pol_to_eng.get('jeden', 'NaN' )
pol_to_eng.get('zero', 'NaN' )

# %%
# pol_to_eng.pop('dwa')
pol_to_eng.popitem()

# %%
pol_to_eng.update({'dwa' : 2})

# %%
countries_capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Czechy': 'Praga',
}
countries_capitals['Włochy'] = 'Rzym'

countries_capitals_sorted = sorted(list(countries_capitals.values()))
print(countries_capitals_sorted)

# %%
fruits = {'apple': 2, 'banana': 3, 'cherry': 5, 'orange': 1}
# Enter your solution here
print('Dictionary: ',fruits)
fruits['kiwi'] = 4
print('After adding: ',fruits)
del fruits['orange']
print('After deleting: ',fruits)
print('Keys:', fruits.keys())
print('Values:', fruits.values())

# %%
fruits = {'apple': 2, 'banana': 3}
print('Dictionary before update:', fruits)
fruits.update({'apple' : 4})
print('Dictionary after update:', fruits)
fruits['kiwi'] = 1
print('Dictionary after adding:', fruits)

fruits2 = {
    'orange' : 3,
    'peach' : 2,
    }
fruits.update(fruits2)
print('Dictionary after merging: ', fruits)

# %%
"""
Ćwiczenie 22
Podany jest poniższy słownik:

people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}

Napisz program, który wykorzystując odpowiednią metodę usuwa wpis ze słownika o kluczu
 'Bob' i zwraca wartość usuniętego wpisu. W odpowiedzi wydrukuj otrzymaną wartość
 oraz pozostały słownik people tak jak pokazano poniżej.
"""
people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}
age_of_Bob = people.pop('Bob')
print(age_of_Bob)
print(people) 
# %%
"""
Ćwiczenie 23
Podany jest poniższy słownik:

people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}

Napisz program, który wykorzystując odpowiednią metodę umożliwia dodanie 
nowego wpisu do słownika, jeśli klucz nie istnieje, lub zwraca wartości 
związaną z kluczem, jeśli klucz już istnieje w słowniku i dodaj w ten sposób 
parę o kluczu 'Emma' i wartości 20 do słownika people.

W odpowiedzi wydrukuj otrzymaną wartość po dodaniu wpisu oraz słownik people
 do konsoli tak jak pokazano poniżej.
"""
people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}

imie = input('Podaj imie: ')
wiek = input('Podaj wiek: ')
people[imie] = wiek
