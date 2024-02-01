# info=[]
# name=input('Name: ')
# age=int(input('Age: '))

# info.append({
#     'name':name,
#     'age' : age
# })
# print(info)


# info.append({
#     'id': 1,
#     'Name': 'Bekzod',
#     'password':'oqwiueqwkn'
# })


# print(info)
# for inf in info:
#     for key,val in inf.items():
#         inf['password']=1239328473
# info.append({
#     'id': 2,
#     'Name': 'Bekzod',
#     'password':'oqwiueqwkn'
# })      
# print(info)
# for i in range(len(info)):
#     info[i]['MOney']=10000
# print(info)


# main_list=[]
# res=main_list.append([{'id':'1', 'article':'name', 'url':'a.io', 'price':'1000'}])
# print(*main_list)


# keys=['id','name','password','salary']
# values=[1,'Bekzod','adijpqow@peorjwer',9837498234]
# Result={k:v for k,v in zip(keys,values)}
# print(Result)
# numbers=[2,3,4,5,6,5,0,2,1,1,1,987,63]
# for num in numbers:
#     if num==1 or num==5:
#         continue
#     print(num)
# for num in numbers:
#     if num == 4:
#         break
#     else:
#         print(num)


name='Bekzod'
age=25
count=0
info=[]
# while count<10:
#     info.append({'Name':name,'Age':age})
#     count+=1
# print(info)


# for i in range(10):
#     info.append({'Name':name,'age':age})
# print(info)

faranheits = [20, 19, 24, 4500,11] 
result_calculation=[]
for f in range(len(faranheits)):
    calculation=(faranheits[f] - 32) * 5 / 9
    result_calculation.append(calculation)
# print(result_calculation)
for res in result_calculation:
    if  res>=50:
        print(f"Слишком горячо: {res}" )
        continue
    else:
        print(f'Жить можно: {res}')
