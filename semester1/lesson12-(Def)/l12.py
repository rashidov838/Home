# if i==1:
#     print(True)   
def great():
        print('Hello')
print('Вызов функции',great())

def great():
    return 'Hello'
result=great()
print(result)

from unittest import result


def greet(name):
    print(f'Hello{name}')

greet('Bekhruz')

s='Bekzod'
greet(s)

greet(input('input name: '))


def greet(name):
    return f"Hello{name}"
print(greet('Jamshid'))

result=greet('Aybek')
print(result)


# Написать функцию, которая принимает список фарангейтов и возвращает список цельсия 
# from readline import append_history_file


result = [] 
faranheits = [30, 20, 19, 24, 45]  
for far in faranheits: 
    celsius = (far - 32) * 5 / 9  
    if celsius >= 50: 
        print("Слишком горячо") 
        break 
    elif celsius <= 5: 
        print("Жить можно") 
    result.append(celsius)
print(result)


# square_line = 6 
# star = "*" 
# star_width = star * square_line
# def far_cel(square_line):
#     for i in range(square_line):
#         if i>0 and i< (square_line-1): 
#             empty_space = " " * (square_line-2)
#             print(f"{star}{empty_space}{star}")
#         else: 
#             print(star*square_line)
#     return 
# print(far_cel(square_line)) 

