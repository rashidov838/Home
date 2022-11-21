def filter_list(l):
    a=[]
    for i in l:
        if isinstance(i,(int)):
            a.append(i)
    return  a 

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

# 1. git init- Пустое директории
#    git config --global core.editor "code --wait"
# 2.git config --global user.name "rashidov838"
# 3.git config --global user.email "bekzodrashidov73@gmail.com"
# 4.git config --list

