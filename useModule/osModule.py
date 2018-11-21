#os 操作系统相关
#跟操作系统相关，主要是文件操作
#与系统相关的操作，主要包含三个模块里
#os,操作系统目录相关
#os.path 系统路径相关操作
#shutil,高级文件操作，目录树的操作，文件赋值，删除，移动
#getcwd()获取当前的工作目录
#格式：os.getcwd()
#返回值：当前工作目录的字符串
#当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
import  os
mydir=os.getcwd()
print(mydir)

#chdir()改变当前的工作目录
#格式：os.chdir(路径)
#返回值

#listdir()获取一个目录中所有子目录和文件的名称列表
#格式：os.listdir(路径)
#返回值：所有子目录和文件名称的列表
ld=os.listdir()
print(ld)

#makedirs()递归创建文件夹
#格式：os.makedirs(递归路径)
#返回值：无
#递归路径：多个文件夹层层包含的路径就是递归路径

#system()运行系统shell命令
#格式：os.system(系统命令)
#返回值：打开一个shell或者终端界面
#ls是列出当前文件和文件夹的系统命令
#一般推荐使用subprocess代替
rst=os.system("dir")
print(rst)

#getenv()获取指定的系统环境变量值
#格式：os.getenv('环境变量名')
#返回值：指定环境变量名对应的值
rst=os.getenv("path")
print(rst)

#exit()退出当前程序
#格式exit()
#返回值：无


#值部分


#os.cudir:current dir 当前目录
#os.pardir:parent dir 父亲目录
#os.sep:当前系统的路径分隔符
#os.linesep:当前系统的路径的换行符
#os.name:当前系统名称
print(os.pardir)
print(os.curdir)
print(os.linesep)
print(os.name) #windows的名字是nt  mac，linux,unix是posix

#os.path模块，跟路径相关的模块
#abspath()将路径转化为绝对路径
#格式 os.path.abspath("路径")
#返回值：路径的绝对路径形式
import  os.path as op
abs=op.abspath('.')
print(abs)

#basename()获取路径中文件名部分
#格式 os.path.basename("路径")
#返回值：文件名部分路径
print(op.basename("I:\PythonApp\App1\pythonApp"))

#join()将多个路径拼接成一个路径
#格式 os.path.join(路径1，路径2，路径3)
#返回值：组合之后的新路径字符串
bd="I:\PythonApp"
fn="hah.dd"
p=op.join(bd,fn)
print(p)

#split()将路径切割为文件夹部分和当前文件部分
#格式：os.path.split(路径)
#返回值：路径和文件名组成的元组
t=op.split("I:\PythonApp\App1\pythonApp")
print(t)
b,d=op.split("I:\PythonApp\App1\pythonApp")
print(b,d)

#isdir()检测是否是目录
#格式：os.path.isdir(路径)
#返回值：布尔值
rst=op.isdir("I:\PythonApp\App1")
print(rst)

#exists() 检测文件或者目录是否存在
#格式 os.path.exists(路径)
#返回值：布尔值
e=op.exists("I:\PythonApp")
print(e)


#shutil模块
#copy()复制文件
#格式 shutil.copy(来源路径，目标路径)
#返回值：返回目标路径
#拷贝的同时，可以给文件重命名
import shutil

rst=shutil.copy("I:\\PythonApp\\App1\\pythonApp\\1.txt","I:\\PythonApp\\App1\\pythonApp\\copy\\2.txt")
print(rst)

#copy2() 复制文件，保留元数据（文件信息）
#格式：shutil.copy(来源路径，目标路径)
#返回值：返回目标路径
#注意：copy和copy2的唯一区别在于 copy2复制文件时尽量保留元数据


#copyfile()将一个文件中的内容复制到另外一个文件中
#格式 shutil.copyfile(原路径，目标路径)
#返回值：目标文件路径

rst=shutil.copyfile("I:\\PythonApp\\App1\\pythonApp\\1.txt","I:\\PythonApp\\App1\\pythonApp\\copy\\3.txt")
print(rst)

#move()移动文件/文件夹
#格式：shutil.move(原路径，目标路径)
#返回值：目标路径
# shutil.move("I:\\PythonApp\\App1\\pythonApp\\4.txt","I:\\PythonApp\\App1\\pythonApp\\copy\\")

#归档和压缩
#归档：把多个文件或者文件夹合并到一个文件当中
#压缩：用算法把多个文件或文件夹无损或有损合并到一个文件当中

#归档操作 make_archive()归档操作
#格式：shutil.make_archive("归档之后的目录和文件名"，"后缀"，"需要归档的文件夹")
#返回值：归档之后的地址

rst=shutil.make_archive("I:\\PythonApp\\App1\\pythonApp","zip","I:\\PythonApp\\App1\\pythonApp\\copy")
print(rst)

#unpack_archive()解包操作
#格式 shutil.unpack_archive("归档文件地址"，"解包之后的地址")
#返回解包之后的地址


#zip- 压缩包
import zipfile
#zipfile.ZipFile
zf=zipfile.ZipFile("I:\\PythonApp\\App1\\pythonApp\\copy.zip")

#random 生成随机数

#choice()随机返回序列中的某个值

import  random
l=[str(i)+"hahah" for i in range(10)]
rst=random.choice(l)
print(rst)

#shuffle()随机打乱列表

l1=[i for i in range(10)]
print(l1)

random.shuffle(l1)
print(l1)

print(random.randint(0,100)) #随机生成一个整数 包含0 也包含100