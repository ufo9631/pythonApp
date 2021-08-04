class Dog(object):
    def __init__(self):
        print("-------init方法--------")

    def __del__(self):
        print("----del方法----------")
    def __str__(self):
        print("----str方法-------")
        return "对象的描述"
    def __new__(cls):#cls 此时是Dog指向的那个类对象
        print(id(cls))
        print("-----New方法---------")
        return object.__new__(cls)

print(id(Dog))
xtq=Dog() #这个动作做了三件事，1-调用__new__方法来创建对象，2-调用__init__()方法