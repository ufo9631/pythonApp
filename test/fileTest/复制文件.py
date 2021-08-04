# 1.获取要复制的文件名
old_file_name=input("请输入要复制的文件名(需要后缀):")

# 2.打开要复制的文件
f_read=open(old_file_name,"r")
oldFileArr=old_file_name.split(".")
new_file_name=oldFileArr[0]+"[复制]"+oldFileArr[1]
#3 创建一个新文件
f_write=open(new_file_name,"w")

#4 从old文件中读取数据，写入到new文件中
content=f_read.read()
f_write.write(content)

#5 关闭两个句柄
f_read.close()
f_write.close()