from abstest import my_abs,my_a
import math
v=my_abs(9)
print(v)
my_a('hello world')

#函数返回多个值
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

x,y=move(100,100,60,math.pi/6)
print('x={0},y={1}'.format(x,y))
