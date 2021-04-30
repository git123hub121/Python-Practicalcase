#求和函数累加
def sum(a,n):
    result, t=0, 0
    for i in range(n):
        t=t*10+a
        result+=t
    return result

a=int(input("输入a:"))        
n=int(input("输入n:"))
print(sum(a,n))

def f(x):
    if x==1:
        return 1
    else:
        return(f(x-1)+x*x)
print(f(5))

#递归函数
b=input("输入a:")
print(b)               

#调用模块1
import math
print("50的平方根：",math.sqrt(50))

#调用模块1
from math import *
print("64的平方根：",math.sqrt(64))

