# #local
# def info_about_person():
#     name='Salim'
#     return name 

# print(info_about_person())

# #global
# name='Bekzod'  
# def info_about_person():
#     global name
#     name='Salim'
#     return name 

# print(info_about_person())


# enclosed
# lastname='rashidov'
# def info_about_lastname():
#     lastname='Komilov'
#     def info_about_lastname_1():
#         lastname='Samitov'
#         return lastname
#     return info_about_lastname_1()
# print(info_about_lastname())


# from math import pi

# def  first_area():
#     def second_area():
#         print(pi)
#     second_area()
# first_area()


# Info_dict={'Bekzod':12,
# 'Samila':99,
# 'BOla':9}
# a=[ x and s for x,s in Info_dict.items()]
# print(a)


#Ternary
x=10
y=20
answer= 1 if x<y  else 0
print(answer)

#Lambda - anonym func
def func_name():
    return 


anonymous_func= lambda x,y:x+y
print(anonymous_func(40,11))

anonymous_func= lambda x,y:x+y
print(anonymous_func('wertyhujki','xcvbnm'))



#map() -> function amd iterable objects can be given  inside map()
def square(x):
    return x**2

# answer=list(map(square,[3,4,5]))
# print(answer)

answer=list(map(lambda x: x**2,[3,4,5]))
print(answer)
# iterable it can contains one more value