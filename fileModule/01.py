#open函数
#open函数负责打开文件，带有很多参数
#第一个参数：必须有，文件的路径和名称
#mode:表明文件用什么方式打开
#r:以只读方式打开
#w:写方式打开，会覆盖以前的内容
#x:创建方式打开，如果文件已存在，报错
#a:append方式，以追加的方式对文件内容进行写入
#b:binary方式，以二进制方式写入
#t:文本方式打开
#+：可读写

f=open(r"test.txt","w") #f成为文件句柄 r的意思是不需要转义字符串
f.close()#文件打开必须关闭

#with语句
#with语句使用的技术是一种成为上下文管理协议的技术
#自动判断文件的作用于，自动关闭不再使用的打开的文件句柄

#with语句案例
with open(r"test01.txt",'r') as f:
    pass
    #下面语句块开始对文件f进行操作
    #在本模块中不需要使用close关闭文件f

#with案例
with open(r"test01.txt",'r') as f:
    #按行读取内容
    strline=f.readline()
    #此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline=f.readline()

#list能用打开的文件作为参数，把文件内每一个行内容作为一个元素
with open(r"test01.txt",'r') as f:
    l=list(f)#以打开的文件f作为参数，创建列表
    for line in l:
        print(line)

#read是按字符读取文件内容
#允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
#否则，从当前位置读取指定个数字符
with open(r"test01.txt",'r') as f:
    strChar=f.read(1)
    print(len(strChar))
    print(strChar)

#seek (offset,from)
#移动文件的读取位置，也叫读取指针
#from的取值范围
#0：从文件头开始偏移
#1：从文件当前位置开始偏移
#2：从文件末尾开始偏移
#移动的单位是字节（byte）


#seek案例
#打开文件后，从第五个字节开始读取
with open(r"test01.txt",'r') as f:
    #seek移动单位是字节
    f.seek(4,0)
    strChar=f.read()
    print(strChar)


#案例
#打开文件，三个字符一组，显示在屏幕上
#读取一次，休息一秒钟
import  time
with open(r"test01.txt",'r') as f:
    strChar=f.read(3) #read参数的单位是字符，可以理解成一个汉字就是一个字符
    while strChar:
        print(strChar)
      #  time.sleep(1)
        strChar=f.read(3)

#tell函数：用来显示文件读写指针的当前位置
with open(r"test01.txt",'r') as f:
    strChar=f.read(3)
    pos=f.tell()
    while strChar:
        print(pos)
        print(strChar)
        strChar=f.read(3)
        pos=f.tell()

#文件的写操作
#write(str):把字符串写入文件
#writeline(str):把字符串按行写入文件
#区别：
#write函数参数只能是字符串
#writeline参数可以写入很多行，参数可以是list格式

#write案例
with open(r"test01.txt",'a') as f:
    f.write("hahahahaha,\n xixixixiix")

with open(r"test01.txt",'a') as f:
    f.writelines("hahahahaha")
    f.writelines("xixixixiix")

l=["i","love","vic"]
with open(r"test01.txt",'a') as f:
    f.writelines(l)