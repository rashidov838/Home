import datetime


def find_duplicate_values(d):
    dups = {}
    unique_values = set()
    for post in posts:
        for k, v in post.items():
            if v in unique_values:
                dups[k] = v
            else:
                unique_values.add(v)
    print(dups.items())
    # print(unique_values)
    
 
posts = [
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
    },
    {
        'tags': 'django, hiking',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
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
    },
]

        
find_duplicate_values(posts)