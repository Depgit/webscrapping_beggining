from urllib.request import urlopen
html = urlopen('https://depblog.herokuapp.com/')
print(html.read().stringify())