# def fibonaci(num):
#     if num in(1,2):
#         return 1
#     return fibonaci(num-1)+fibonaci(num-2)

# print(fibonaci(10))

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

# print(*list(w for w in names))




# print(names[0])

# print(isinstance(names[1],list))
# print(isinstance(names[2],str))
# print(names[1][1],list)
# print(len(names))


# for id_num, val in enumerate(names):
#     print(id_num,val)
# def count_leaf_items(object):
#     count=0
#     for obj in object:
#         if isinstance(obj,list):
#             count+=count_leaf_items(obj)
#         else:
#             count+=1
#     return count

# print(count_leaf_items([9,4,5,6]))




# def palindrome(word):
#     return word==word[::-1]

# print(palindrome('weew'))


# import random

# def random_number(length,minumum=1,maximum=100):
#     numbers=[]
#     count=0
#     while count<length:
#         numbers.append(random.randint(minumum,maximum))
#         count+=1
#     return numbers

# print(random_number(50))
# print(random_number(5,-20,10))


from ast import Num
import statistics

def quick_sort(num):
    if len(num)<=1:
        return num
    else:
        val=statistics.median(
            [num[0],
            num[len(num)//2],
            num[-1]
            
            ]
        )
        items_less,val_items,items_grater=(
            [n for n in num if n<val],
            [n for n in num if n==val],
            [n for n in num if n> val]
        )
        return (
            quick_sort(items_less)+val_items+quick_sort(items_grater)
        )
    
print(quick_sort([5,86,4,6,8]))