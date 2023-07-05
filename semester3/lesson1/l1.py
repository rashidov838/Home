import requests
from bs4 import BeautifulSoup
import re
import pprint


url="https://news.ycombinator.com/"
res=requests.get(url)

# with open('index.html','w') as file:
#     file.write(res.text)


# print(res.text)
# content=""
# with open('index.html') as file :
#     content=file.read()


soup=BeautifulSoup(res.text,'html.parser')
# soup=BeautifulSoup(content,'html.parser')
# print(soup.prettify())

# -----------------------------
# print(soup.title)

# print(soup.title.name)

# print(soup.title.string)

# print(soup.title.parent.name)
# -----------------------------
# print(soup.span)
# print(soup.span['class'])
# print(soup.span.attrs)
# print(soup.a.attrs)

# -----------------------------

# print(soup.find_all("a"))
# print(soup.find(id='link'))

# title=soup.find(class_='titleline')
# print(title.a.text)


# link_article=title.a['href']

# score=soup.find(class_='score')

# print(score.text.split()[0])






# ycombinator_news=[
#     {
#         "title":title.text,
#         'link_article':link_article,
#         "score":score.text.split()[0]
#     }
# ]
# print(ycombinator_news)
# -------------------------------------------------
# print(soup.select(".score"))
# print(soup.select(".titleline"))

# pprint.pp(soup.select(".titleline"))


# title=soup.select(".titleline>a")
# pprint.pp(title)



for link in soup.select(".titleline>a"):
    answer_link=link.get('href')



for tlt in soup.select(".titleline"):
    answer_title=tlt.a.text


for scr in soup.select(".subline"):
    answer_scr=scr.span.text
    ycombinator_news=[
        {
            "title":answer_title,
            'link_article':answer_link,
            "score":answer_scr
        }
    ]
    print(ycombinator_news)