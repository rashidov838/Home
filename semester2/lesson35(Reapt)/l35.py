from functools import reduce
# products=['apple', 'samsung', 'oneplus']

# pr_iter=iter(products)
# while True:
#     try:
#         print(next(pr_iter))
#     except StopIteration as err:
#         break

# def multi(x,y,z):
#     return x*y*z

numbers=[i for i in range(10)]

numbers_2=[i for i in range(10,15)]

numbers_3=[i for i in range(10,15)]

# print(list(map(multi,numbers,numbers_2,numbers_3)))



# print(list(filter(lambda x : x%2==0,numbers)))
# name=['','qw','sdf','bekzod','sabina']
# print(list(filter(lambda x: len(x)>=3,name)))



# print(list(zip(numbers,numbers_2,numbers_3)))




# num={i:str(i) for i in range(10,15)}
# print(list(zip(numbers,num.values())))

# print(reduce(lambda x,y :x+y,numbers))
 



# def add_tax(total):
#     tax=total*0.06
#     new_total=total+tax
#     return new_total


# def total_bill(func,val):
#     total=func(val)
#     return total

# print('answer',total_bill(add_tax,100))



# def hello():
#     print("Greeting")
# hello()

# def my_dec(func):
#     def wrapper():
#         print("Расширяем функцию")
#         func()
#         print("Расширяем функцию")
#     return wrapper

# answer=my_dec(hello)
# print(answer())

# @my_dec
# def like_me():
#     print("Like me")
# like_me()

# def authorize(func):
#     def wrapper(x,y):
#         print("Расширяем функцию")
#         print("Расширяем функцию")
#         return func(x,y)
#     return wrapper


# @authorize
# def mult(n1,n2):
#     return n1*n2
# print(mult(932,66))



# def authorize(func):
#     def wrapper(*args,**kwargs):
#         print("Расширяем функцию")
#         print("Расширяем функцию")
#         return func(*args,**kwargs)
#     return wrapper



# @authorize
# def like(username,password):
#     print(f'My username : {username} ')
#     print(f'My password: {password}')
# like('Bekzod','adf231')




# try:
#     10/0
# except Exception as err:
#     print(err)



users={
    'age':12,
    'name':'Bekzod'
}


# class LengthException(Exception):
#     print( 'Length is short')


# try:
#     if len(users['name'])>3:
#         raise LengthException()
#     else:
#         print("Eligible to Vote ")

# except LengthException as err:
#     print(err)


# finally:
#     print("it is working ")
# cat_food={
#     'Cat':2,
#     'Cat1':3,
#     'Cat2':4
# }

# cat_iter=iter(cat_food)
 
# print(map(next,cat_iter))


# for cat in cat_food:
#     print(cat +'has ' +str(cat_food[cat]) +' bags')




# class CustomerCounter:
#     def __init__(self,customer_list):
#         self.customers=customer_list
    
#     def __iter__(self):
#         self.index=0
#         return self
#     def __next__(self):
#         if self.index<len(self.customers) and self.index<100:
#             customer_status=self.customers[self.index]
#             self.index+=1
#             return customer_status
#         else: 
#             raise StopIteration

# customer_cls=CustomerCounter(list(range(110)))
# for customer in customer_cls:
#     print(customer)




from itertools import count,chain,combinations


# for i in count(start=0,step=4):
#     print(i)
#     if i>=20:
#         break


# even=[2,5,6]

# ev_com=list(combinations(even,2))
# print(ev_com)


# def course_gen():
#     yield 'Comp'

# for c_g in course_gen():
#     print(c_g)


# print(list(i for i in range(120202)))


# def prixe_gen():
#     student_info={
#         'Joan Tsark':355,
#         'Bekzod':123,
#         'Sabina':12,
#         'Kate':45

#     }

#     for st in student_info:
#         name=st
#         id=student_info[name]
#         if id%3==0 and id%5==0:
#             yield st+" Get prize C"

#         elif id%3==0:
#             yield st+" Get prize B"
#         elif id%5==0:
#             yield st+" Get prize A"


# for std in prixe_gen():
#     print(std)



# def fibonacci(n):

#     if n in (1, 2):
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# generator=fibonacci(10)
# for gen in generator:
#     print(gen)



def fib(n):
    try: 
        if n<0:
            print("Incorrect input")
        elif n==0:
            return 0
        
        elif n==1 or n==2:
            return 1
        else:
            return fib(n-1)+fib(n-2)
    except RecursionError as err:
        print(err)    
print(fib(10))