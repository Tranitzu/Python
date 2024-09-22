# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:29:15 2024

@author: pawel
"""
stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc', 'UBER.US': 'Uber Technologies Inc',
          'MSFT.US': 'Microsoft Corp'}

# %%
#stocks.keys()
#stocks.values()
#stocks.items()

for key, value in stocks.items():
    print('{:8}: {}'.format(key, value))
    
# %%

stocks_dict = {key:value for (key, value) in stocks.items()}

# %%

stocks_set = {(key, value) for (key,value) in stocks.items()}

# %%

stocks_invert = {value: key for (key, value) in stocks.items()}

# %%

stocks_lower = {key.lower(): value for (key, value) in stocks.items()}

# %%

stocks_values_len = {key: len(value) for (key, value) in stocks.items()}
    
# %%

stocks_lenght = {key: value + ':' + str(len(value)) \
                 for (key, value) in stocks.items()}

# %%
def replace_corp_inc(name):
    name = name.replace('Corp', '0')
    name = name.replace('Inc', '1')
    return name

stocks_flag = {k: replace_corp_inc(v) for (k, v) in stocks.items()}

# %%

stocks_corp = {key: val for (key, val) in stocks.items() if 'Corp' in val}
stocks_inc = {key: val for (key, val) in stocks.items() if 'Inc' in val}

# %%

stocks_start_a = {k: v for (k, v) in stocks.items() if v.startswith('A') \
                  if len(v) < 13}
    
# %%

inc_or_corp = {k: 'Corp' if 'Corp' in v else 'Inc' for (k, v) \
               in stocks.items()}

# %%
numbers = range(20)
numbers_dict = {}

for n in numbers:
    if n % 2 == 0:
        numbers_dict[n] = n ** 2
print(numbers_dict)        

# %%
num_dict = {k: k ** 2 for k in numbers if k % 2 == 0}

# %%
nested_dict = {'001': {'price': 100},
               '002': {'price': 40},
               '003': {'price': 60}}

for k, v in nested_dict.items():
    print(k, v)
    
# %%
{k: v['price'] for (k, v) in nested_dict.items()}

# %%
nested_dict = {'001': {'price': 100, 'items': 4},
               '002': {'price': 40, 'items': 9},
               '003': {'price': 60, 'items': 8}}
# %%

for k, v in nested_dict.items():
    print(k, v)

# %%
{k: v['price'] * v['items'] for (k, v) in nested_dict.items()}

















