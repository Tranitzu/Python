# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 23:12:42 2024

@author: pawel
"""

# %%
print(2 + 2)

# %%
print(3 * 3)

# %%
print (3 + 2 * 2)

# %%

10 /3

# %%
# dzielenie bez reszty bez miejsc po przecinku
10 // 3
7 // 6 

# %%
#potęgpwanie
2 ** 5

# %%
# dzielenie modulo (reszta z dzielenia)
10 % 3
12 % 5
11 % 2


# %%
(10 - 2 ** 3) * 10


# %%

a = 10
b = 20

print(a+b)
print(a-b)

# %%
'love python'
"love python"

# %%

'It\'s the best!'

# %%
print('Python 3.12')
print('Python\n3.7')

# %%
print("""Python
3.7""")


# %%
sentence = "I love Python!"

print(sentence)

# %%
print('\tPython')
print('\t\t\tPython')

# %%
print(r'\tHelloWorld')
print(r'c:\tutut\tutu')
# %%
import os
os.getcwd()

# %%


print("""
Instrukcja uruchamiania pliku przyklad.py
      --file [nazwa pliku]
          zapisuje output do pliku
      
      --quiet
          wycisza logi w konsoli
Koniec.
""")

# %%
text  = ' I love Python. '
print(text *3)
print('hau...'*8)
print('-' * 30)

# %%
'Pyhon'
'Py' 'thon'

# %%
url1 = 'https://th.bing.com/th/id/OIP.dJToM1TiZiJA0GYwzDHwjQHaHY?rs=1&pid=ImgDetMain'

url2 = ('https://th.bing.com/th/id/OIP.dJToM1TiZiJA0GY'
        'wzDHwjQHaHY?rs=1&pid=ImgDetMain')

# %%
name = 'Python'
print (name + ' 3.7')
print(name, '3.7')

# %%
age = 27
imie = 'Paweł'

print(imie + ' ma lat ' + str(age))

print(imie, 'ma lat', age)

print('{0} ma {1} lat' . format(imie,age))


# %%
"""
Ćwiczenie 2:
    Wykonaj następujące czynności:

        1. Utwórz zmienną o nazwie name i przypisz do niej łańcuch znaków 'Python'.

        2. Wykorzystując funkcję print(), wydrukuj do konsoli przywitanie 'Cześć, Python', korzystając z wartości zmiennej name.



Aby ułatwić zrozumienie rozwiązania, kod został podzielony na sekcje opatrzone komentarzami.



Oczekiwany wynik:



Cześć, Python

"""

name = 'Python'
print('Czesć ' + name )


# %%
""" 
Ćwiczenie 3
"""

name = 'John'
age = 25
height = 180.5

print(f'My name is {0} and I\'m {1} years old' .format(name, age))
print(f'My height is {height}')

# %%
# Ćwiczenie 4
name = 'Alice'
age = 30
height = 165.5

print(name, age, height, sep='|')

# %%

saldo = 40 
saldo += 30
saldo -= 10
print(saldo)

# %%
lokata = 1000 
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny
print('Wartosc lokaty po roku: ' , lokata_po_roku)

# %%
pixel = 150
pixel /= 255
print(pixel)

# %%
base = 2 
base **= 5
print(base)

# %%
x = 103
x %= 10
print(x)

# %%
imie = 'Pawel '
nazwisko = 'Falis'
imie += nazwisko
print(imie)

# %%
initial_amount = 1000
initial_rate = 0.05
duration  = 2
fv = initial_amount * (1 + initial_rate) ** duration

print(fv)

# %%
radius = 5
PI = 3.14159
circumference = 2 * PI * radius
print(f'The circumference of the circle is {circumference}.')

# %%
imie = input('Podaj swoje imię: ')

print('Czesć {}!' . format(imie))

# %%
jezyk = input('Jakiego języka chcesz się nauczyć? ')
print('Podano język {}' . format(jezyk))

# %%
name = input(' Podaj imię: ')
age = int(input('Podaj wiek: '))
print('Czeć {}! Masz {} lat.' .format(name, age))