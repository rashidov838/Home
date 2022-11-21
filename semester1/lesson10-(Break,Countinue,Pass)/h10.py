# 1. Создать программу которая записывывает в список 10 словаря состоящий из двух ключей: "name" и "age" и при этом используйте input и for.
# Пример: 
# Скажем у нас есть пустой список
# info = []
# На результат верунть список из 10 словарей, где каждый словарь состоит из ключей "name" и "age"

#Exercise1
info=[]
while True:
    name=input('Name:')
    age=int(input('Age: '))
    info.append({
        'name': name,
        'age': age
})
    print(info)
# /////////////////////////////////////
# Exercise1.2
info=[]
for i in range(10):
    name=input('Name:')
    age=int(input('Age: '))
    info.append({
        'name': name,
        'age': age
})
    print(info)

# //////////////////////////////////////////

# 2. Написать программу, которая переводит значение из списка из фарангейта в цельсий.  
# Если после перевода на цельсий градус выше 50, закончить цикл и вывести на экран "Слишком горячо" 
# Если ниже 5 вывести на экран "Жить можно"  
# Формула нахождения цельсия из фарангейта: (32F − 32) × 5/9 = 0C 
# Exercise2
faranheits = [20, 19, 24, 45] 
celsius1= (faranheits[0] - 32) * 5 / 9
celsius2 = (faranheits[1] - 32) * 5 / 9
celsius3 = (faranheits[2] - 32) * 5 / 9
celsius4= (faranheits[3] - 32) * 5 / 9
if  celsius1>=50 and celsius2>=50 and celsius2>=50 and celsius2>=50:
        print(f"Слишком горячо" )
else:
    print(f'Жить можно{celsius1}{celsius2}{celsius3}{celsius4}')
# /////////////////////////////////////////////
# Exercise 2.1
faranheits = [20, 19, 24, 45] 
celsius1= (faranheits[0] - 32) * 5 / 9
celsius2 = (faranheits[1] - 32) * 5 / 9
celsius3 = (faranheits[2] - 32) * 5 / 9
celsius4= (faranheits[3] - 32) * 5 / 9
print(celsius1,celsius2,celsius3,celsius4)
val=[celsius1,celsius2,celsius3,celsius4]
for num in val:
    if  num>=50:
        print(f"Слишком горячо" )
    break
else:
    print(f'Жить можно{celsius1,celsius2,celsius3,celsius4}')
# ///////////////////////////////////////////////////
# Exercise 2.2
faranheits = [200, 190, 240, 45] 
celsius1= (faranheits[0] - 32) * 5 / 9
celsius2 = (faranheits[1] - 32) * 5 / 9
celsius3 = (faranheits[2] - 32) * 5 / 9
celsius4= (faranheits[3] - 32) * 5 / 9
print(celsius1,celsius2,celsius3,celsius4)
val=[celsius1,celsius2,celsius3,celsius4]
for num in val:
    if  num>=50:
        print(f"Слишком горячо" )
    continue
else:
    print(f'Жить можно')


