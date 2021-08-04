print(range(10))
print(range(1,10,2))

a=[i for i in range(1,18)]
print(a)

b=[11 for i in range(1,18)]
print(b)

c=[i for i in range(10) if i%2==0]
print(c)

d=[i for i in range(3) for j in range(2)]
print(d)

#d列表描述
'''
相当于
 d=[]
  for i in range(3):
      for j in range(2):
          d.append((i,j))
'''


e=[(i,j) for i in range(3) for j in range(2)]
print(e)

f=[(i,j,k) for i in range(3) for j in range(2) for k in range(3)]
print(f)