mystr="hello world itcast and hahahahah"
print(mystr.find("zhangsan")) #返回找到值的索引，找不到返回-1
print(mystr.index("world")) # 要找的字符串必须是已存在的 否则会报错
print(mystr.rfind("hello")) # 从右边开始找
print(mystr.count("itcast"))# 统计个数
print(mystr.replace('world',"WORLD")) #替换
print(mystr.replace('world',"WORLD",1)) #替换 第三个参数表示替换的次数，没填表示全替换
print(mystr.split(" ")) #分割，分割是有消耗的，如果没传参数 那就按照不可见的字母进行切割（空格，制表符等）
print(mystr.capitalize()) #首字母改成大写
print(mystr.title()) #每个单词首字母都大写
print(mystr.startswith("张三")) #判断是否以某字符串开头
print(mystr.endswith("张三")) #判断是否以某字符串结尾
print(mystr.lower()) #转小写
print(mystr.upper()) #转大写
lyric="想带你一起去看大海"
print(lyric.center(50))#中间对齐
print(lyric.ljust(50)) #左对齐
print(lyric.rjust(50)) #右对齐
print(mystr.strip()) #去掉左右空格
print(mystr.lstrip()) #去掉左边空格
print(mystr.rstrip()) #去掉右边空格
print(mystr.partition("and")) #分割成三部分，str 前，str和 str后
print(mystr.rpartition("and")) #从右边开始匹配 and分割成三部分，str 前，str和 str后
file_content="123123\n123123\ns"
print(file_content.splitlines()) #按换行符\n进行切割
a="sdjflsdfkkkjls"
print(a.isalpha()) #判断是否春英文数字
print(a.isdigit()) #判断是否纯数字
print(a.isalnum()) #判断是否是数字和英文字母的组合
print(a.isspace()) #判断是否是纯空格
names=["aa","bb","cc"]
a="_"
print(a.join(names)) #以_连接在一起