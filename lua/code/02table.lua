Config={} --新建空的表
Config.word="hello world"
Config.num=100
Config["name"]="zhangsan"
print(Config.name)
print(Config.word)
print(Config["name"])


Config1={hello="hello lua",world="World"}
print(Config1.world)

--遍历表
for key,var in pairs(Config1) do
   print(key,var)
end