import requests
from bs4 import BeautifulSoup
import re
import pprint
ycombinator_news=[]
def func_for_news():
    url="https://news.ycombinator.com/"
    for num in range(1,11):
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




"""
https://ycombinator.com/
"""
import json
import requests
import time
import logging

from bs4 import BeautifulSoup
from pathlib import Path
from functools import wraps
from datetime import datetime


# time_counter decorator for counting time
def time_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(
            f"\n#######[TIME-RATE]####### {func.__name__} completed in {time.perf_counter()-start:8f} seconds.\n"
        )
        return result

    return wrapper


# logger decorator for presenting information about https
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            format=f"#-------[INFO]#######[{func.__name__}]-------# %(funcName)s %(asctime)s %(message)s",
            level=logging.DEBUG,
        )
        return func(*args, **kwargs)

    return wrapper


@logger
def api_check(url: str) -> BeautifulSoup:
    """
    Returns soup object if url is valid otherwise exception
    """
    try:
        response_txt = requests.get(url).text
        soup = BeautifulSoup(response_txt, "html.parser")
    except Exception as error:
        raise error

    return soup


def get_api_data(soup: BeautifulSoup) -> tuple | Exception:
    """
    Returns tuple of titles_link (titles and links) and score (points) of article
    """
    news_data = []

    try:
        titles_link = soup.select(
            ".titleline"
        )  # getting all tags with class called titleline
        points = soup.select(".score")  # getting all tags with class called score

        for point in points:
            for title in titles_link:
                if (
                    point["id"][6:] == title.parent.parent["id"]
                ):  # If an article point's id is equal to title's id
                    news_data.append(
                        {
                            "title": title.a.text,
                            "link_to_article": title.a["href"],
                            "score": int(point.text.split(" ")[0]),
                        }
                    )
                    break
    except AttributeError as error:
        raise error

    return news_data


def write_json(dictionary: dict | list) -> str | Exception:
    """
    Write dictionary data to json file
    """
    try:
        path = Path(__file__).parent / "data.json"
        written_time = datetime.now().strftime("%d day, %m month, %Y - %H:%M")

        dictionary = {
            "last update": written_time,
            "data": dictionary,
        }

        with open(path, "w") as json_file:
            json.dump(dictionary, json_file, indent=4)
    except FileNotFoundError as error:
        raise error


@time_counter
def get_ycombinator_news(url: str, pages: int = 10) -> list[dict] | dict:
    """
    Returns all hacker news from hacker https://news.ycombinator.com/ by sorting their score
    """
    ycombinator_news = []

    for i in range(1, pages + 1):
        try:
            soup = api_check(url + f"?p={i}")
            news_data = get_api_data(soup)
            ycombinator_news.extend(news_data)
        except TypeError as error:
            return error

    sorted_news = sorted(
        ycombinator_news, key=lambda dictionary: dictionary["score"], reverse=True
    )  

    return sorted_news
 

def main(prompt):
    url = "https://news.ycombinator.com/"
    news = get_ycombinator_news(url, prompt)

    write_json(news)
    print("Completed!", f"Written {len(news)} articles.")


if __name__ == "__main__":
    prompt = int(input("How many pages do you want to save? "))
    main(prompt)
