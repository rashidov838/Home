# class FishInventory:
#     def __init__(self,fishlist) :
#         self.available=fishlist

#     def __iter__(self):
#         self.index=0
#         return self

#     def __next__(self):
#         if self.index<len(self.available):
#             fish_status=self.available[self.index] + ' plus'
#             self.index+=1
#             return fish_status
#         else:
#             raise StopIteration 

# fish_inventory_cls=FishInventory(['Bekzod','SMall'])
# print(fish_inventory_cls.__iter__())

# for fish in fish_inventory_cls:
#     print(fish)


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



from itertools import   count,chain,combinations
# for i in count(start=0,step=4):
#     print(i)
#     if i>=20:
#         break



# odd=[3,4,5]
# even={6,3,7}
# all_numbers=chain(odd,even)
# for num in all_numbers:
#     print(num)

even=[2,5,6]
even_combination=list(combinations(even,2))
print(even_combination)


collars=['Red-S','Red-M','Blue-S','Yellow-S']
col_combination=combinations(collars,2)
for i in col_combination:
    print(i)                    



# # Generator expressions
print(list(i for i in range(100000000)))
def multiply(a,b):
    sum=0
    return a*b

print(multiply(3,6))
def course_generator():
    yield 'Computer Science'
    yield 'Art'
    yield 'Business'

courses=course_generator()
for course in courses:
    print(course)

# ---------------------------------------------------------


# ---------------------------------------------------------
# def prize_generator():
#     student_info={
#         'Joan Tsark':355,
#         'Bekzod':123,
#         'Sabina':12,
#         'Kate':45

#     }

#     for student in student_info:
#         name=student
#         id=student_info[name]
#         if id%3==0 and id%5==0:
#             yield student+" Get prize C"
#         elif id%3==0:
#             yield student+" Get prize B"
#         elif id%5==0:
#             yield student+" Get prize A"

# prizes=prize_generator()
# for prize in prizes:
#     print(prize)


# def fibonacci(n=10):
#     return (1 if n in (1, 2) else fibonacci(n-1) + fibonacci(n-2) )
    

# generator=fibonacci()
# for gen in generator:
#     print(gen)


# def fibonacci():
#     n=10
#     # return (1 if n in (1, 2) else fibonacci(n-1) + fibonacci(n-2))
#     if n in (1, 2):
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)


# generator=fibonacci()
# for gen in generator:
#     print(gen)
