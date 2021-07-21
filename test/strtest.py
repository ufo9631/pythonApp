l=[1,2,3,4,5]
print(1 in l)
print(1 not in l)

s="hell world{0}{1}".format(1,2)
print(s)
s1='name is %s,age is %d'%('张三',18)
print(s1)
print(s is s1)

print(s is not s1)

i=1
while i<2000:
    i=i+1;
    print(1,end="|")
    if i==10:
        break
i=0
while i<10:
    print(i,'\n')
    i=i+1
else:
    print('循环结束')
i=100
print(id(i))

print("hello"+"world")


print(len('abcdefg'))

s="hello world"
print(s[-1])
print(s[-2])

s="abcdefgABCDEFG"
print(s[1:3]) # 字符串切片
print(s[1:-2])
print(s[1:]) #冒号后面没写 就取到最后
print(s[2:-1:2])# 第二个冒号表示补偿长度  从2到-1 然后隔一个取一个
print(s[-1::-1]) #相当于字符串逆序输出 也可以缩写为 s[::-1]
