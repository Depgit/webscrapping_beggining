from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://depblog.herokuapp.com/')
bsObj = BeautifulSoup(html.read(), 'lxml')

print(bsObj.html)