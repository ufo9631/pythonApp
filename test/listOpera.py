#list 增删改查
names=['老王','老李','老刘']
names.append('老赵') #添加到list最后
print(names)

# names.insert(位置，要添加的内容)
names.insert(0,'老陈')
print(names)

names.insert(2,'老汪')
print(names)

names2=['葫芦娃','叮当猫','蜘蛛侠']

names3=names+names2;
print(names3)

names.extend(names3) #将 names3合并到names
print(names)

names.pop()  #将最后一个删除 并返回删除的元素
names.remove('老王') #根据内容来删除
del names[0]  #删除指定下标的元素