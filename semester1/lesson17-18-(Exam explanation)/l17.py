obj={
    'RACE':"oGRE",
    'age':'100',
    'skill':['Roar'],
}
if 'RACE' in obj and 'age' in obj and isinstance(obj['age'],int):
    print(obj['RACE'],obj['age'])
else:
    print('human')
def short_word(names):
    if names:
        length=len(names[0])
    else:
        return False
    for name in names[1:]:
        name_len=len(name)
        if name_len<length:
            length=name_len
        return length

name=['Bekzod','John','Gabriel']
result=short_word(['Bekzod','John','GAbriel'])
print(result)

# def encode(s:str)->str:
#     s=list(s)
#     total=''
#     'coderwars'
#     for i in range(len(s)):
#         if i%2==0:
#             total+=s[0]
#             s.pop(0)
#         else:
#             total+=s[-1]
#             s.pop(-1)
#         print(s,total)
#     return total
# print(encode('coderwars'))


# def decode(s:str)->str:
#     return s[::2]+s[1::2][::-1]
# print(decode("qwertyuio"))


# def resheniye(arr):
#     checkNum=len(arr[0])
#     checkSym=""
#     for i in arr:
#         if (len(i)<=checkNum):
#             checkNum=len(i)
#             checkSym=i
#     print(checkSym," - ",checkNum)
#     return checkNum

# arr=['hi','qwerty','say']
# print(resheniye(arr))


def  number_to_words(n):
    f={1:'one', 2:"two",3:'three', 4:"four",5:'five', 6:"six",7:'seven', 8:"eight",9:'nine', 
    }
    l={10:'ten', 20:"twenty",30:'thirty', 40:"fourthy",50:'fifty', 60:"sixty",70:'seventy', 80:"eight",90:'ninety', 
    }
    s={11:'eleven', 12:"twelve",13:'thirteen', 14:"fourteen",15:'fivteen', 16:"sixteen",17:'seventeen', 18:"eighteen",19:'nineteen', 
    }
    n1=n%10
    n2=n-n1
    if n<10:
        return f.get(n)
    elif 20 > n >10:
        return s.get(n)
    elif n>=10 and n2==0:
        return l.get(n)
    elif n>20:
        return l.get(n2)+' '+f.get(n1)

print(number_to_words(33))
def pig_it(text):
     tl = text.split(' ')
     store = []
     for i in tl:
        if i.isalpha():
             i = i[1:]+i[0] + 'ay'
             store.append(i)
             return ' '.join(store)
        else:
            return ' '.join(store)