def mult(x,y,z):
    return x*y*z

numbers=[i for i in range(10)]

numbers_2=[i for i in range(10,15)]

# numbers_3=[i for i in range(20,30)]

# # print(list(map(mult,numbers,numbers_2,numbers_3)))




# def map(func,val):
#     result=list(func(val))
#     return result

# def func(a,b):
#     return 


""" 
--------------------------------------------------------------------------
        filter value which is True
        map can get all value 
--------------------------------------------------------------------------
        Iterables:
        list
        set
        dict 
        tuple
        fronzeset
        str
        map


"""
# print(list(filter(lambda x:x%2==0,numbers)))

# name=['','qw','sdf','bekzod','sabina']
# print(list(filter(lambda x : len(x)>=3,name)))

#zip
# print(list(zip(numbers,numbers_2,numbers_3)))

# numbers={i:str(i) for i in range(10)}

# numbers_2={i:str(i) for i in range(10,15)}
# print(list(zip(numbers.values(),numbers_2.values())))


#reduce we can add inside func, iterable, init
# работает с полученым результатом дальше
from functools import reduce
print(reduce(lambda i,x:i+x,numbers))



# def custom(initial,num):
#     print(initial,num)
#     return initial+num



# print(numbers,sum(numbers))

# print(reduce(custom,numbers,3))




# Функции вышего порядка
# def add_tax(total):
#     tax=total*0.06
#     new_total=total+tax
#     return new_total


# #Функции как аргументы
# def total_bill(func,val):
#     total=func(val)
#     return total

# # print(add_tax,100)
# print("answer= ",total_bill(add_tax,100))
