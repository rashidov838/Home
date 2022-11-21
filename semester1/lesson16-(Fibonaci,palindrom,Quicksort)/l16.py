# Exercise3
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
# Exercise2
# Traverse a Nested List
names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]
print(names[0])
print(isinstance(names[0],list))
print(isinstance(names[1],list))
print(names[1][1],list)
print(len(names))
# ///////////
for a,b in enumerate(names):
    print(a,b)

def count_leaf_items(item_list):
    count=0
    for item in item_list:
        if isinstance(item,list):
            count+=count_leaf_items(item)
        else:
            count+=1
    return count

count_leaf_items([5,6,7])
# ////////////
# Detect Palindromes
def palindrome(word):
    return word==word[::-1]
print(palindrome("qwerrewq"))
# //////////
def palind(word):
    if len(word)<=1:
        return True
    else:
        return word[0]==word[-1] and palind(word[1:-1])

print(palind(''))
print(palind('qwerty'))
print(palind('qweewq'))
# Sort With Quicksort
from ast import Num
import statistics
def quicksort(num):
    if len(num)<=1:
        return num
    else:
        vau=statistics.median(
            [
                num[0],
                num[len(num)//2],
                num[-1]
            ]
        )
        items_less,vau_items,items_greater=(
            [n for n in num if n<vau],
            [n for n in num if n==vau],
            [n for n in num if n>vau]
        )
        return (
            quicksort(items_less)+vau_items+quicksort(items_greater)
        )

print(quicksort([5,86,4,6,8]))

import random 
def random_get(length,minimm=1,maximum=100):
    numbrs=[]
    for i in range(length):
        numbrs.append(random.randint(minimm,maximum))
    return numbrs


print(random_get(50))
print(random_get(5,-50,34))
print(random_get(10,maximum=500))
print(random_get(10,10000,20000))