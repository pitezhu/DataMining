# chapter 2
name = '  zhuhaifei123  '
address = 746000
# print(name.title())  # 首字母改为大写
# print(name.upper())  # 全部改为大写
# print(name.lower())  # 全部改为小写
name = name.upper()  # 永久改变变量
# print(name.strip())  # l/r分别为删除左边和右边的空格符,只是暂时删除
name = str(name)  # 将非字符串改为字符串
info = name+' '+str(address)  # +号进行字符串连接
# print(info)

# chapter 3

arr = ['as', 23, 'aa']  # 可用下标访问，从0开始
# print(arr[-1])  # 负数索引
arr.append('xing')  # 添加元素至列表尾
arr.insert(1, 'b')  # 在指定位置插入元素

del arr[2]  # 删除后无法访问，删除指定位置元素
ab = arr.pop()  # 删除的值可以访问，弹出尾元素
arr.remove('as')  # 删除的值可以访问，删除指定的值

# print(sorted(arr))  # sorted临时排序
# arr.sort(reverse=True)  # 永久性排序,反向排序
for ms in arr:
    arr.pop()

arr.remove('b')
arr.append('李亚兰')
arr.append('崔盼盼')
arr.append('小兰')
arr.append('小崔')
arr.reverse()  # 反向排列
# print(len(arr))  # 列表长度
num = list(range(1, 10, 3))  # list生成列表,指定步长为3
# print(min(num))#统计函数 min,max,sum
squ = [val for val in range(1, 5)]  # 列表解析，将for循环和创建列表合并
# print(squ)
# print(squ[0:3])  # 切片
ass = squ  # 两个列表指向同一数据
# print(ass)
ass[0] = 10
# print(squ)
dd = (1, 2, 3)  # 元组的元素不可改变
dd = (2, 3)  # 可以给元组变量赋值
# print(dd)
# print(len(dd))

# chapter 5
cs = 12
cq = 5
if (cs != 2) and (cq == 4):
    cs = 1
elif cq == 5:
    cs = 2
else:
    cs = 3
print(cs)
