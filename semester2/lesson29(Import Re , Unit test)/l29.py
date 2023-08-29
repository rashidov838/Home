import re
"""LECTURE
  Manual test -  от руки проверять нужно
 Unit test -проверка кусок кода"""
titles = 'Middle JavaScript react'

js={
    "JavaScript":{
        "javascript",
        "AngularJS",
        "react",
        " angular",
        "angularjs "
    }
}
# ("javascript","AngularJS","react","angular","angularjs")

mapper_string="|".join([reg_ex for reg_ex in js["JavaScript"]])

# result=re.finditer(mapper_string,titles,re.IGNORECASE)
# print(next(result))
# print(next(result))


regexex=r"react|javascript|angular"
test_str="middle javascript react"
matches=re.findall(regexex,titles,re.IGNORECASE)
print(matches)


# for math in matches:
#     print("match", match.group())

# pattern=r"(^[a-zA-Z0-9$#@%]{6,}[0-9]$)"
# password='somejokehere9'


# name='Bekzod'
# pattern_name=r"(^[A-Za-z0-9$#@%]{,8}$)"
# result_2=re.fullmatch(pattern_name,name)
# print(result_2)

# email='bekzodr73.@gmail.com'
# pattern_email=r"(^[a-zA-z0-9.@]{,20}[a-zA-z]$)"
# result=re.fullmatch(pattern_email,email)
# print(result)

# pattern=r"(^[a-zA-Z0-9$#@%]{6,16}$)"
# password='bekr123#123'

# result=re.fullmatch(pattern,password)
# print(result)



# card_code='3647583465734283'
# pattern_card_code=r"(^[0-9]{,16}[0-9]$)"
# result=re.fullmatch(pattern_card_code,card_code)
# print(result)






def plus(num):
    try:
        return num+5
    except ValueError as err:
        return err

if __name__=="__main__":
  assert plus(4) == 9
  # assert plus("a") ==10
  print(plus(6))
  print(plus(-6))
  # print(plus("6"))
  # print(plus("a"))