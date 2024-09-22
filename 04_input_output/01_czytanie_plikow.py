# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:55:50 2024

@author: pawel
"""

file = open('simple.txt', 'r')

for line in file:
    print(line, end='')
    
file.close()

# %%
with open('simple.txt', 'r') as file:
    for line in file:
        print(line, end='')
        
# %%
with open('data.txt', 'r') as notowania:
    for line in notowania:
        print(line, end='')

# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)
    
# %% 
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# %% 
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
    
# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()
        
# %%
with open('simple.txt', 'r') as file:
    lines = file.read()
    print(lines)
    
# %% Ćwiczenie z kodowania 71: Ćwiczenie 5
with open('data.txt', 'r') as data:
    dane = data.readlines()
    pairs = [dane1.strip().split(',') for dane1 in dane]
    generate_power = 0
    for power in pairs:
       if power[0] is None:
           break
       generate_power += float(power[1])
generate_power = round(generate_power, 3)
print(f'Total power generated: {generate_power:.2f} MW')

# %% Ćwiczenie z kodowania 72: Ćwiczenie 6
with open('data.csv', 'r') as f:
    dane = f.readlines()
    dane_podzielone = [dane1.strip().split(',') for dane1 in dane]
    del dane_podzielone[0]
    wygenerowana_energia = 0
    count = len(dane_podzielone)
    for power in dane_podzielone:
        if power[0] is None:
            break
        wygenerowana_energia += float(power[2])

average_production = wygenerowana_energia / count
print(f'Average energy generated: {average_production:.2f} kWh')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    