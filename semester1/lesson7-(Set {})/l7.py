#cd 
# dir
# py 
# python

from unicodedata import name

#Интерируемые-iterableю Исчисляемые  Это те переменые которые хранят больше одного значения 
# индексы 



numbers={2,3,4,'Hello',2,4}
print(numbers)
numbers={}  #dict
print(type(numbers))
numbers=set()
print(type(numbers))

remove_duplicates=[1,2,3,4,5,6,1,2,3,4,'AA','VV','AA']
print(remove_duplicates,set(remove_duplicates),sep='\n')
print(set(remove_duplicates))
print(list(set(remove_duplicates)))
print(tuple(set(remove_duplicates)))
# list 
# tuple
# set

#List inmuatable

#     
name=[1,3,4,5]
print(type(name))
#Tuple muatable
names=()
print(type(names))
#Dictionary 

user_data={}
print(type(user_data),user_data)
 
user_data={
     'key':'znacheniya',
    1:None,
    2:21,
    3:6.7,
    4:[2,3,4],
    5:(3,4,5),
    6:{'key':"Другой словарь"}
    #[1]:23 #error
    #(2,3,[2,3]):'Error' # Кортеж можно использовать как клюсь но не рекомендуется

}
#40-50
print(type(user_data),user_data['key'])
print(user_data[1])
print(user_data[2])
print(user_data[3])
print(user_data[4])
print(user_data[5])
print(user_data[6])
print(user_data[1],user_data[2],user_data[3],user_data[4],user_data[5],user_data[6], sep='\n') 



user_data={
    'username':"Gabby",
    'password':'234567',
    'age':23

}

print(user_data['age'])

user_data['username']='qwerty'
print(user_data.keys(),user_data.values(),user_data.items(),sep='\n')

#view
#dict_keys(['username', 'password', 'age'])  KEYS
#dict_values(['qwerty', '234567', 23])           VALUES
#dict_items([('username', 'qwerty'), ('password', '234567'), ('age', 23)])  Items

user_list=list(user_data.values())
print(user_list)

user_list=list(user_data.keys())
print(user_list)


print('get',user_data.get('age'),user_data.get('username'),user_data.get('unexisting'))  #GET
#user_data.get('unexisting') Answer: None


user_data_2={
    'username':"Gabby",
    'password':'234567',  
    'age':23,

}





user_data=[
 {  'username':'Gabby',
    'password':'234567',
    'age':18,   },
{   'username':"qwerty",
    'password':'234567',
    'age':48,   },

]

print(user_data[0]['username'])
print(user_data[1]['age'])
# print(user_data[0]['234567']) #error
 
