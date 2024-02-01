# num=int(input("Write number: "))
# if num>=18:
#     print("Number is higher than 18")
# else:
#     print("Number is less than 18")

# a=2
# print(a+5)

# s='BEkzod'
# for num,i in enumerate(s):
#     print(s[num])

# x=True
# y=False
# print(x==y)
# print(2>=3)
# print(2<=4)
# print(3==3)

# if 2==1:
#     print("It is equal")
# else:
#     print("It is not equal")


# name=input("Write your name: ")
# age=int(input("Write your age: "))
# print(f"Name is  {name}, age is {age}")

# num1=int(input("write first number: "))
# num2=int(input("Write second number: "))

# print(num1+num2)
# print(num1-num2)
# print(num1/num2)
# print(num1%num2)
# ----------------------------------------------
# name="Bekzod"
# def my_func():
#     global name
#     name="Samir"
#     return name 
# print(my_func())
# ----------------------------------------------
# my_name="Sherzod"
# def outer():
#     my_name="Shamsi"
#     print(my_name)
#     def inner():
#         nonlocal my_name
#         my_name="Bekzod" 
#         return my_name
#     print(inner())
# outer()
# print(my_name)
# ----------------------------------------------


# def my_func(items):
#     for num in items:
#         print(num,end=' ')
# my_func([9,6,53,2,22,33,66,89,54,88])


# def add(num1,num2):
#     return num1+num2
# print(add(12,4))
# print("Hi")