from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

def bs4_sample():
    url = "http://pythonscraping.com/pages/page1.html"
    # url = "http://pythonscraping.com/pages/page1111.html"

    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)

    if (html is None):
        print("URL is not found")

    bsObj = BeautifulSoup(html.read(), features="html.parser")

    print(bsObj.h1)
    print(bsObj.html.body.h1)
    print(bsObj.body.h1)
    print(bsObj.html.h1)

    try:
        badContent = bsObj.nonExistingTag.anotherTag
    except AttributeError as e:
        print("Tag was not found")
    else:
        if badContent == None:
            print("Tag was not found")
        else:
            print(badContent)

if __name__ == '__main__':
    bs4_sample()