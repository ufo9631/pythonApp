print("hello world")
-- 注释
num=100  --全局变量

local num1=100 --局部变量


function sayHello()
    print("hello world")
    -- body
end

sayHello()

function max(a,b)
    -- body
    if a>b then
        return a
    else
        return b
    end
end
print(max(1,4))

-- 循环
for var=1,100 do
 print(var)
end