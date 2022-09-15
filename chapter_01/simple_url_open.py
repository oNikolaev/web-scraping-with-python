from urllib.request import urlopen

def simple_url_open():
    url = "http://pythonscraping.com/pages/page1.html"
    html = urlopen(url)
    print(html.read())

if __name__ == '__main__':
    simple_url_open()