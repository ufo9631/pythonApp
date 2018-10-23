# -*- coding: utf-8 -*-
print("hello world")
#name=input("enter you name")
#print(name)
print("陈伟超")
print(10%3)


''' def test(d):
    if(d>10):
        print("true")
    else:
        print("FLASE")
'''
# test(11)

print(ord("中"))
print(chr(25991))

x=b'ABC' #python对bytes类型的数据用带b前缀的单引号活双引号表示
print("abc".encode('ascii')) #str 通过encode()方法可以编码为指定的bytes
print('中文'.encode('utf-8'))

#将bytes转为str 需要用到decode()方法  中文的bytes无法使用ascii编码  因为超过了ascii的编码范围
print(b"abc".decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print("字符串长度",len('abc'),"方法为len()")
