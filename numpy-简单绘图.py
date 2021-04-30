import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)     # x轴数据
y =  x ** 3         # 函数关系
plt.title("y=x**3")     # 图像标题
plt.xlabel("x")     # x轴标签
plt.ylabel("y")     # y轴标签
plt.plot(x,y)     # 生成图像
plt.show()    # 显示图像