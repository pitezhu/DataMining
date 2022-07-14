import numpy as np
import matplotlib.pyplot as plt
lis = list(np.arange(10))
ran = np.random.randn(100)
plt.plot(ran)
plt.title('正态分布')
plt.xlabel('x')
plt.ylabel('data')
# plt.show()
dat = np.arange(20).reshape(4, 5)
dat[1, :2] = 1
# print(dat.T)
res = np.dot(dat.T, dat)  # 矩阵乘积
rest = np.array([[-1, 2, 3], [4, 5, 6]])
print(rest)
