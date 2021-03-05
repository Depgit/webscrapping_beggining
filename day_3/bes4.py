#for parsing url
from urllib.request import urlopen

from bs4 import BeautifulSoup


html = urlopen('https://depblog.herokuapp.com/')
bsObj = BeautifulSoup(html.read(), 'html5lib')
element = bsObj.select('.card-body')# selecting element by id on the link

# element is a list of objects selected by id (card-body ) on the given site
for i in element:
    print(i, end=',')