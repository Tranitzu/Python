# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:28:25 2024

@author: pawel
"""

empty_list = list()
print(empty_list)

# %%
techs = ['python', 'java', 'c++', 'go', 'sql']
techs[0] = 'python 3.7'
print(techs)

# %%
numbers =  [3, 5, 3, 5, 23]
print(numbers)
print(type(numbers))


# %%
mixed = ['python', 3.7, 5, True]
print(mixed)

# %%
empty = []
nested = [[1, 2, [3, 'sql']], ['python', 'java', 'go'], 3]

# %%
first = ['mleko', 'ziemniaki', 'makaron']
second = ['woda', 'jajka']
bucket = [first, second]

# %%
len(bucket)

# %%
techs = first + second + ['scala']

# %%
techs = ['python', 'java', 'c++', 'go', 'sql']

techs += ['javastript']
print(techs)

# %%
print(dir(list))

# %%
# Ćwiczenie 9

numbers = [ 1, 4, 2, 5]
letters = ['d', 's', 't']
wynik = numbers + letters
print(wynik)

# %%
fruits = [['apple', 'banana'], ['cherry', 'orange'], ['kiwi', 'melon']]
print('Nested list:', fruits)
print('First item of second nested list:', fruits[1][0])

# %%
# wycinanie
index = [0,   1,  2,  3,  4,  5]
idx_n = [-6, -5, -4, -3, -2, -1]
lista = [34, 23, 56, 24, 23, 76]
# lista[start:stop]
# lista[index]
# lista[start:]
# lista[:stop]
# lista[::step]

lista[0]
lista[1]
lista[-1]
lista[-3]

lista[1:5]
lista[-5:-1]
lista[::-1]

lista[:4]
lista[3:]

# %%
# Ćwiczenie 11
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
 
print('List:', fruits)
print('Slice 1:', fruits[1:3])
print('Slice 2:', fruits[:3])
print('Slice 3:', fruits[3:])
print('Slice 4:', fruits[1:5:2])

# %%
#Ćwiczenie 12

fruits = [
    ['apple', 'banana', 'cherry'],
    ['orange', 'kiwi', 'melon'],
    ['grape', 'pear', 'plum'],
]
print('Last item of first nested list:', fruits[0][2])
print("First two items of second tested list:", fruits[1][:2])
print('Last two items of third nested list:', fruits[2][1:])

# %%
# metody
techs = []
print(techs)

techs.append('python')
print(techs)
techs.append('java')
techs.append('java')

# %%

techs.append(['hadoop', 'spark'])
print(techs)

# %%
techs.extend(['sql','sas'])
print(techs)

# %%
techs.insert(0, 'go')
print(techs)

techs.insert(2, 'r')
print(techs)

# %%
print(techs)
techs.pop()
print(techs)

# %%
techs = [ 'python', 'java', 'sq', 'php']
print(techs)
techs.pop(0)
print(techs)

# %%
techs = [ 'python', 'java', 'sq', 'php']
techs.index('java')
print(techs.index('java'))

# %%
techs = [ 'python', 'java', 'sq', 'php', 'python']
techs.count('python')
techs.count('java')
techs.count('jav')

# %%
techs = [ 'python', 'java', 'sq', 'php', 'r']
techs.sort()
print(techs)
techs.sort(reverse=True)
print(techs)

# %%
techs = [ 'python', 'java', 'sq', 'php']
techs.reverse()
print(techs)

# %%
techs = [ 'python', 'java', 'sq', 'php']
techs[1] = 'c++'
print(techs)