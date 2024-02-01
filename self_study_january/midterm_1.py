name='Bekzod'
surname='Rashidov'
age=21
text1='My name is {}, surname is {} and age: {}'.format(name,surname,age)
print(text1)

text2='My name is {1}, surname is {0} and age: {2}'.format(name,surname,age)
print(text2)

text3=f'My name is {name:<10},surname is {surname:5} and age is {age:<10}'
print(text3)

a=' '
print(len(a))

text="You've got that fire (fire).The flavor, the style (style)"
print(text.split('.'))