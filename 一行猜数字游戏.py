import random
n=random.randint(1,99)
[(lambda a:print('Y' if a==n else 'H' if a>n else 'L'))
 (int(input())) for i in range(6)]
#大了就输入H，小了就输入L ，超过6次退出，Y代表正确
#一行代码的迷宫游戏等 文章链接：https://mp.weixin.qq.com/s/S4rm4a3lMgG3Zr6Kz-8qAQ
