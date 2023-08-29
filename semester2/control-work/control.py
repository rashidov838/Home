
"""Lecture

1. Генератор это подвид итерируемых объектов, как список или кортеж. Он генерирует для нас последовательность значений, которую мы можем перебрать. 
def course_generator():
    yield 'Computer Science'
    yield 'Art'
    yield 'Business'

courses=course_generator()
for course in courses:
    print(course)
2. Берем list all products переведем в iter и проходимся по next если в конце не остается то выйдет ошибка StopIteration
3. Да , оно не иззменится  
"""


# from PIL import Image
# import csv
# import datetime
# from time import time
# import time
# Task:1
# class Staff:
#     def __init__(self, name,last_name,photo,position,salary,age,department):
#         self.name=name
#         self.last_name=last_name
#         self.photo=photo
#         self.position=position
#         self.salary=salary
#         self.age=age
#         self.department=department

#     # def __str__(self):
#     #     return f'{self.name}'
#     def save_info_csv(self):
#         big_list=[{"name":self.name,"last_name":self.last_name,"photo":self.photo,"position":self.position,
#             "salary":self.salary,"age":self.age,"department":self.department}]
#         with open('staff.csv','w',newline='',encoding="utf-8") as all_info:
#             fields=['name',"last_name","photo","position","salary","age","department"]
#             output_writer=csv.DictWriter(all_info,fieldnames=fields)
#             output_writer.writeheader()
#             for item in big_list:
#                 output_writer.writerow(item)

#     def read_info_from_staff_csv(self):
#         with open('staff.csv',newline='') as file:
#             all_info=csv.DictReader(file,delimiter=',')
#             for row in all_info:
#                 print(row)

#     # def filter_last_name_department(self):
#     #     print(list(filter(lambda last_name,:)))



# filename="drawpict.png"
# with Image.open(filename) as img:
#     img.load()

# info=Staff("Bekzod",'Rashidov',img,'Python developer',20000,20,'IT')
# print(info.save_info_csv())
# print(info.read_info_from_staff_csv())









# class Purchase():
#     def __init__(self,purchase_id,qunatity,price,created_at,uploaded_at):
#         self.purchase_id=purchase_id
#         self.qunatity=qunatity
#         self.price=price
#         self.created_at=created_at
#         self.uploaded_at=uploaded_at
    

# pur=Purchase(1,30,1500,datetime.date(1999, 12, 25),datetime.date(2023, 12, 20))

# products=['appple',"banana"]
# class Load_Wagon:
#     def __init__(self,wagon_id,type,status,shipping_date,location,products,updated_at,created_at):
#         self.wagon_id=wagon_id
#         self.type=type
#         self.status=status
#         self.shipping_date=shipping_date
#         self.location=location
#         self.products=products
#         self.updated_at=updated_at
#         self.created_at=created_at

#     def attach_wagon(self):
#         return f'wagon_id: {self.wagon_id} type: {self.type}, status: {self.status}, shipping_date: {self.shipping_date}, location: {self.location} products: {self.products},updated_at: {self.updated_at},created_at:{self.created_at}'



# load_info=Load_Wagon(1,"Wagon","Not loaded",datetime.date(1999, 12, 25),'Uzbekistan',products,datetime.date(1999, 12, 15),datetime.date(1999, 12, 10))
# print(load_info.attach_wagon())

# class Load_Gruz:
#     def __init__(self,load_id,qunatity,status,purchase_id,wagon_id):
#         self.load_id=load_id
#         self.qunatity=qunatity
#         self.status=status
#         self.purchase_id=purchase_id
#         self.wagon_id=wagon_id  
#     def  create_load(self):
#         return f'load_id: {self.load_id} qunatity{self.qunatity}, status: {self.status}, purchase_id: {self.purchase_id}, wagon_id: {self.wagon_id}'

# load_gruz=Load_Gruz(1,30,' Not loaded',1,1)

# print(load_gruz.create_load())




# Task-3

# def rewrite():
#     numbers_1=[1,2,3,4,5,6,78,8,7]
#     numbers_2=[2,6,8,9,0,5,78,6,2]
#     a = set(numbers_1)
#     b = set(numbers_2)
#     # Логическое Или
#     yield a | b
#     # Логическое и
#     yield a & b
#     yield a - b
#     # Исключающее ИЛИ
#     yield a ^ b
    


# for gen in rewrite():
#     print(gen)

# Task-4

# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#         time.sleep(5)
#         return result
#     return wrapper
# @my_decorator
# def slow_rate(n):
#     for i in range(n):
#         for j in range(100000):
#             i*j
  
# slow_rate(5)