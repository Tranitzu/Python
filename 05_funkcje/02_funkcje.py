# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 23:02:18 2024

@author: pawel
"""
# %%
def funkcja_1():
    print('Pierwsza funckja uruchomiona.')
    
funkcja_1()

# %%
def funkcja_2(x, y):
    print(f'Podane argumenty to: {x}, {y}')
    
funkcja_2(2, 4)

# %%

def funkcja_3(x, y=10):
    print(f'Podane argumenty to: {x}, {y}')
    
funkcja_3(y=20, x=5)

# %%
import math


math.sqrt(9)
math.exp(1)
math.sin(0)
dir(math)
# %%

def funkcja_4():
    print('Uruchomiono')

funkcja_4()
print(type(funkcja_4()))

funkcja_4()
fun = funkcja_3()
# %%
def add(x, y):
    return x + y

add(2, 2)

# %%
def substract(x: int, y: int):
    """
    Odejmuje od siebie dwie liczby.
    """
    return x - y

substract(2, 4)

# %%
def print_menu():
    print('Start programu...')
    print('*' * 30)
    print("""Wybierz jedną z podanych opcji:
          0 - logowanie
          1 - wyjscie""")
    print("*" * 30)
    print('Koniec programu.')

print_menu()

# %% Ćwiczenie z kodowania 84: Ćwiczenie 8
def calculate_average(x, y, z):
    return (x + y + z) / 3

# %%
def print_even(maximum):
    even = []
    for i in range(maximum + 1):
        if i % 2 == 0:
            even.append(i)
    return even            
            
print_even(10)
num = print_even(20)

# %%
def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)
    
write_file('sample.txt', 'Pierwsza linia.\nDruga Linia.')
write_file('sample_2.txt', 'Pierwsza.\nDruga.\nTrzecia.')

# %%
def calculate_profit(pv=1000, rate=0.03, n=1):
    return pv * (1 + rate)**n - pv
    
#calculate_profit(1000, 0.20, 15)
calculate_profit(rate=0.40)

# %% Ćwiczenie z kodowania 85: Ćwiczenie 9
def print_odd_numbers(maximum=20):
    odd_numbers = []
    for i in range(maximum + 1 ):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers         

# %% Ćwiczenie z kodowania 86: Ćwiczenie 10
def rectangle_are(x, y):
    return x * y

rectangle_are(2, 4)
rectangle_are(10, 6)    
    
# %% Ćwiczenie z kodowania 87: Ćwiczenie 11   
def is_even(x):
    if x % 2 == 0:
         return True
    else:
         return False
    
# %% Ćwiczenie z kodowania 88: Ćwiczenie 12    
def divisible_by_3_or_5(start, end):
    output = []
    for i in range(start + 1, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append(i)
    return output      

# %%





















    
    
    
    
    
    
    
    
    
    
    
    
    





























