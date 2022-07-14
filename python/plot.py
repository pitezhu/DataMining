import matplotlib.pyplot as plt
import numpy as np
import jieba
import requests
import urllib


# subplot函数
def plot1():
    # plt.plot([1,2,3])
    # 现在创建一个子图，它表示一个有2行1列的网格的顶部图。
    # 因为这个子图将与第一个重叠，所以之前创建的图将被删除
    plt.subplot(2, 1, 1)
    plt.plot(range(12))
    plt.show()
    # 创建带有黄色背景的第二个子图
    plt.subplot(2, 1, 2, facecolor='y')
    plt.plot(range(12))
    plt.show()


# subplots函数
def plot2():
    fig, a = plt.subplots(2, 2)
    x = np.arange(1, 5)
    # 绘制平方函数
    a[0][0].plot(x, x*x)
    a[0][0].set_title('square')
    # 绘制平方根图像
    a[0][1].plot(x, np.sqrt(x))
    a[0][1].set_title('square root')
    # 绘制指数函数
    a[1][0].plot(x, np.exp(x))
    a[1][0].set_title('exp')
    # 绘制对数函数
    a[1][1].plot(x, np.log10(x))
    a[1][1].set_title('log')
    plt.show()


# 网络爬虫
def url1():
    import urllib
    url = 'http://www.baidu.com'
    page_info = urllib.request.urlopen(url).read()
    page_info = page_info.decode('utf-8')
    print(page_info)


def url2():
    url = 'http://www.baidu.com'
    r = requests.get(url)
    print(r.url)
    r.encoding = 'utf-8'  # 改变编码格式
    print(r.text)


url2()
