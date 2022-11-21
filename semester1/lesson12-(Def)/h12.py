# Exercise1
# def make_upper_case():
#     a=input()
#     i=a.upper()
#     return a.upper()
# print(make_upper_case())
# Exercise2
def greet_qwe():
    return 2**4
print(greet_qwe())


def square(x):
    print(x**2)
square(55)

def qwe(a,s):
    print(a*s)
qwe(6,5)
def even(a):
    if a%2==0:
        print(a,'even')
    else:
        print(a,'odd')
even(9)
for i in range(4,18):
    even(i)

def factorial(n):
    pr=1
    for i in range(2,n+1):
        pr=pr*i
    print(pr)
