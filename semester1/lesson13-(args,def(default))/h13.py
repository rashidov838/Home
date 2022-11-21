# Exercise1
def fibonacci(n):
    if n in (1,2):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))
# Exercise2
def qwe():
    a=['name']
    b={}
    return b.fromkeys(a)
print(qwe())
# Exercise3
# Виртуальное окружение это работа с разными проектами и иметь отдельные папки свой терминал а также  библеотеки и  материалы

# Exercise4
def shades_of_grey(n):
    shades=[]
    hex='123456789abcdef'
    counter=0
    for i in range(n):
        if counter ==15:
            counter=0
        gray=f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
        if i>=15:
            break
        shades.append(gray)
        counter+=1
    return shades
print(shades_of_grey(50))

# Exercise5
def asd():
    a=[1,2,3,4]
    for i in range(len(a)):
        b=[]
        b.append([a]*4)
    if isinstance(i,(list)):
        for val in i:
            print(val='\n\n')
    return b
    
print(str(*asd()), end='\n')
# //////////////////////////////////////////////













# def shades_of_grey(n):
#     shades=[]
#     hex='123456789abcdef'
#     counter=0
#     for i in range(n):
#         if counter ==15:
#             counter=0
#         gray=f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
#         if i>=15:
#             break
#         shades.append(gray)
#         counter+=1
#     return shades
# print(shades_of_grey(50))


# from audioop import reverse


# def qwe():
#   A=([1,2])
#   A2=([2,1])
#   B=([2,3])
#   if A==B:
#     return True
#   else:
#     return False
# print(qwe())
# def qwe():
#   A=([1,2])
#   A2=([2,1])
#   B=([2,3])
#   if not A==A2:
#     return True
#   else:
#     return False
# print(qwe())
# def qwe():
#   A=([1,2])
#   A2=([2,1])
#   B=([2,3])
#   if A!=B:
#     return True
#   else:
#     return False
# print(qwe())
# message = "One of Python's strengths is its diverse community." 
# print(message)
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title())
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles.pop())
# print(motorcycles.pop(1))
# # список сортируется в порядке, обратном алфавитному:

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(sorted(cars))
# cars.reverse()
# print(cars)
# print(len(cars))
# print(cars[3][0])
# for i in  cars:
#   print(i.title()+", that was a great trick!")
#   print("I can't wait to see your next trick, " + i.title() + ".\n")
# for i in range(10,80,4):
#   print(i)
#   print(list(range(i)))