使用python实现冒泡法排序从小到大

num = [int(i) for i in input("请输入10个数字\n").split(' ')]
for i in range(len(num)-1):
    for j in range(len(num)-i-1):
        if num[j] > num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]
for i in num:
    print(i)

实现找出特定的数
import math
for i in range(1,10000):
    a = int(math.sqrt(i+100))
    b = int(math.sqrt(i+268))
    if a*a == i+100 and b*b == i+268:
        print(i)

九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end='\t')
    print()
一行实现
print('\n'.join([' '.join(["%2s x%2s=%2s"%(j,i,j*i) for j in range(1,i+1)]) for i in range(1,10)]))
列外行内

#递归数列
a,b = 1,1
for i in range(3,51):
    c = a+b
    a,b = b,c
print(c)