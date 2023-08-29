def validate_pin(pin):
    if (len(pin)==4 or len(pin)==6) and pin.isdigit():
        return True
    else:
        return False
print(validate_pin(".245"))
# [5, 10, 14]
# def odd_or_even(arr):
#     for i in arr:
#         if (i%2)==1:
#             return 'even'
#         if (i%2==0):
#             return 'odd'
#         else:
#             return 'even'
    
# print(odd_or_even([0, 1, 3]))
# # odd_or_even([0, 1, 2]), "odd")
# # test.assert_equals(odd_or_even([0, 1, 3]), "even")
# # test.assert_equals(odd_or_even([1023, 1, 2]), "even"
# ////
# def series_sum(n):
#     a= sum(1/(1+i*3) for i in range(n))
#     return "%.2f" % a
# print(series_sum(4))

# ////
# def to_jaden_case(string):
#     # return string.title()
#     return ' '.join(w.capitalize() for w in string.split())    
# quote = "How can mirrors be real if our eyes aren't real"
# print(to_jaden_case(quote))
# def square_digits(num):
#     a=list(str(num))
#     for i in a:
#         print(int(i)**2,end='')    

# 2 way
# # z = ''.join(str(int(i)**2) for i in str(num))
#     return int(z)
# square_digits(9119)
# def binary_array_to_number(arr):
#     if arr[0]==0 and arr[1]==0 and  arr[2]==0 and arr[3]==1:
#         return 1
#     if arr[0]==0 and arr[1]==0 and  arr[2]==1 and arr[3]==0:
#         return 2
#     if arr[0]==1 and arr[1]==1 and  arr[2]==1 and arr[3]==1:
#         return 15
#     if arr[0]==0 and arr[1]==1 and  arr[2]==1 and arr[3]==0:
#         return 1
#     else:
#         return f'Not correct {arr}'
# print(binary_array_to_number(([1,1,1,1])))
# test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
# test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
# test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
# test.assert_equals(binary_array_to_number([0,1,1,0]), 6)
#  def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0]+numbers[1]
# print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))


# def descending_order(num):
#     descending=''.join(sorted(str(num),reverse=True))
#     return int(descending)
# print(descending_order(15))
# test.assert_equals(descending_order(0), 0)
# test.assert_equals(descending_order(15), 51)
# test.assert_equals(descending_order(123456789), 987654321)

# import random 
# def random_get(length,minimm=1,maximum=100):
#     numbrs=[]
#     for i in range(length):
#         numbrs.append(random.randint(minimm,maximum))
#     return numbrs


# print(random_get(50))
# print(random_get(5,-50,34))
# print(random_get(10,maximum=500))
# print(random_get(10,10000,20000))

# # def add_binary(a,b):
# #     return '{0:b}'.format(a + b)


# def complementary_strand_find(dna_strand):
#     complementary_strand = ""
#     for base in dna_strand:
#         if base == "A" :
#             complementary_strand += "T"
#         elif base == "T" :
#             complementary_strand += "A"
 
#         elif base == "U" :
#             complementary_strand += "A"
 
#         elif base == "G" :
#             complementary_strand += "C"
 
#         elif base == "C" :
#             complementary_strand += "G"
 
#         elif base == "Y" :
#             complementary_strand += "R"
 
#         elif base == "R" :
#             complementary_strand += "Y"
 
#         else :
#             print("Wrong input")
#             complementary_strand = None
#             break
#     return complementary_strand
# # test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
# # test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
# # test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")
# # "ATTGC" --> "TAACG"
# # "GTAT" --> "CATA"
# # https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
# def is_square(n):  
#     if n**2==n*n:
#         return True 
#     else:
#         return False
# print(is_square(-1))
# # isSquare (-1) // => false
# # isSquare   3  // => false
# # isSquare   4  // => true
# # isSquare  25  // => true
# # isSquare  26  // => false

# def min_max(lst):
#     a=[]
#     b=min(lst)
#     a.append(b)
#     c=max(lst)
#     a.append(c)
#     return a

# print(min_max( [1]))
# # [1,2,3,4,5] --> [1,5]
# # [2334454,5] --> [5,2334454]
# # [1]         --> [1,1]