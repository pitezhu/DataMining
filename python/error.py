def div_zero(a, b):
    try:            # 异常捕获
        c = a/b
        print(c)
    except:
        print('can not div zero')


div_zero(1, 2)

tit = 'can not div zero'
sp = tit.split()  # 文本分析，进行切词，创建单词列表
print(sp)
