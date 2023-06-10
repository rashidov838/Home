# import re

# titles = 'Middle JavaScript react'

# js={
#     "JavaScript":{
#         "javascript",
#         "AngularJS",
#         "react",
#         " angular",
#         "angularjs "
#     }
# }
# # ("javascript","AngularJS","react","angular","angularjs")

# mapper_string="|".join([reg_ex for reg_ex in js["JavaScript"]])

# result=re.finditer(mapper_string,titles,re.IGNORECASE)
# print(next(result))
# print(next(result))


def plus(num):
    return num+5


if __name__=="__main__":
    # assert plus(4) == 9
    # assert plus("a") ==10
    print(plus(6))
    print(plus(-6))
    print(plus("6"))
    print(plus("a"))






