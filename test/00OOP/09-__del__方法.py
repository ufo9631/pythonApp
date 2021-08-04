import  sys
class Dog:

    def __del__(self): #当对象销毁的时候自动调用
        print("---------英雄Over----------")

dog1=Dog()
dog2=dog1

print(sys.getrefcount(dog1)) #测量对象的引用个数

del dog1

print("=====11111111=====")

