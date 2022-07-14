b = [1, 2, 3]
a = b[:3]  # 切片赋值,若a=b则两者指向同一对象
# print(a is b)  # 判断a,b是否指向同一对象
# print(a == b)  # 判断a,b是否相等
a = tuple(a)  # 将序列转换为元组
s = 'python'
c = list(s)
# print(c)
# print(type(c))
d = list(range(0, 10))
# print(d)
for i in range(5):
    q = i
# print(i)
tup = 1, 2, 3  # 元组
# print(tup)
tup = 4, 5, 6
# print(tup)
l = {1, 2, 3, 4}
g = {3, 4, 5}
m = l.union(g)
n = l | g
# print(m)
l.add(0)
print(l)
