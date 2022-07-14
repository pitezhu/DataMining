from tkinter.font import names


def greet1(names):
    for name in names:
        mess='hello,'+name
        #print(mess)

nam=['na','ga','sfa']
greet1(nam)  #实参传递列表


def greet3(first,**top):   #传递键值对
    names={}
    names['first_name']=first
    for key,val in top.items():
        names[key]=val
    return names
bs=greet3('sd',ad='sdf')
print(bs)

def greet2(*top):   #传递多个实参
    sa=top
    #print(sa)

greet2('sd','sd')
