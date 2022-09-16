from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def find_refs():
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html, features="html.parser")

    # Выводятся все ссылки, в т.ч. и ссылки на боковой панели
    # for link in bsObj.findAll("a"):
    #     if 'href' in link.attrs:
    #         print(link.attrs['href'])

    # Выводится список URL-адресов связанных статей
    for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])


if __name__ == '__main__':
    find_refs()
