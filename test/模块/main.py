import sendmsg  #导入模块的时候  模块会先从头到尾执行一遍
import recvmsg

sendmsg.test1()
sendmsg.test2()
recvmsg.test1()



#import sendmsg  #import 先搜索当前路径，当前路径找不到会去系统的指定路径搜索
#sendmsg.test1()

#import sendmsg as sd #取别名
# sd.test1()

#from sendmsg import test1
#test1()

#from sendmsg import test1,test2
#from sendmsg import * #*星号表示导出所有方法
#from recvmsg import * #后面引入的会覆盖前面的方法
#test1()
#test2()