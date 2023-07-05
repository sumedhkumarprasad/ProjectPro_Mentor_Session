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





s1= "How are you you"
s1 = s1.lower()
s1_set = set(s1)
empty_dict = {'a':0,'e':0,'i':0, 'o' :0,'u':0}

for i in s1_set:
    if i in "aeiou":
        empty_dict[i] = empty_dict.get(i) + 1
       

print(empty_dict)

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


s1 = "How are you you"
s1 = s1.lower()
s1_set = set(s1)
vowels = "aeiou"
empty_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in s1_set:
    if char in vowels:
        empty_dict[char] =  empty_dict.get(char) + s1.count(char)
        type( s1.count(char))
print(empty_dict)

#Balanced brackets 
def is_balanced(s):
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
            print(stack)
        elif c in [')', '}', ']']:
            if not stack:
                return False
            elif c == ')' and stack[-1] == '(':
                stack.pop()
                print(stack)
            elif c == '}' and stack[-1] == '{':
                stack.pop()
                print(stack)
            elif c == ']' and stack[-1] == '[':
                stack.pop()
                print(stack)
            else:
                return False
    print(stack)
    return not stack
    
result = is_balanced([({})]) 
print(result) 

 # Check if a string of brackets is balanced
result = is_balanced('(){}[]')
print(result)  # True

result = is_balanced('({[}])')
print(result)  # False

