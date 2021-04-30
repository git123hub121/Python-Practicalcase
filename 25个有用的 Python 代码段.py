#1.在两个变量之间交换值
a = 5
b = 10
a,b = b,a
print(a) # 10
print(b) # 5
#print('\n')

#2.检查给定的数字是否为偶数
def is_even(num):
    return num % 2 == 0
is_even(10) # True

#3.将多行字符串拆分为行列表
def split_lines(s):
    return s.split('\n')
split_lines('50\n python\n snippets') # ['50', ' python', ' snippets']

#4.查找对象使用的内存
#5.反转字符串
#6.打印字符串 n 次

#7.检查字符串是否为回文
#8.
#9.
#10.
#11.
#12.求一组数字的平均值
def average(*args):
  return sum(args, 0.0) / len(args)

average(5, 8, 2) # 5.0

#13.
#14.
#15.
#16.
#17.
#18.
#19.
#20.
#21.
#22.
#23.
#24.
#25.