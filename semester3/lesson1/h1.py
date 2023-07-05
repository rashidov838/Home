import requests
from bs4 import BeautifulSoup
import re
import pprint
ycombinator_news=[]
def func_for_news():
    url="https://news.ycombinator.com/"
    for num in range(10):
        all_url=url+("?p=")+str(num)
        res=requests.get(all_url)
        soup=BeautifulSoup(res.text,'html.parser')
    lst_title=[]
    for tlt in soup.select(".titleline"):
        answer_title=tlt.a.text
        lst_title.append(answer_title)

    lst_link=[]
    for link in soup.select(".titleline>a"):
        answer_link=link.get('href')
        lst_link.append(answer_link)


    lst_score=[]
    for scr in soup.select(".subline"):
        answer_scr=scr.span.text
        lst_score.append(answer_scr)

    while True :
        try:
            if (lst_title[0] and lst_link[0] and lst_score[0]) not in ycombinator_news:
                ycombinator_news.append({
                            "title":lst_title[0],
                            "link_article":lst_link[0],
                            "score":lst_score[0]
                        })
                lst_title.pop(0)
                lst_link.pop(0)
                lst_score.pop(0)
                pprint.pp(ycombinator_news)
        except Exception:
            break
print(func_for_news())