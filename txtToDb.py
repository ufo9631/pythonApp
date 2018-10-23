

nameList=[]
scoreList=[]
countryList=[]
def readTxt():
    txtFile=open('result.txt','r',encoding='utf-8')
    #文件读取 read(),readline(),readlines()
    line=txtFile.readline()
    while line: #表示line有值
        str=line.split() #不指定分隔符  默认使用空格
        name=str[0].split(':')[1]
        score=str[1].split(':')[1]
        country=str[2].split(':')[1]
        nameList.append(name)
        scoreList.append(score)
        countryList.append(country)
        line=txtFile.readline() #读取下一行
    txtFile.close()

readTxt()