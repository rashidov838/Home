# Inbuilt-in modules :Встроенные модулли

# import math
# import os


# from pathlib import Path,WindowsPath

#third-package modules: Сначала нужно скачать систему через интенрета потом можно использовать
# import pandas as pd
# from itertools import *

#my modules : где можно импортировать папки встроенные 
# import utils.shop as shp 
# print(__name__)


import datetime
from operator import itemgetter
posts = [
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 19),
    },
    {
        'tags': 'django, hiking',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 21),
    },
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 12),
    },
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 11),
    },
    {
        'tags': 'jazz',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 22),
    },
]
for post in posts:
    print(post['published'])
    # for k,l in post.items():
        




# >>> 
# >>> sorted_rooms = dict(sorted(rooms.items(), key=itemgetter(1)))
# >>> sorted_rooms
# {'Ocean': 'Rm 2000', 'Space': 'Rm 201', 'Big': 'Rm 30', 'Pink': 'Rm 403', 'Quail': 'Rm 500', 'Lime': 'Rm 503'}
 
