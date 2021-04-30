from random import randint
while True:
    number_1 = randint(0, 3)
    number_2 = randint(0, 3)
    number_3 = randint(0, 3)
    code_1=input("请输入第一位密码(范围：0--3)\n")
    code_1=int(code_1)
    if code_1!=number_1:
        continue
    print("第一位密码正确")
    code_2 = input("请输入第二位密码(范围：0--3)\n")
    code_2 = int(code_2)
    if code_2 != number_2:
        continue
    print("第二位密码正确")
    code_3 = input("请输入第三位密码(范围：0--3)\n")
    code_3 = int(code_3)
    if code_3 == number_3:
        break
print(f"密码正确，解锁成功，密码是：{number_1}{number_2}{number_3}")