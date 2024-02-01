from itertools import permutations
# a={'qwerty','fama','lama'}
# for _ in list("Update: "+''.join(info) for info in a):
#     print(_)

# info=[]
# info.append({
#     'id': 1,
#     'Name': 'Bekzod',
#     'password':'oqwiueqwkn'
# })
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

# keys=['id','name','password','salary']
# values=[1,'Bekzod','adijpqow@peorjwer',9837498234]
# Result={k:v for k,v in zip(keys,values)}


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

# a={3:1, 2:2, 1:3}
# print(sorted(a.items()))

# faranheits = [20, 19, 24, 45, 140]
# count=0
# while count<len(faranheits):
#     result=(faranheits[count]- 32) * 5 / 9
#     count+=1 
#     if result >= 50:
#         print(f"Слишком горячо: {result}")
#         continue
#     else: 
#         print(f"Жить можно: {result}")




def info(*args):
    for i in args:
        print(i)
info(2,3,4,'goooooo','biiiiiiii',{3,2,2,},(4,4,4),[1,2,3])
words= ['t\tr\te\tk    ', 'qwerty', 'redline', 'BEKZOD  Sami']


print(words[0].title())
print(words[0].lower())
print(words[0].upper())
print(words[0])
print(words[0].strip())
print(words[3].casefold())
print(words[3].endswith('Samir'))
print(words[3].find("Sami"))
print(words[3].index("Sami"))

words= ['t\tr\te\tk    ', 'qwerty', 'redline', 'BEKZOD  Sami']
print(words[0].expandtabs(2))

words= ['t\tr\te\tk    ', 'qwe\nrty', 'red\nline', 'BEKZOD  Sami']
for i in words:
    print(i.splitlines())


word="cpderwars"
letter=[w for w in word]
print(letter)
for p in list(permutations(letter)):
    print(''.join(p))
    