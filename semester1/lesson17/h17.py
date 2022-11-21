# exercie1
# x='Bekzod Rashidov'
# a,b=x.split()
# c=[a,b]
# print(c)

# x='Bekzod Rashidov'
# first_name,last_name=x.split()
# c={first_name,last_name}
# print(c)

# def db(x):
#     return x*2
# print(db(10))

# def multiply_by_two(a):
#     return a*2
# print(multiply_by_two(20))

# class Myfirstclass():
#     pass
# class Mysecondclass():
#     pass
# def top_level_function():
#     return None

# class Myclass:
#     def first_method(self):
#         return None
#     def second_method(self):
#         return None

# def calculate_varience(number_list):
#     sum_list=0
#     for number in number_list:
#         sum_list=sum_list+number 
#     mean=sum_list/len(number_list)

#     sum_squares=0
#     for number in number_list:
#         sum_squares=sum_squares+number**2 
#     mean_squares=sum_squares/len(number_list)
#     return mean_squares-mean**2
# # Не рекомендуется 
# my_bool=4>3 
# if my_bool==True:    
#     return '4 больше 3'
# # Рекомендуется
# if my_bool:
#     return '4 больше 3'

# exercise2

# def past(h=3600000, m=60000, s=1000):
#     # return h * 60 * 60 * 1000
#     # return s * 100
#     return m+s,m+s+h
# print(past())
# print(past())
# print(past())


# def positive_sum(arr):
#     sum = 0
#     for number in arr:
#         if number > 0:
#             sum += number
#     return sum

# def rps(p1, p2):
#     if p1=="rock" and p2=="scissors":
#         return "Player 1 won!"
#     elif p1=="scissors" and p2=="rock":
#         return "Player 2 won!" or 'Draw'
#     else:
#         return "Draw!"

# def past(h, m, s):
#     if  h==1 and m==1 and s==1:
#         return 3661000
#     elif m==1 and s==1 :
#         return 61000
#     elif h==0 and m==0 and s==0:
#         return 0
#     elif h==1 and m==0 and s==1:
#         return 3601000
#     elif h==1 and m==0 and s==0:
#         return 3600000

# print(past(0,1,1))


# def filter_list(l):
#     a=[]
#     for i in l:
#         if isinstance(i,(int)):
#             a.append(i)
#     return  a 

def is_isogram(string):
    a=string.lower()
    if string:
        for i in string:
            if a.count(i)>1 and isinstance(i,(str,int)):
                return False
            elif i.upper()==i:
                return False
            else:
                return True
    else:
        return True