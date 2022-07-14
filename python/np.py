import numpy as np
import matplotlib.pyplot as plt
my_arr = np.arange(10)          # np的range函数--数组版
my_list = list(range(10))
my_arr *= 2                     # 对整个数组的操作，数组向量化
my_list[3] *= 2
my_list = [x*2 for x in my_list]
data = np.random.randn(10)      # 随机正态分布
# plt.plot(data)
# plt.show()

data1 = (1, 2, 3, 4, 5, 2)
arr1 = np.array(data1)          # 转换成数组形式
arr2 = np.zeros(5)              # 生成0数组
arr3 = arr1.astype(np.float64)  # 改变数据类型
arr4 = np.array(['1.2', '2.1'], dtype=np.string_)  # 将字符串转换为数字
arr5 = arr4.astype(float)
arr6 = np.array([[1, 2, 3], [5, 7, 8]])
arr7 = np.array([[0, 3, 5], [2, 2, 3]])
# arr6[1:3] = 95                # 切片，数组切片是原数组的视图
# arr6[:] = 99                  # 默认为所有值
# arr8 = arr6[1:3].copy()       # 显式复制
arr9 = arr6[:1, 2:]             # 二维数组切片
#print(arr6[0, 1])
# print(arr6[0][1])
# print(arr9)
arr10 = data.reshape(2, 5)      # 设置数组格式
arr11 = arr6[[0], :2]           # 神奇索引是对数组的复制
arr11[0, 1] = 0                 # 修改复制的数组
arr12 = arr6[:, :2]             # 切片是数组的视图
arr12 *= 2                      # 修改原数组
arr13 = arr10.T                 # 数组转置
arr14 = np.dot(arr10, arr13)    # 计算矩阵乘积
# 一元通用函数：sqrt,exp,abs,fabs,square,log,sign,cos,arcsin
# 二元通用函数：add,substract,multiply,divide,fmax,maximum,mod
# 数组统计方法：sum,mean,std,var,min,max,cumsum,cumprod
# 数组集合操作：unique,intersect1d
arr15 = np.sqrt(arr6)
rem, who = np.modf(arr15)  # modf返回整数和小数部分
plt.imshow(arr15, cmap=plt.cm.gray)
arr16 = arr6.mean(axis=1)  # axis=0:计算列方向均值
arr17 = arr15.sort(axis=1)  # 排序
arr18 = np.random.randn(10)
np.save('array', arr18)    # 存储数组元素
arr19 = np.load('array.npy')
arr20 = list(range(10))
arr20.append(0.3)  # 祥列表添加元素
