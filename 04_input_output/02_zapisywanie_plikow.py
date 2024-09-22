# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:25:39 2024

@author: pawel
"""

# %%
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)
        
# %%
even_number = list(range(100))[::2]

with open('numbers.txt', 'w') as file:
    for number in even_number:
        file.write(str(number) + '\n')
        
# %%
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'a') as file:
    for tech in techs:
        print(tech, file=file)

# %%

technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line)
        
print(technologies)

# %%

technologies = []
with open('App Project CRM funcion and database by Falis.csv', 'r') as file:
    for line in file:
        technologies.append(line[:-1])
        
print(technologies)

# %% Ćwiczenie z kodowania 73: Ćwiczenie 7
techs = ['python', 'java', 'sql', 'sas']

with open('techs.txt', 'w') as file:
    for tech in techs:
        file.write(str(tech) + '\n')

# %% Ćwiczenie z kodowania 74: Ćwiczenie 8

products = [
    {'name': 'T-shirt', 'price': 29.99},
    {'name': 'Shoes', 'price': 99.99},
    {'name': 'Pants', 'price': 49.99},
]

with open('products.txt', 'w') as file:
    
    for product in products:
        file.write(str(product['name'] + ',' + str(product['price']) + '\n'))

# %%
with open('tree.txt', 'w') as file:
    for j in range(2):
        for i in range(10):
             file.write(('{:>9}'.format('*' * i)) + ('*' * i) + '\n')

# %% Ćwiczenie z kodowowania 75: Ćwiczenie 19
stock_data = {
    'AAPL': 145.9,
    'GOOG': 2680.7,
    'TSLA': 712.6,
    'AMZN': 3379.1
}

with open('stock_prices.txt', 'w') as file:
    for stocks, wartosc in stock_data.items():
        file.write(f'{stocks};{wartosc}\n')
   

# %% Ćwiczenie z kodowania 76: Ćwiczenie 19

first_name = 'Jan'
last_name = 'Kowalski'
weight = 75.5
height = 1.85
date_of_birth = '1990-01-01'
chronic_conditions = ['hypertension', 'diabetes']
medications = {
    'hypertension_medications': ['enalapril', 'hydrochlorothiazide'],
    'diabetes_medications': ['metformin'],
}

with open('patient_data.txt', 'w') as file:
    file.write(f'First name: {first_name}\n')
    file.write(f'Last name: {last_name}\n')
    file.write(f'Weight: {weight}\n')
    file.write(f'Height: {height}\n')
    file.write(f'Date of birth: {date_of_birth}\n')
    file.write(f'Chronic_conditions: {', '.join(chronic_conditions)}\n')
    for key, value in medications.items():
        formatted_key = key.replace('_', ' ').capitalize()
        formatted_value = ', '.join(value)
        file.write(f'{formatted_key}: {formatted_value}\n')
























        
    