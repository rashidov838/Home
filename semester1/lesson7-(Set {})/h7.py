# Прочитать и попробовать методы множеств (set):
#  union, update, add, pop, remove, copy, clear, difference 


# a={'qwerty','fama','lama'}
# b={'kola','pepsi','qwerty'} #Union
# x=a.union(b)  #Not repeat same words Дополняет то что не хватает
# print(x) 

a={'qwerty','fama','lama'}    #Update
b={'kola','pepsi','qwerty'} #Not repeat same words again 
a.update(b)
print(a)

# a={'qwerty','fama','lama'} 
# a.add('banana')        #ADD
# print(a)

# b={'kola','pepsi','qwerty'}
# b.add(123)   #ADD
# print(b)

a={'qwerty','fama','lama','asdfg','asdfadfad'} # В середине удаляет слово
a.pop()
print(a)

# b={'kola','pepsi','fanta'}
# b.pop()
# print(b)

# a={'qwerty','fama','lama'} 
# a.remove('qwerty')
# print(a)


# b={'kola','pepsi','fanta'}
# b.remove('fanta')
# print(b)

# Copy
# a={'qwerty','fama','lama'} 
# c=a.copy()
# print(c)

# b={'kola','pepsi','fanta'}
# d=b.copy()
# print(d)

# Clear
# a={'qwerty','fama','lama'} 
# a.clear()
# print(a)

# b={'kola','pepsi','fanta'}
# b.clear()
# print(b)
# Difference
# a={'qwerty','fama','lama'}
# b={'kola','pepsi','fanta','qwerty'}

# x=a.difference(b)
# print(x)                     #Оно только относится а или б комплемент

# c=b.difference(a)
# print(c)
# ////////////////////////////////////////////////////////////////////////////////////////


# 2 exe/Прочитать и попробовать методы словарей (dict).

# Clear
# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user2={
#     'name':'Sancho',
#     'password':'098765',
#     'age':78
# }

# user.clear()
# print(user)
# print(user2)

# user2.clear()
# print(user2)
# print(user)
# #Copy

# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user2={
#     'name':'Sancho',
#     'password':'098765',
#     'age':78
# }

# a=user.copy()
# print(a)
# b=user2.copy()
# print(b)

# Get
# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user2={
#     'name':'Sancho',
#     'password':'098765',
#     'age':78
# }

# a=user.get('password')
# print(a)
# s=user2.get('password')
# print(s)
# d=user.get('age')
# print(d)
# f=user2.get('name')
# print(f)

# Items
# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user2={
#     'name':'Sancho',
#     'password':'098765',
#     'age':78
# }
# a=user.items()
# print(a)

# s=user2.items()
# print(s)

# Keys
# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user2={
#     'name':'Sancho',
#     'password':'098765',
#     'age':78
# }
# a=user.keys()
# print(a)
# s=user.keys()
# print(s)
# a=user.keys()
# user['height']=[1234567]
# print(a)

# Pop
# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user2={
#     'name':'Sancho',
#     'password':'098765',
#     'age':78
# }

# user.pop('name')
# print(user)
# user2.pop('age')
# print(user2)


# Popitem
user={
    'name':'bekzod',
    'password':'1234567',
    'age':89
}
user2={
    'name':'Sancho',
    'password':'098765',
    'age':78,
    'QWERTYU': 'ASDFGHJK' #Самое полмденее не берет qwerty или age

}

user.popitem()
print(user)
user2.popitem()
print(user2)


# Setdefault
# from turtle import color


user={
    'name':'bekzod',
    'password':'1234567',
    'age':89
}
user2={
    'name':'Sancho',
    'password':'098765',
    'age':78
}

a=user.setdefault('name')
print(a)
s=user2.setdefault('name') #Пиши ключ получаем значение
print(s)

# d=user.setdefault('color','white')
# print(d)
# f=user2.setdefault('color','black')
# print(f)


# update
user={
    'name':'bekzod',
    'password':'1234567',
    'age':89
}
user2={
    'name':'Sancho',
    'password':'098765',
    'age':78
}

user.update({'region':'tashkent'})
print(user)
user.update({'height':'12345678'}) # Тоже добавление
print(user)


# VAlues
# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user2={
#     'name':'Sancho',
#     'password':'098765',
#     'age':78
# }
# a=user2.values()
# print(a)
# user2['age']=34
# print(a)
# ///////////////////////////////////////////////////////

# user={
#     'name':'bekzod',
#     'password':'1234567',
#     'age':89
# }
# user['name']='Samina'
# user['university']='Amity'
# print(user)

# del user['password']
# print(user)
# user.clear()
# print(user)

