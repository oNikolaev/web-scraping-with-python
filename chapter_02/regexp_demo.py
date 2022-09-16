from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def regexp_demo():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html, features="html.parser")

    images =bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})

    for image in images:
        print(image["src"])

if __name__ == '__main__':
    regexp_demo()