# chapter 6
dic = {'a': 1, 'b': 2, 'c': 2}
for key, val in dic.items():  # items()方法返回键值对
    print(key+':' + str(val))
for key in dic.keys():
    print(key)
for val in set(dic.values()):  # set除去重复值
    print(val)
for nam in dic:
    print(nam)
if 'a' in dic.keys():
    print('ok')
# chapter 7
# info = input('give me some thing!') #输入提示信息
x = 5 % 2  # 求模返回余数
