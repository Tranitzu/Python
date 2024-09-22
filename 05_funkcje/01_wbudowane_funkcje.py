# -*- coding: utf-8 -*-

# abs()
# bool()
# dir()
# enumerate()
# eval()
# filter()

# %%
number = 5
string = 'Hello, world!'
values = [5, 2, 8, 1, 9, 3]

# Enter your solution here
if isinstance(number, int):
    print('The number is of type int.')
    
if isinstance(string, str):
    print('The string is of type str')

if isinstance(values, list):
    print('The object is of type list')

# %%

x = 5
y = 3

expression1 = '2 * 3 + 5'
expression2 = 'x + y'
expression3 = 'max([5, 2, 8, 1, 9, 3])'



print(f'The result of the expression1 is: {eval(expression1)}')
print(f'The result of the expressionq is: {eval(expression2)}')
print(f'The maximum value in the list is: {eval(expression3)}')

# %%

# 1 2 3 4 5 6 7 8 9 
# 0 2 4 6 8 
# 100 90 80 70 60 50 40 30 20 10 

for i in range(1, 10):
    print(i, end = " ")

print()

for i in range(0, 10, 2):
    print(i, end = " ")
    
print()

for i in reversed(range(10, 110, 10)):
    print(i, end = " ")
    
# %%

# Używając funkcji wbudowanej map() dokonaj konwersji 
# elementów listy na typ int. Otrzymaną listę wydrukuj do konsoli.



# Oczekiwany wynik:



# [5, 2, 8, 1, 9, 3]

values = ['5', '2', '8', '1', '9', '3']

int_values = list(map(int, values))

print(int_values)

































