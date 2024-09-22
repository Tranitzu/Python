# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:02:15 2024

@author: pawel
"""
# %%
i = 0
while i < 5:
    print(i)
    i += 1
    
# %%
n = 0
while True:
    print(n)
    if n >= 10:
        break
    n += 1

# %%
while True:
    name = input('Podaj swoję imie: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Czeć {}'.format(name))

# %%
n = 0
while n < 20:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
    
# %%
n = 0
while n < 20:
    n = n + 1
    if n % 2 != 0:
        continue
    print(n)
    
# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False

idx = 0
while idx < len(lista_do_przeszukania):
    print(lista_do_przeszukania[idx])
    idx += 1

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 80

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('Znaleziono element {}'.format(wartosc))
else:
    print('Nie znaleziono elementu {}'.format(wartosc))

# %%

lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 124

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if not flaga:
    lista_do_przeszukania.append(wartosc)

# %% Ćwiczenie z kodowania 64: Ćwiczenie 27
proportions = {
    'flour': 500,
    'salt': 4,
    'sugar': 200,
    'butter': 150
}

amount_of_dought = 3000
counter = 0

ingredients = {}

while counter < amount_of_dought:
    for key, value in proportions.items():
        if key not in ingredients:
            ingredients[key] = value
        else:
            ingredients[key] += value
        counter += value
print('To prepare', amount_of_dought,'g of dough, you need:')
for key, value in ingredients.items():
    print(f'{key.capitalize()} - {value} g' )

# %%
KOD_PIN = '0000'
pin = input('Podaj kod pin: ')

while pin != KOD_PIN:
    pin = input('Spróbuj ponownie jeszcze raz: ')
print('Zalogowany')

# %%
KOD_PIN = '0000'
pin = ''
counter = 0
while pin != KOD_PIN and counter < 3:
    pin = input('Wprowadź kod pin: ')
    if pin == KOD_PIN:
        print('Zalogowany')
        break
    counter +=1
else:
    print('Zbyt dużo prób logowania.')

# %% Ćwiczenie z kodowania 65: Ćwiczenie 28
fuel = 100
fuel_consumption_rate = 10
time = 0

print('Fuel remainig:', fuel, 'units.')
while fuel > 0:
    if fuel > 0:
        print('Fuel remainig:', fuel, 'units.')
        time += 1
        fuel = fuel - fuel_consumption_rate
print('End of flight')

# %% Ćwiczenie z kodowania 66: Ćwiczenie 29

hour = 8
solar_power = 50
battery_capacity = 500
battery_level = 0

while battery_level < battery_capacity and hour < 15:
    battery_level += solar_power
    hour += 1
    
print(f'The solar battery charge level is: {battery_level} Watt-hours')

    
    
    
    
    
    
    
    
    
    
    
    
    
