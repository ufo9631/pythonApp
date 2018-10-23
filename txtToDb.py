
import pymysql
nameList=[]
scoreList=[]
countryList=[]
def readTxt():
    txtFile=open('result.txt','r',encoding='utf-8')
    #文件读取 read(),readline(),readlines()
    line=txtFile.readline()
    while line: #表示line有值
        str=line.split('\t') #不指定分隔符  默认使用空格
        name=str[0].split(':')[1]
        score=str[1].split(':')[1]
        country=str[2].split(':')[1]
        nameList.append(name)
        scoreList.append(score)
        countryList.append(country)
        line=txtFile.readline() #读取下一行
    txtFile.close()

readTxt()


'''
数据入库
mysqldb python2 不支持python3
pymysql 支持python3
mysql.connector --mysql官方发布
'''
def operDB():
    conn=pymysql.connect(user='root',password='Keytop:wabjtam!',host='localhost',port=5831,db='moivedb')
    myCursor=conn.cursor()
    sql="insert into movie(movieName,score,country)values('%s','%s','%s')" #占位符的方式
    for i in range(250):
        values=(nameList[i],scoreList[i],countryList[i])
        myCursor.execute(sql % values)
    conn.commit()
    conn.close()
#readTxt()
#operDB()
def getDb():
    conn=pymysql.connect(user='root',password='Keytop:wabjtam!',host='localhost',port=5831,db='moivedb')
    myCursor=conn.cursor()
    sqlSelect="select * from movie where score>9.2"
    myCursor.execute(sqlSelect)
    movies=myCursor.fetchall()  #fetchall 得到查询的结果集
    for movie in movies:
        print("name:",movie[1])
    conn.close()
getDb()

   