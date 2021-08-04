import sys
print(sys.argv)
sys.argv[0]
name =sys.argv[1]  # python 给程序传递参数.py laowang   sys.argv[1]就能接收到laowang这个参数
#name="laowang"
print("热烈欢迎%s的到来"%name)