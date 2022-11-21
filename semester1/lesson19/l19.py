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
