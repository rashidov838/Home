# try:
#     10/0
# except Exception as err:
#     print("Worked",err)


# USERS=[
#     {   'name': 'Sabina',
#         'email': 'sa@',
#         'password': '123456',
#         'purchases': [],
#         'card': {'code': '1234567891234567', 'balance': 1000}
#     }
# ]
# def register( name, email, password, card_code, card_balance):
#         # Есть ли данный пользователь в системе
#         for user in USERS:
#             if user['email'] == email and user['password'] == password:
#                 return "Пользователь с такими данными уже есть."

#         if not (name and email and password and card_code and card_balance):
#             return 'Empty values were given.'
#         try:
#             if name.isalpha() and '@' in email and len(password) >= 6 and len(card_code) == 16 and card_balance >= 0:
#                 USERS.append(
#                     {
#                         'name': name,
#                         'password': password,
#                         'email': email,
#                         'purchases': [],
#                         'card': {'code': card_code, 'balance': card_balance}
#                     }
#                 )
#                 print(USERS)
#         except TypeError  as err:
#             print("Exception",err)
#         except AttributeError  as err:
#             print("Exception",err)
#         else:
#             print('No exception')
#         finally:
#             print("Will work")

# print(register('Bekzod','bekzodrashidov@gmail.com',12345623,1234567891234567,44))






# class OWnexception(Exception):
#     pass



# users={
#     'age':12,
#     'name':'Bekzod'
# }
# # if users['age']<18:
# #     raise OWnexception()


# class Lengthexception(Exception):
#     pass
# try:
#     if len(users['name'])>3:
#         raise Lengthexception()
#     else:
#         print("Eligible to Vote ")
# except Lengthexception as err:
#     print("Exceprion",err)
# finally:
#     print("Will wor")



cat_food={
    'Cat':2,
    'Cat1':3,
    'Cat2':4
}

# for cat in cat_food:
#     print(cat+'has '+ str(cat_food[cat])+'bags')

cat_food_iterator=iter(cat_food)
# print(cat_food_iterator)
a=next(cat_food_iterator)
print(a)

# cat_food_iterator_two=iter(cat_food)
# print(cat_food_iterator_two)
# a=next(cat_food_iterator_two)
# print(a)
# a=next(cat_food_iterator_two)
# print(a)
print(map(next,cat_food_iterator))
# ---------------------------------------------------------

# cat_food={
#     'Cat':2,
#     'Cat1':3,
#     'Cat2':4
# }

for cat in cat_food:
    print(cat+'has '+str(cat_food[cat])+'bags')

# cat_food_iter=iter(cat_food)
# while True:
#     try:
#         print("work")
#         next(cat_food_iter)
#     except StopIteration as e:
#         break
#     finally:
#         print("It was worked")

