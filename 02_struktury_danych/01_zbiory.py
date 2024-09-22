# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:51:39 2024

@author: pawel
"""

empty_set = set()
print(empty_set)
print(type(empty_set))

# %%

techs = {'python', 'java', 'c++', 'sql'}

print(techs)
print(type(techs))
print(len(techs))

# %%
set('python')
set('aaaaaale')

# %%
'python' in techs
'go' in techs

# %%
print(dir(set))

# %%
techs.add('sas')

# %%
print(techs)

# %%
techs.remove('sas')
print(techs)

# %%
techs.pop()

# %%

techs.clear()

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

C.issubset(A)
C.issubset({5, 7})
A.issuperset(C)
A.union(B)
A.intersection(B)
A.symmetric_difference(B)

D = A.copy()

# %%
# Ćwiczenie 1

string = 'Programowanie w języku Python - od A do Z'
string = string.lower()
string = string.replace('-', '')
string = string.replace(' ', '')
string = string.replace('ę', 'e')
unique_characters_count = len(set(string))
print(unique_characters_count)

# %%
# Ćwiczenie 2

set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])
print('Union set:', set1.union(set2))
print('Intersection set:', set1.intersection(set2))
print('Difference set:', set1.difference(set2))
print('Symmetric difference set:', set1.symmetric_difference(set2))

# %%
# Ćwiczenie 3

list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print('List with duplicates:', list1)
print('List without duplicates:', set(list1))

# %%
# Ćwiczenie 4

set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

print('Union set without duplicates:', set1.union(set2))