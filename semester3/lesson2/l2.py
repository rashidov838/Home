import requests
from bs4 import BeautifulSoup
from pprint import pprint
def parse_yombinator():
    result=[]
    for page in range(1,4):
        url=f'https://news.ycombinator.com/?p={page}'
        res=requests.get(url)
        soup=BeautifulSoup(res.text,"html.parser")
    titles=soup.find_all(class_='titleline')
    score_parents=soup.select(".subtext")
    for id, title in enumerate(titles):
        if score := score_parents[id].find(class_="score"):
            score=score.string.split()[0]
            result.append(
                {
                    "title":title.a["href"],
                    "link":title.a.string,
                    "score":score
                }
            )
        else:
            result.append(
                {
                    "title":title.a["href"],
                    "link":title.a.string,
                    "score":0
                }
            )
    return result

res=parse_yombinator()
print(res,len(res))