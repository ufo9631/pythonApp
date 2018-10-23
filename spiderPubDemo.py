import urllib.request
from bs4 import BeautifulSoup
nameList=[]
scoreList=[]
countryList=[]
url='https://movie.douban.com/top250'
def getData(url): #根据url获取数据
    res=urllib.request.urlopen(url).read().decode()
    return res

def parseData(html): #分析数据
    soup=BeautifulSoup(html,'html.parser')  #转成html
    mZone=soup.find('ol')
    movieList=mZone.find_all('li')
    for movie in movieList:
        movieName=movie.find('span',attrs={'class':'title'}).getText()
        movieScore=movie.find('span',attrs={'class':'rating_num'}).getText()
        movieCountry=movie.find('p').getText().rstrip().split('/')[-2]  #rstrip()去掉右边的空格
        nameList.append(movieName)
        scoreList.append(movieScore)
        countryList.append(movieCountry)
    next_url=soup.find('span',attrs={'class':'next'}).find('a')     #下一页的超链接，获取a标签href的属性值
    if next_url:
        newUrl=url+next_url['href']
        html=getData(newUrl)
        parseData(html)
    return nameList,scoreList,countryList

def saveData(nameList,scoreList,countryList): #数据存储 存到txt文件
    resFile=open('result.txt','w',encoding='utf-8')
    for i in range(250): #1-249
        lineText='名字:'+nameList[i]+"\t得分:"+scoreList[i]+"\t国家:"+countryList[i]
        resFile.write(lineText+"\n")
    resFile.close()

myHtml=getData(url)
nameList,scoreList,countryList=parseData(myHtml)
saveData(nameList,scoreList,countryList)
