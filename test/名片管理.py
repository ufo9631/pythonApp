#打印功能提示
print("="*50)
print("     名字关系系统1.0.0")
print("1:添加一个新的名字")
print("2:删除一个名字")
print("3:修改一个名字")
print("4:查询一个名字")
print("="*50)


names=[]
while True:
    num=int(input("请输入功能序号"))
    if num==1:
        name=input("请输入名字：")
        names.append(name)
        print(names)
        print("添加成功")
    elif num==2:
        name=input("请输入名字：")
        if name in names:
            names.remove(name)
            print("删除成功")
        else:
            print("名字不存在")     
    elif num==3:
        pass
    elif num==4:
        pass
    else:
        print("输入有误")
        break

