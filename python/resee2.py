# chapter 8函数
def fun(name, add=2022):
    if add:
        print('name:'+str(name))
    else:
        print('add:'+add)


fun('pisa', 2022)  # 位置实参
fun(add='pisa', name=2022)  # 关键字实参
fun(2022)  # 形参默认值，默认值必须放到最后


def fun2(name):
    for nm in name:
        nm = nm+'s'
    name.pop()  # 对列表的修改时永久性的
    return name


ba = ['a', 'b']
nam = fun2(ba[:])  # 传递切片，不会修改原列表
print(nam)
print(ba)
