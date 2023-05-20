# def is_pangram(s):
#     return not set('abcdefghijklmnopqrstuvwxyz')-set(s.lower())

# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
# print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))

# https://www.codewars.com/kata/56853c44b295170b73000007/train/python
# [1, 4, 9, 16, 25, 36]
# [1, 2, 3, 4, 5, 6]), False)
# ([]), None)
# ([1, 4, 9, 16, 25]), True)
# ([1, 2, 4, 15]), False)

# def is_square(arr):
#     for i in arr:
#         if i<1:
#             return False
#         else:
#             for i in range(int(arr/2)+1):
#                 if (i*i)==arr:
#                     return True
#             return False

# print(is_square([1, 4, 9, 16, 25, 36]))


# def circles(x1,y1,radius1,x2,y2,radius2):
#     dis_x=x2-x1
#     dis_y=y2-y1
#     rad=radius1+radius2
#     if (dis_x*dis_x)+(dis_y*dis_y)<(rad*rad):
#         return True
#     else:
#         return False   

# print(circles(1, 1, 1, 1.1, 1.1, 0.1))
# print(circles(1, 1, 0.01, 1, 1.1, 0.01))


# def isVowel(ch):
#     return  ch.upper() in ['A', 'E', 'I', 'O', 'U','a','e','i','u','o']

# def get_count(sentence):
#     count=0
#     for i in range(len(sentence)):
#         if isVowel(str(i)):
#             count+=1
#     return count


# print(get_count("bcdfghjklmnpqrstvwxz  y"))


# from collections import Counter
# def get_count(sentence):
#     a=list(sentence)
#     dictt=Counter(a)
#     num=[]
#     for val,key in dictt.items():
#        num.append(key)
#     return sum(num)

# ---------------------------------------

# def find_outlier(integers):
#     odds=[x for x in integers if x%2!=0 ]
#     even=[x for x in integers if x%2==0]
#     return odds[0] if len(odds)<len(even) else even[0]
# print(find_outlier([2, 4, 6, 8, 10, 3]))

def recursive(data):
    total=0
    for li in data:
        total+=len(li)
    print(total)

recursive([2, [2 , 3, [[[[[[[[5]]]]]]]]]])

