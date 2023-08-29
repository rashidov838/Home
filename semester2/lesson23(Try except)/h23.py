def has_unique_chars(string):
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if(string[i]==string[j]):
                return False
    return True

print(has_unique_chars("abcdef"))
print(has_unique_chars("++-"))
print(has_unique_chars("  nAa"))



def solution(number):
    total_sum=0
    for i in range(number):
        if(i%3==0 or i%5==0):
            total_sum+=i
    print(total_sum)

print(solution(4))



name=['tyrytr','qw','sdf','bekzod','sabina']
print(filter(lambda x : next(x),iter(name)))

a=[2,1]
print(next(iter(a)))