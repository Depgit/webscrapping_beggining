#for parsing url
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup



# try:
#     html = urlopen('https://depcraze.herokuapp.com')
#     # print(html.read())
#     bsObj = BeautifulSoup(html.read(), 'lxml')
#     print(bsObj.sometag.good)#just checking that wheather this tag exist or not

# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print("The server could not find")
# except AttributeError as e:
#     print("Tag was not found!")
# else:
#     print("it worked!")
# print("fine")



def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), 'html5lib')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle('https://depblog.herokuapp.com/')
if title is None:
    print("title could not be found!")
else:
    print(title)
