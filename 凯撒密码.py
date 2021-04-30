mima = input('请输入明文：\n')
for i in mima:
    if ord("a") <= ord(i) <= ord("z"):
        print(chr(ord("a")+(ord(i)-ord("a")+3)%26), end='')
    else:
        print(i, end='')
        #   ord()函数主要用来返回对应字符的ascii码，chr()主要用来表示ascii码对应的字符