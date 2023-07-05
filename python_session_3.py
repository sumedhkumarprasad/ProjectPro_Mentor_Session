# -*- coding: utf-8 -*-
"""
Created on Tue May 16 00:04:56 2023

@author: Sumedh Prasad
"""

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

result = count_vowels('hello world')
print(result)  # 3


def Check_Vow(string, vowels):
     
    
    string = string.casefold()

    count = {}.fromkeys(vowels, 0)

    for character in string:
        if character in count:
            count[character] += 1   
    return count
     

vowels = 'aeiouAEIOU'
string = "Data SciencE"
print (Check_Vow(string, vowels))



#########################
my_dict = {'apple': 2, 'banana': 3, 'orange': 4}

if my_dict.get('banana', 0) > 2:
    my_dict['banana'] += 1
print(my_dict)    
    
    
    
#pythonic loop vs normal loop
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
total


numbers = [1, 2, 3, 4, 5]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
total



import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

total = 0
for i in range(len(df)):
    total += df.loc[i, 'B']

print(total)

()
{}
[]

[({})]

[](){)

{(})

#Balanced brackets 
def is_balanced(s):
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        elif c in [')', '}', ']']:
            if not stack:
                return False
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack
    
 is_balanced([({})]) 
 
 
 
 # Check if a string of brackets is balanced
result = is_balanced('(){}[]')
print(result)  # True

result = is_balanced('({[}])')
print(result)  # False


import numpy as np
import pandas as pd
list1 =[(23, '2018-08-09 07:30:13.143424', '2018-08-09 07:56:24.544946'),
        (27, '2018-08-09 07:50:06.026874', '2018-08-10 06:37:09.173335'),
            (49, '2018-08-09 07:30:13.234235', '2018-08-10 13:24:09.08271'),
            (47, '2018-08-09 07:40:02.837237', np.nan),
            (27, '2018-08-10 06:40:21.677425', '2018-08-12 07:57:13.583935')]


df1 = pd.DataFrame(list1,columns=('driver_id','start_date','end_date'))

df1['start_date_new'] = pd.to_datetime(df1['start_date'])
df1['end_date_new'] = pd.to_datetime(df1['end_date'])

df1['start_date_hrs'] = df1['start_date_new'].dt.hour
df1['end_date_hrs'] = df1['end_date_new'].dt.hour
