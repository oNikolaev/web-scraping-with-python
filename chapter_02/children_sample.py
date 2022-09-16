from urllib.request import urlopen
from bs4 import BeautifulSoup


def children_sample():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html, features="html.parser")

    for child in bsObj.find("table", {"id": "giftList"}).children:
        print(child)


if __name__ == '__main__':
    children_sample()
