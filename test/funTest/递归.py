
'''
i=1
result=1
while i<=4:
    result=result*i
    i+=1
print(result)
'''

def getNums(num):
    if num>1:
        return num*getNums(num-1)
    else:
        return num
result=getNums(4)
print(result)