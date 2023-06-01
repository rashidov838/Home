print(__name__)
ITEMS={
    'dog':1,
    'cat':3,
    'crocodile':3
}

def buy(animal):
    for item,count in ITEMS.items():
        if item==animal and count:
            ITEMS[item]-=1
            return animal
    return "We dont have animal"


if __name__=='__main__':
    print(buy('cat'))