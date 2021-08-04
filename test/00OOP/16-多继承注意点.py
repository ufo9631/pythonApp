class Base: #只要定义了类 默认继承了object
    def test(self):
        print("-----Base")

class A(Base):
    def test(self):
        print("-----------A")

    
class B(Base):
    def test(self):
        print("-----------B")


class C(A,B):
    def test(self):
        print("--------C")

c=C()
c.test()

print(C.__mro__)  #__mro__决定了一个方法调用搜索的顺序，如果在某一个类中找到调用的方法，那么就停止搜索 __mro__  C3算法
