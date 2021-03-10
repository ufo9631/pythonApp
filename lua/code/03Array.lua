-- 数组的索引是从1开始
-- arr={1,2,3,4,"hello"}
-- for key, value in pairs(arr) do
--   print(key,value)
-- end

arr={}
for i = 1, 100 do
 table.insert(arr,1,i)
end

for key, value in pairs(arr) do
 print(key,value)
end

--查看数组长度
 -- print(table.maxn(arr)) --新版lua已经不支持