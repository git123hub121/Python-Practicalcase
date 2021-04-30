#控制流
"""for  while if-elif-else break continue"""
#if-elif-else
number = 23
guess = int(input('Enter a or an integer:    '))    #input返回的是字符串，所以需要int转换
if number == guess:
    #自动帮你缩进
    print('yes!')
elif guess < number:
    print("g < n")
else:
    print('g > n')
print('程序结束')