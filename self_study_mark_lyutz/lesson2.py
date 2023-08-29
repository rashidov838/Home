import re

"""Групировка"""
# match=re.match('Hello[\t]*(.*)world',"Hello Python world")
# print(match.group())
# print(match.group(1))


# match=re.match('[/:](.*)[/:](.*)[/:](.*)','/user/hoome:lumerqe')
# print(match.groups())



# match=re.match('[/')



"""                                     Списки

    Объект списка Python является наиболее общей последовательностью, предлагаемой
    языком. Списки представляют собой позиционно упорядоченные коллекции объектов
    произвольных типов и не имеют фиксированных размеров. Кроме того, они изменяе
    мы — в отличие от строк списки можно модифицировать на месте путем присваивания
    по смещениям и вызова разнообразных списковых методов. Соответственно они пре
    доставляют очень гибкий инструмент для представления произвольных коллекций —
    перечня файлов в каталоге, сотрудников в компании, сообщений в ящике входящей
    почты и т.д.
    
"""

# lst_info=[123,'spam',1.33]

# print(len(lst_info))
# print(lst_info[0])
# print(lst_info[:-1])
# print(lst_info+[4,5,6,9])
# print(lst_info*2)

# print(lst_info.append('Kola'))
# print(lst_info.pop(2))

# data=['bb','aa','cc']
# data.sort()
# print(data)


# data.reverse()
# print(data)


"""     Вложение:

        Одна приятная особенность основных типов данных Python заключается в том,
        что они поддерживают произвольное вложение — мы можем вкладывать их в любой
        комбинации и на любую желаемую глубину. Скажем, у нас может быть список, кото
        рый содержит словарь, содержащий еще один список, и т,д. Одно из прямых приме
        нений такой возможности связано с представлением в Python матриц, или “многомер
        ных массивов”. Список с вложенными списками пригоден для базовых приложений
        (в строках 2 и 3 вы получите приглашение . . . при работе в некоторых интерфейсах,
        но не в IDLE):

"""

# data=[[1,2,3],[8,90,32],[9,4,5]]
# print(data[1][2])

# col12=[row[1] for row in data]
# print(col12)

# col13=[ row[1] for row in data if row[1]%2==0]
# print(col13)


# diagonal_from_matrix=[data[i][i] for i in [0,1,2]]
# print(diagonal_from_matrix)


# doubles=[c*2 for c in 'spam']
# print(doubles)

"""Range"""
# print(list(range(4)))
# print(list(range(-6,7,2)))


# data=[[x**2,x**3] for x in range(4)]
# print(data)

# data=[[x,x/2,x*2] for x in range(-6,7,2)]
# print(data)


# data=[[1,2,3],[8,90,32],[9,4,5]]
# generator=(sum(row) for row in data)
# print(next(generator))
# print(next(generator))
# print(next(generator))

# print(list(map(sum,data)))

# print(list(sum(row) for row in data))



# print({i:sum(data[i]) for i in range(3)})

print([ord(x) for x in 'QWERTYU'])   # Список порядковых чисел для символов


"""
                                    Словари
Словари Python — нечто совершенно иное; они вообще не являются последователь
ностями и взамен известны как отображения. Отображения также представляют собой
коллекции других объектов, но они хранят объекты по ключам, а не по относитель
ным позициям. В действительности отображения не поддерживают какой-либо надеж
ный порядок слева направо; они просто отображают ключи на связанные значения.
Словари — единственный тип отображения в наборе основных объектов Python — яв
ляются изменяемыми’, как и списки, их можно модифицировать на месте и они способ
ны увеличиваться и уменьшаться по требованию. Наконец, подобно спискам слова
ри — это гибкий инструмент для представления коллекций, но их мнемонические ключи
лучше подходят, когда элементы коллекции именованы или помечены, скажем, как
поля в записи базы данных

"""



# data = {'food': 'eggplant', 'quantity': 4, 'color': 'pink'}
# data['quantity']+=1
# print(data)

#1
# data={}

# data['name']="Bekzod"
# data['job']="administrator"
# data['age']=110
# print(data)

#2
# info=dict(name='Bobi',job='accounter',age=111)
# print(info)

# #3
# info_2=dict(zip(['name','level','skill'],['Komil',23,'foot']))
# print(info_2)


# rec={
#     'name':{'first':'Bob','last':'Rooney'},
#     'jobs':['dev','mgr'],
#     'age':40.5
# }


# print(rec['name'])

# rec['name']['last']='Bekzod'
# print(rec)
# print(rec['name']['last'])

# print(rec['jobs'][-1])

# rec['jobs'].append('front')
# print(rec['jobs'])

data_3={'a':1,'b':2,'c':3,'x':5}
if not 'f' in data_3:
    print('missing') 
    print('no, really....')


value=data_3.get('x')
print(value)


    
