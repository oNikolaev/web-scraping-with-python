from urllib.request import urlopen
from bs4 import BeautifulSoup


def siblings_demo():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html, features="html.parser")

    print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())


if __name__ == '__main__':
    siblings_demo()
