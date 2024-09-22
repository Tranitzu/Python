# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:49:48 2024

@author: pawel
"""
from collections import Counter

soldiers = [
    {'name': 'Alice', 'rank': 'Private', 'service_years': 2},
    {'name': 'Bob', 'rank': 'Sergeant', 'service_years': 4},
    {'name': 'Charlie', 'rank': 'Sergeant', 'service_years': 6},
    {'name': 'David', 'rank': 'Lieutenant', 'service_years': 3},
    {'name': 'Eve', 'rank': 'Private', 'service_years': 1},
    {'name': 'Frank', 'rank': 'Lieutenant', 'service_years': 7},
]

# {k: v['price'] * v['items'] for (k, v) in nested_dict.items()}

rank_dict = {soldier['rank']: sum( 1 for s in soldiers if s['rank'] == soldier['rank'])
    for soldier in soldiers
}
print(rank_dict)

# %%
compounds = [
    {
        'name': 'Water',
        'atoms': ['H', 'O', 'H'],
    },
    {
        'name': 'Methane',
        'atoms': ['C', 'H', 'H', 'H', 'H'],
    },
    {
        'name': 'Ethanol',
        'atoms': ['C', 'H', 'O', 'H', 'H', 'C', 'H', 'H', 'H'],
    },
]


element_sum = {(element['atoms']: sum(1 for one in compounds if one['atoms' == element'atoms'])) for element in compounds}

print(element_sum)