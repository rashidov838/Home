def plus(num=0):
    try:
        if num:
            return int(num)+5
    except ValueError as err:
        return err

if __name__=="__main__":
    print(plus(5))