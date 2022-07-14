# chapter 10 文件操作
# f_p='D:/test.txt'  f_p='D://test.txt'  f_p=r'D:\test.txt'
import json
f_p = 'D://test.txt'
with open(f_p, 'a') as files:
    files.write('i am in china'+'\n'+'i love china')

num = [1, 2, 3, 4, 5]
with open('txt', 'w') as file_json:
    json.dump(num, file_json)

with open('txt', 'r') as file_json:
    mes = json.load(file_json)
    print(mes)
