# info=[]
# a=input('Name: ' )
# b=int(input('Age:'))
# info.append( 
#     { 
#         "age": b, 
#         "name": a, 
#     } 
# )
# for i in range(len(info)):
#     info[i]['asdfghj']='VOR'
#     print(info)

# a = []
# res = a.append([{'id':'1', 'article':'name', 'url':'a.io', 'price':'1000'}])
# print(res)
# keys = [a, b, c]
# values = [1, 2, 3] 
# list_dict = {k:v for k,v in zip(keys, values)}


numbers=[1,2,3,4,5,6,7]
for val in numbers:
    if val==5 or val==7:
        print(f'Прропустить{val}')
        continue
    print('val= ',val)

# numbers=[1,2,3,4,5,6,7]
# for val in numbers:
#     if val==5 or val==7:
#         print(f'Выйти из цикла')
#         break
#     print('val= ',val)

if 1==1:
    pass 