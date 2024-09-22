# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:05:03 2024

@author: pawel
"""
# %%
version = 3.7

print(version)

# %%
version > 3
version <= 3

# %%
number = 1200
number > 1000

number == 1200
number == 1000

number != 1200
number != 1000

# %%
"""
if [warunek]:
    [instrukcje]
"""    

# %%
if 8 < 10:
    print('Tak')

if 8 > 10:
    print('Tak')

# %%
a = 15
if a > 10:
    print('a > 10')

# %%
a = 10
if a > 115:
    print('a > 10')
else:
    print('a <= 10')

# %%
age = 18
if age < 18:
    print('Nie masz uprawnień. ')
else:
    print('Dostęp przyznany. ')
    
# %%
age = 18

if age == 18:
    print('Masz 18 lat. ')
elif age < 18:
    print('Nie masz uprawnień')
else:
    print('Dostęp przyznany. ')

# %%
age = int(input('Podaj swój wiek: '))

if age == 18:
    print('Masz 18 lat. ')
elif age < 18:
    print('Nie masz uprawnień')
else:
    print('Dostęp przyznany. ')

# %%

print('Program uruchomion...')
print("""Włam się dy systemu, zgadjując dwucyfrowy pin.
Numer pin składa się z cyfr: 0, 1, 2.""")

pin = input('Wprowadź numer pin: ')

if pin == '21':
    print('Brawo! Złamałes system. ')
elif pin == '20':
    print('Byłe blisko!')
else:
    print('Nie zgadłes.')

# %%

print('Program uruchomion...')
print("""Włam się dy systemu, zgadjując dwucyfrowy pin.
Numer pin składa się z cyfr: 0, 1, 2.""")

pin = int(input('Wprowadź numer pin: '))

if pin == 21:
    print('Brawo! Złamałes system. ')
elif pin == 20:
    print('Byłe blisko!')
else:
    print('Nie zgadłes.')

# %%
string = '1'

if string:
    print('Nie pusty ciąg znaków')
else:
    print('Pusty ciąg znaków')
    
# %%
number = 12

if number:
    print('Liczba niezerowa')
else:
    print('Zerrro!!')

# %%
default_flag = False


if default_flag:
    print('Doszło do defaultu.')
else:
    print('Nie doszło')    

# %%
default_flag = True


if not default_flag:
    print('Doszło do defaultu.')
else:
    print('Nie doszło')        
    
# %%
category = 'electronics'
price = 2000

# Enter your solution here
if category == 'electronics':
    if price > 1000:
        vat = price * 0.23
        print('The VAT for a product is ', vat)
    else:
        vat = price * 0.08
        print('The VAT for a product is ', vat)
elif category == 'clothing':
    vat = price * 0.23
    print('The VAT for a product is ', vat)
else:
    vat = price * 0.21
    print('The VAT for a product is ', vat)
    
# %%
saldo = 10000
klient_zweryfikowany = True

if saldo > 0 and klient_zweryfikowany:
    print('Możesz wypłacić gotówkę.')
else:
    print('Nie możesz wypłącić gotówki.')

# %%
saldo = 10000
klient_zweryfikowany = True
amount =int(input('Ile chcesz wypłacić gotówki: '))
if saldo > 0 and klient_zweryfikowany and (saldo - amount) >= 0:
    print('Możesz wypłacić gotówkę.')
else:
    print('Nie możesz wypłacić gotówki. \
Brak wystarczającej kwoty {}'.format(abs(saldo - amount)))

# %%
fact = 'Python is easy and enjoyable'
# Enter your solution here
unique_character = set(fact)
number_of_unique_character = len(unique_character)
if number_of_unique_character < 20:
    print('There are less than 20 unique characters.')
else:
    print('The number of unique characters is greater than or equal to 20.')
    

# %%

name = 'python'

if 'p' in name:
    print('Znaleziono p')
else:
    print('Nie znaleziono p')
    
# %%

tech = 'python'

if tech == 'python':
    flag = 'Dobry wybór'
else:
    flag = 'Poszukaj czego lepszego.'


# %%
# x if [warunek] else y
tech = 'python'
'Dobry wybór' if tech == 'python' else 'Poszukaj czego lepszego'

# %%
text = 'sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx'

contains = set(text)

print('The text contains the letter "q".') if 'q' in contains else print('The text \
does not contain the letter "q".')

# %%
height = 1.85
weight = 85

bmi = round(weight / (height ** 2), 2)
print('The patient\'s BMI is:', bmi)

if bmi < 18.5:
    print('Underweight')
elif bmi >= 18.5 and bmi < 25:
    print('Normal weight')
else:
    print('Obese')

# %%

password = 'my_password_123'
passwd_test = set(password)
passwd_lenght = len(passwd_test)
contains_digit = any(char.isdigit() for char in password)
contains_upper = any(char.isupper() for char in password)
contains_lower = any(char.islower() for char in password)
if passwd_lenght > 8 and contains_digit and contains_upper and contains_lower:
    print('The password is complex enough.')
elif passwd_lenght < 8:
    print('The password is too short.')
elif contains_digit == False:
    print('The password must contain at least one digit.')
elif contains_upper == False:
    print('The password must contain at least one uppercase letter.')
elif contains_lower == False:
    print('The password must contain at least one lowercase letter.')
    
# %% pętle
lista = [1, 2, 3, 4, 5]
for liczba in lista:
    print(liczba)
    
slownik = {"imie": "Jan", "wiek": 30, "miasto": "Warszawa"}
for klucz in slownik:
    print(klucz)
    
for i in range(5):  # Iteracja od 0 do 4
    print(i)

# %%
for i in 'python':
    print(i)

# %%
name ='sas'
index = 0 
for character in name:
    print(index, character)
    index = index + 1

# %%
for index in range(10):
    print(index)
    
# %%
name = 'python'
for index in range(len(name)):
    print('Nr indeksu: ', index, 'Litera: ',  name[index])

# %%
for i in enumerate(name):
    print(i)

for indeks, character in enumerate(name):
    print(indeks, character)

# %%
for i in [4, 5, 6, 8, 6]:
    print(i)

# %%
for i, value in [4, 5, 6, 8, 6]:
    print(i, value)

# %%
for i in range(10, 20):
    print(i)

# %%
for i in range(10, 20, 2):
    print(i)
# %%
for i in range(10, -1, -1):
    print(i)

# %%
for i in range(10, 100, 10):
    print(i)

# %%
techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])

# %%
string = 'Python Course'
for char in string[0:6]:
    print(char)
    
# %%
string = 'Python Course'
for char in string[::-1]:
    print(char)

# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    print(char)

# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)

# %%
for char in zip('abcde', '12345'):
    print(char)

# %%
for char, number in zip('abc', 'python'):
    print(char, number)    

# %%
hashtags = '#sport#gym#fitness#'
result = ''
for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''

# %%
for i in range(21):
    print(i)
# %%
hashtags = '#weekend#good#time#'
results = ''

for char in hashtags:
    if char not in '#':
        results = results + char
        
    else:
        print(results)
        results = ''


# %%
# Napisz program, który będzie sumował liczby od 1 do 10. 
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
sum = 0
wynik = 0
for sum in range(11):
    wynik = wynik + sum
    
print('The sum of numbers from 1 to 10 is:', wynik)
    
# %%

products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]

total = 0.0
total_items = 0
for product in products:
    total += product[1]
if len(products) > 1:
    rabat = total * 0.1
    total = total - rabat
print('The total order amount after applying the discount is:', total)    

# %%
products = [
    ('T-shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 100.00),
    ('Shoes', 'Footwear', 150.00)
]
rodzaj = 'Clothing'

for product in products:
    if product[1] == rodzaj:
        print(product[0], product[2])

# %% instrukcja break

for i in '0123456789':
    i = int(i)
    print(i)
    if i  == 6:
        break

print('Koniec')        
    

# %%
sample = 'Python Course'
for char in sample:
    if char == " ":
        break
    print(char)
    
print('Koniec')    

# %%
for char in 'kowalskij@gmail.com':
    if char == '@':
        print('Adres email zweryfikowany.')
        break
else:
    print('Adres email nie jest poprawny')
    
print('Koniec')

        
# %%     
products = [
    ('Shoes', 'Footwear', 150.00),
    ('T-shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 100.00),
]

rodzaj = 'Clothing'

for product in products:
    if product[1] == rodzaj:
        print(f'The first product is {product[0]}.') #f string pozwala na zapisanie zmiennj w tekscie i jej późniejsze podstawienie
        break
    

# %%
cars = [
    {'model': 'Tesla', 'mileage': 15000, 'battery_level': 100},
    {'model': 'Nissan', 'mileage': 30000, 'battery_level': 75},
    {'model': 'BMW', 'mileage': 5000, 'battery_level': 100},
    {'model': 'Ford', 'mileage': 20000, 'battery_level': 50}
]

for car in cars:
    if car['battery_level'] == 100:
        print('The firs car with a full charge is:', car['model'])
        break
    
# %%
panels = [
    {'id': 1, 'output_power': 200},
    {'id': 2, 'output_power': 150},
    {'id': 3, 'output_power': 250},
    {'id': 4, 'output_power': 180},
]

for panel in panels:
    if panel['output_power'] > 200:
        print('The first panel with an output power greater than 200 is:', panel
              ['id'])
        break
        
# %% instrukcja continue
for i in range(10):
    if i == 6:
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 == 1:
        continue
    print(i)

# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        continue
    print(char)

# %%
hashtags = '#summer#holiday#free'
result = ''
for char in hashtags:
    if char == '#':
        print(result)
        result = ''
        continue
    result = result + char
print(result)

# %%
missions = [
    {
        'name': 'Apollo 11',
        'date': '20.07.1969',
        'status': 'completed',
    },
    {
        'name': 'Mars Pathfinder',
        'date': '04.07.1997',
        'status': 'completed',
    },
    {
        'name': 'Chang\'e 4',
        'date': '03.01.2019',
        'status': 'in progress',
    },
    {
        'name': 'Cassini',
        'date': '15.10.1997',
        'status': 'completed',
    },
]

for status in missions:
    if status['status'] == 'completed':
        print('Mission', status['name'], 'took place on', status['date'])
        continue

# %%
trainings = [
    {'name': 'Basic marksmanship', 'rank': 'Private'},
    {'name': 'Infantry tactics', 'rank': 'Corporal'},
    {'name': 'Art of war', 'rank': 'Sergeant'},
    {'name': 'Heavy weapons specialist', 'rank': 'Captain'},
    {'name': 'Advanced first aid', 'rank': 'Private'},
    {'name': 'Combat engineering', 'rank': 'Corporal'},
    {'name': 'Field intelligence', 'rank': 'Sergeant'},
    {'name': 'Military law', 'rank': 'Captain'},
    {'name': 'Parachuting', 'rank': 'Private'},
    {'name': 'Amphibious assault', 'rank': 'Corporal'},
    {'name': 'Counterterrorism', 'rank': 'Sergeant'},
    {'name': 'Military diplomacy', 'rank': 'Captain'},
]


# Solution

for training in trainings:
    if training['rank'] == 'Sergeant':
        print(f'Training for {training['rank']} is: {training['name']}')
        continue
    


# %%
raw_data = '345!23!3234!43434'
clean_data = ''

for char in raw_data:
    if char != '!':
        clean_data += char
    else:
        clean_data +=  ','
print(clean_data)

# %%
suma = 0
for i in range(10):
    suma += i
print(suma)

# %%
saldo = 450
print('Saldo początkowe{}'.format(saldo))
for kwota in range(10, 60, 10):
    print('Wypłacona kwota {}'.format(kwota))
    saldo -= kwota
    print('Saldo: {}'.format(saldo))
print('Saldo końcowe: {}'.format(saldo))


# %%
print('Witaj w systemie logowania.')
print('*' * 30)
nick = input('Podaj swój nick: ')
pin = input('Podaj swój kod pin, {}: '.format(nick))

if len(pin) == 4:
    for char in pin:
        if char not in '012345678':
            print('Podałes niepoprawny kod pin')
            break
    else:
        print('Kod pin ważny.')
else:
    print('Podałe niepoprawny kod pin.')

# %%
rooms = [
    {
        'number': 101,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
        ],
    },
    {
        'number': 102,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
        ],
    },
    {
        'number': 103,
        'available_dates': [
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
    {
        'number': 105,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
    {
        'number': 107,
        'available_dates': [
            '2023-05-11',
            '2023-05-12',
        ],
    },
    {
        'number': 110,
        'available_dates': [
            '2023-05-10',
            '2023-05-11',
            '2023-05-12',
            '2023-05-13',
        ],
    },
]
from datetime import datetime

#start_data = datetime.strptime(input('Podaj datę od: (YYYY-mm-dd): '), '%Y-%m-%d')
#end_data = datetime.strptime(input('Podaj datę do: (YYYY-mm-dd): '), '%Y-%m-%d')
start_data = datetime.strptime('2023-05-11', '%Y-%m-%d')
end_data = datetime.strptime('2023-05-13', '%Y-%m-%d')

for room in rooms:
    for available_room in room['available_dates']:
        date = datetime.strptime(['available_dates', '%Y-%m-%d'])
        if start_data <= date <= end_data:
            print('Pokój jest dostępny')
                         
            
# for available_rooms in rooms:
#     data = datetime.strptime(['available_dates'], '%Y-%m-%d')
#     if start_data >= data >= end_data:
#         print(f'Pokój nr {['number']}, jest dostępny')
#         continue
    







































