# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:38:39 2024

@author: Paweł Falis
"""

text = 'Witaj na kursie Pythona. \nPython jest wspaniały. '
print(text)

# %%
dir(text)
help(str.count)

# %%
text.capitalize()


# %%
text.title()

# %%
text.count('Python')

# %%
text.startswith('kurs')

# %%
'python'.startswith(py)

# %%

text.endswith('y. ')

# %%
'sample.py'.endswith('.py')

# %%
'sample.png'.endswith('.png')

# %%
text.find('Python')
text[text.find('Python'):]

# %%
hashtags = 'sport#gym'
idx = hashtags.find('#')
hashtags[:idx]

# %%
'pawel212321 '.isalnum()

# %%
'4fasfdas312123412' .isdigit()

# %%
'Python' .islower()

'pawel' .isupper()

# %%
' ' .join(['python', '3.7'])
'#'.join(['sport', 'gym', 'fit'])

# %%
'#good#time#mood' .replace('#', ' ')

# %%
'column name' .replace(' ', '_')

# %%
'     python    ' .strip()
'     python    ' .rstrip()
'     python    ' .lstrip()

# %%
'1,2,3,4,5' .split(',')

'python java php sql sas' .split()

'#gym#fit#mood' .split('#')

# %%
'12' .zfill(5)
'1' .zfill(10)

# %%
#Ćwiczenie 11
words = ['sport', 'python', 'free', 'time']
joined_words = '#'.join(words)
print(joined_words)

# %%
#Ćwiczenie 12
number_string = '123,785,45,5'
numbers = number_string.split(',')
print(numbers)

# %%
#Ćwiczenie 13
text = ' Python '
print(text)
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace('P', 'C'))

# %%
#Ćwiczenie 14

text = 'script.py view.jpg README.md main.py'
char = '.py'

count = text.count(char)
print(f'The extension \'{char}\' appears {count} times in the text. ')

# %%
a = 7 // 3.0
print(a)