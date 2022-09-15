from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getTitle(url: str):
    result = ''

    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), features="html.parser")
        result = bsObj.body.h1
    except AttributeError as e:
        return None

    return result


if __name__ == '__main__':
    url = "http://pythonscraping.com/pages/page1.html"
    title = getTitle(url)
    if title == None:
        print("Title could not be found")
    else:
        print(title)
