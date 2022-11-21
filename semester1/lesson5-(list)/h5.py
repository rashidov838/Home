# append, count, copy, insert, sort, extend, pop, index
from audioop import reverse
from turtle import back
from unicodedata import decimal

# 1 
list="phew" 
print(list[::-1])

# 2
product=['banana', "apple",'milk','bread','pOTATO','rOLTON']
product.insert(3,'popcorn')       #INSERT
print(product)
product.append('cherry')     #APPEND
print(product)
print(sorted(product))
print(product)
print(sorted(product,reverse=True))     #SORT
print(product)
product[3]='qwerty'                #INDEX
print(product)             
product2=product.copy()     #COPY
print(product2)
product2.pop(-3) #POP
print(product2)
product1=[1,2,3,4,5,6,7,5,6]
x=product1.count(5)          #COUNT
print(x) 
product=['banana', "apple",'milk','bread','pOTATO','rOLTON']
product1=[1,2,3,4,5,6,7]
product.extend(product1)   #extend
print(product)


# from decimal import *
# getcontext().prec=28
# decimal(10)


x=2+3j
x1=3-4j
print(type(x))
print(type(x1))


