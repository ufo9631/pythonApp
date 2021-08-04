f=open("haha.txt","w")
f.write("hahaha")
f.close()

f=open("haha.txt","r")
print(f.read(1)) #1表示读一个字节
print(f.read(1)) #
print(f.read())
f.close()