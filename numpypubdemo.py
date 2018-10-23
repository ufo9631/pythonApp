import numpy as np #  as 
#创建数组
list1=[1,3,5,-2,0,-9]
list2=[2,4,-3,-7,1,-7]
list3=[[2,5,0],[11,3,4]]
list4=[[3,-1,8],[9,-3,9]]

arr0=np.array(list1)
arr1=np.array(list3) #创建数组

arr2=np.arange(1,10,2)# 创建一个1为起点10为终点之间每个数字间隔2的数组
arr3=np.linspace(1,10,2) #1到10 区间2等分
arr_zero=np.zeros((3,4)) #创建3行4列全为零的数组 zeros的参数是元组
arr_one=np.ones((3,3)) #创建3行3列全为1的数组 zeros的参数是元组
#print(arr_one*100) #全为100的数组
arr_eye=np.eye(4,4) #对角线全为1其它的全为0 ，两个参数指定行和列
#print(arr_eye)

#数组的索引和切片
#print(arr1[0])
#print(arr0[:3]) #切片 下标为0可以不写 做切片是左闭右开
#print(arr1[1:2,1:3]) #二维数组做切片


#2.通用函数运算
#print("sqrt: \r",np.sqrt(arr1))  #求平方根
#print("exp:\n",np.exp(arr1)) #以e为底
#print("maximum：\n ",np.maximum(arr0,np.array(list2))) #数组逐个数字两两做对比取最大的值，取最大的值组成新的数组 两个数组的数量必须一样

new_arr=np.where(np.array(list2)>0,1,0) #大于的置为1否则置为0
#print(new_arr)

new_arr1=np.unique(np.array([0,1,2,3,3,4,5,5,7])) #去重并排序
#print(new_arr1)

#数组作为文件的输入和输出
np.save('myarr',arr0) #把数组保存为文件文件的扩展名叫.npy
np.savez('myarrzip',a1=arr0,a2=arr1,a3=arr2,a4=arr3) #压缩保存多个数组，参数名需要使用指定名称，文件扩展名npz
new_arr2=np.load("myarr.npy") #从文件从转为数组
new_arrzip=np.load('myarrzip.npz')
#print(new_arrzip['a1'])#通过关键字来访问转换的数组
#print(new_arr2)

#线性代数的操作 矩阵
arr5=np.array(list3)
arr6=np.array(list4)
print("hstack横向合并", np.hstack([arr5,arr6]))
print("vstack横向合并", np.vstack([arr5,arr6]))
#矩阵的点乘
print('dot:\n',arr6.reshape(3,2).dot(arr5)) # arr6.reshape(3,2) 将矩阵变成 3*2

np.transpose() #行变列 列变行