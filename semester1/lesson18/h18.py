# [1,2,1,1,1,1,1]
# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x

# def divisors(n):
#     result = []
#     for i in range(1, n//2 + 1):
#         if n % i == 0:
#             result.append(i)
#     result.append(n)
#     return result
# print(divisors(24))            

# def is_triangle(a, b, c):
#     return (a<b+c) and (b<a+c) and (c<a+b)
# print(is_triangle(5,6,7))


# def compress_string(line):
#     new_string=""
#     count=1
#     for i in range(len(line)):
#         j = i
#         j+=1
#         try:
#             if line[i]==line[j]:
#                 count+=1
#             else:
#                 new_string+=line[i]
#                 new_string+=str(count)
#                 count=1
#         except:
#             new_string+=line[i]
#             j=i
#             j-=i
#             if line[i]==line[j]:
#                 new_string+=str(count)
#             else:
#                 new_string+='1'
#     if len(new_string)>len(line):
#         print(line) 
#     else:
#         print(new_string)
# string=input("")
# compress_string(string)


# #     test.expect(xo('xo'), 'True expected')
# # test.expect(xo('xo0'), 'True expected')
# # test.expect(not xo('xxxoo'), 'False expected')
# def xo(s):
#     char=list(s)
#     x_count=0
#     o_count=0
#     for i in char:
#             if i.lower()=='x':
#                 x_count+=1
#             elif i.lower()=='o':
#                 o_count+=1
#     return x_count==o_count

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
arr=[1,2,1,1,1,1,1]
stray(arr)
