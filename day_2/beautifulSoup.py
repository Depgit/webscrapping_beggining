#for working with urls use this
from urllib.request import urlopen

# for parsing data
from bs4 import BeautifulSoup

html = urlopen('https://depblog.herokuapp.com/')
bsObj = BeautifulSoup(html.read(), 'html5lib')# html5lib is a way to parse HTML

print((bsObj.html))