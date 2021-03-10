function clone(tab)
    local ins={}
    for key, value in pairs(tab) do
        ins[key]=value
    end
    return ins
end


function copy(dist,tab)
    for key, value in pairs(tab) do
        dist[key]=value
    end
end


People={}
function People.sayHi(self1)
 print("hello world"..self1.name)
end
-- People.sayHi=function ()
--   print("people say hi")
-- end

People.new=function (name)
   local self=clone(People)
   self.name=name
   return self
end



-- local p=clone(People)
-- p.sayHi()


local p=People.new("zhangsan")
p.sayHi(p)
p:sayHi()  -- 这两种方法执行的是一样， p:sayHi()会默认把实例当做第一个参数传递进去


-- 类的继承
Man={}
Man.new=function (name)
    local self=People.new(name)
    copy(self,Man)
    return self
end

Man.sayHello=function ()
    print("man say hello")
end

Man.sayHi=function (self)
    print("man say hi---"..self.name)
end

local m=Man.new("wangwu")
m:sayHello()
m:sayHi()
