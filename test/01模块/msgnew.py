__all__=["test1","test2","Test","num"] #表示import * 导入的模块,如果不写__all__ 那么 import * 会导入所有东西，如果写了__all__那么只会导入 __all__里的功能
def test1():
    print("------test1----1----")

def test2():
    print("------test2----2----")


num=100

class Test(object):
    pass