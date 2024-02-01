# numbers={2,3,4,5,"hello",2,342}
# print(numbers)
# print("Monika")
# my_word={}
# print(my_word)
# numbers={}
# print(type(numbers))
# numbers=set()
# print(type(numbers))

# remove_same_info=[1,2,3,4,5,6,1,2,3,4,'AA','VV','AA']
# print(set(remove_same_info),sep='\n')
# print(list(set(remove_same_info)))
# print(tuple(set(remove_same_info)))
# name_of_people=['Jonay,"Kenny',"dolla"]
# print(type(name_of_people))
# user_info={
#     'id':123,
#     "name":"Bekzod",
#     'surname':"Rashidov",
#     'phone':+998944555564,
#     'id_card':{'num':746573638}
# }
# user_info['id_card']['num']=1111111111111111111111
# print(user_info)
# print(user_info['id_card']['num'])
# print(user_info['id'])
# print(user_info['name'])
# print(user_info['surname'])
# print(user_info['phone'])



# print(user_info.keys())
# print(user_info.values())
# print(user_info.items(),end='\n')


# print(list(user_info.values()))
# print(list(user_info.keys()))
# ----------------------------------------------
# print(list(user_info.items()))
# print('\n'.join(str(info) for info in list(user_info.items())))

# print(user_info.get('id_card'))
# print(user_info.get('name'))
# print(user_info.get('phone'))
# print(user_info.get('surname'))


# Multi_inforamtion
# user_info=[{
#     'id':1,
#     "name":"Bekzod",
#     'surname':"Rashidov",
#     'phone':+998944555564,
#     'id_card':{'num':746573638}
# },
# {
#     'id':2,
#     "name":"Munira",
#     'surname':"Ramatova",
#     'phone':+9989448302874,
#     'id_card':{'num':18470174}
# },

# {
#     'id':3,
#     "name":"Shaxriyor",
#     'surname':"Sobirov",
#     'phone':+9989491284712,
#     'id_card':{'num':1024710}
# }
# ]


# print(user_info[2]['id_card']['num'])
# print(user_info[1]['name'])


# a={'qwerty','fama','lama'}
# b={'kola','pepsi','qwerty'}
# a.update(b)
# for _ in list("Update: "+''.join(info) for info in a):
#     print(_)


# for i in b:
#     a.add(i)
# for _ in list("Add: "+''.join(info) for info in a):
#     print(_)


# print(sorted(a))
# print(a.pop())
# a.remove('fama')
# print(a)

# q=a.copy()
# q.add('saar')
# print(q)
# # q.clear()
# # print(q)
# a={'qwerty','fama','lama'}
# b={'kola','pepsi','fanta','qwerty'}
# check=a.difference(b)
# print(check)

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

# info=user.get('password')
# print(info)
# print(list(user.keys()))
# print(list(user.values()))
# print(*(list(user.items())))

# user['age']=79
# print(user)

# print(user.pop('age'))
# print(user)
# print(user2.popitem())


user={
    'name':'Samir',
    'password':12739128,
    'id':1
}
user2={
    'name':'Komil',
    'password':93740231,
    'id':2

}

print(user.setdefault('name'))
print(user.setdefault('password'))
print(user.setdefault('id'))


user.update({'location':'Tashkent'})
print(user)
# print(user.values())
del user['id']
print(user)
user.pop('password')
print(user)

