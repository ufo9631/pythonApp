age=17
if age<18:
    print("去叫家长把，孩纸")

gender="男"
if gender=="女":
    print("美女 你好！")
else:
    print("吔屎啊你")
#score=input("请输入分数：")
#score=int(score)  #字符串转int
#print(score)
#if score>=90:
#    print("优秀")
#elif score>80 and score<90:
#    print("良")

#python 没有switch-case

'''
  for 变量 in 序列：
    语句
'''
for name in ['zhangsan','lisi','wangwu']:
    print(name)

for i in range(1,11):
    print(i)

# for --else
for name in []:
    pass  #pass占位符 ，什么都不实现用pass站位
else:
    print("循环结束")


#循环结束 break,contineu,pass
#break 结束整个循环
