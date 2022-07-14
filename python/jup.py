import re
s = 'abc\\123'  # 转义字符\生效
s1 = r'abc\\123'  # 转义字符\保留
# print(s)
# print(s1)


# print(re.match('www', 'www.baidu.com').span())
# print(re.match('www', 'www.baidu.com'))

# print(re.search('www', 'www.baidu.com'))
# print(re.search('baidu', 'www.baidu.com'))

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)
