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
        
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
arr=[1,2,1,1,1,1,1]
stray(arr)
