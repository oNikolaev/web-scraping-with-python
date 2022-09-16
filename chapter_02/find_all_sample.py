from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def find_all_sample():
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bsObj = BeautifulSoup(html, features="html.parser")

    nameList = bsObj.findAll("span", {"class": "green"})
    for name in nameList:
        print(name.get_text())


if __name__ == '__main__':
    find_all_sample()
