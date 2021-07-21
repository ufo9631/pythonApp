# 字典
#info={键:值,键:值}

info={"name":"张三"}
info["age"]=18
print(info)
del info["age"] #删除 age的key

info.get("age") #取值 key不存在时程序不会崩溃