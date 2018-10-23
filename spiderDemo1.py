import urllib.reqeust
def getData(url):
    req=urllib.request.urlopen(url).read().decode()
    print(req)

getData('https://movie.douban.com/top250')