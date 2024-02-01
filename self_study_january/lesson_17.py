# obj={
#     'RACE':"oGRE",
#     'age':100,
#     'skill':['Roar'],
# }

# print(list({num:i} for num,i in enumerate(list(obj.values()))))

# if 'RACE' in obj and 'age' in obj and isinstance(obj['age'],int):
#     print(obj['RACE'],obj['age'])
# else:
#     print('Invalid')


# def short_word(names):
#     if names:
#         length=len(names[0])
#         # print(length)
#     else:
#         return False

#     for name in names[1:]:
#         length_name=len(name)
#         if length_name<length:
#             length=length_name
#     return length

# print(short_word(['Bekzod','John','GAbriel','Az','sdhjaksdjas']))



# def encode(obj:str):
#     list_of_alp=list(obj)
#     print(list_of_alp)
#     total=''
#     for i in range(len(list_of_alp)):
#         if i%2==0:
#             total+=list_of_alp[0]
#             list_of_alp.pop(0)
#         else:
#             total+=list_of_alp[-1]
#             list_of_alp.pop(-1)
#         # print(list_of_alp,total)
#     return total
# print(encode('codewars'))



# def decode(word:str):
#     print(word[::2])
#     return word[::2]+word[1::2][::-1]

# print(decode("qwertyuio"))



# def check_info(arr):
#     checkNum=len(arr[0])
#     checkSum=""
#     for i in arr:
#         if (len(i)<=checkNum):
#             checkNum=len(i)
#             checkSum=i
#     return checkSum
# print(check_info(['hi','qwerty','say','l']))



# def number_to_words(n):
#     f={1:'one', 2:"two",3:'three', 4:"four",5:'five', 6:"six",7:'seven', 8:"eight",9:'nine', 
#     }
#     l={10:'ten', 20:"twenty",30:'thirty', 40:"fourthy",50:'fifty', 60:"sixty",70:'seventy', 80:"eight",90:'ninety', 
#     }
#     s={11:'eleven', 12:"twelve",13:'thirteen', 14:"fourteen",15:'fivteen', 16:"sixteen",17:'seventeen', 18:"eighteen",19:'nineteen', 
#     }

#     n1=n%10
#     n2=n-n1
#     if n<10:
#         return f.get(n)
#     elif 20 > n > 10:
#         return s.get(n)
#     elif n>=10 and n2==0:
#         return l.get(n)
#     else:
#         return l.get(n2)+' '+f.get(n1)
# print(number_to_words(33))



# def take_away(text:str):
#     split_text=text.split(' ')
#     store=[]
#     for i in split_text:
#         if i.isalpha():
#             i=i[1:]+i[0]+'ay'
#             store.append(i)
#             return ' '.join(store)
#         else:
#             return ' '.join(store)


# print(take_away('QWERTYU'))





# x='Bekzod Rashidov'
# first,second=x.split()
# print({'first':first}, {'second':second} )


# class MyFirstClass:
#     pass

# class MySecondClass:
#     pass

# class MyMainClass:

#     def my_first_function(self):
#         return None

#     def my_second_function(self):
#         return None


# def calculate_varieance(number_list):
#     sum_list=0
#     for number in number_list:
#         sum_list+=number
#     mean=sum_list/len(number_list)
#     print(mean)

#     sum_squares=0
#     for num in number_list:
#         sum_squares+=num**2
#     # print(sum_squares)
#     mean_squares=sum_squares/len(number_list)
#     return mean_squares-mean**2

# print(calculate_varieance([78,44,11,23,45]))


# my_bool=4>3
# if my_bool==True:
#     print('4 and 3')

# if my_bool:
#     print('4 and 3')


# def past(h=360000,m=60000,s=1000):
#     # return h * 60 * 60 * 1000
#     return s *100
# print(past())



def positive_sum(arr):
    sum=0
    for i in arr:
        if i>0:
            sum+=i
    return sum
print(positive_sum([4,5,-1,2,-100,-23,-22,110,]))


# rock  scissors
# def rps(p1,p2):
#     if p1=='rock' and p2=='scissors':
#         return f'Player one won! {p1}'
#     elif p1=='scissors' and p2=='rock':
#         return f'Player second won! {p2}'
#     else:
#         return 'Draw'
# print(rps('rock','rock'))



def filter_info(obj):
    my_list=[]
    for info in obj:
        if isinstance(info,str):
            my_list.append(info)
        if isinstance(info,bool):
            my_list.append(info)
    return my_list
print(filter_info([4,5,'Bekzod',-1,2,-100,'Rashidpov',-23,-22,110,]))



def is_isogram(string):
    a=string.lower()
    print(a)    
    if string:
        for i in string:
            if a.count(i)>1 and isinstance(i,(str,int)):
                return False
            elif i.upper()==i:
                # print(i.upper())
                return False
            else:
                return True
    else:
        return True
print(is_isogram('Bekzod'))