#折线图
import matplotlib.pyplot as plt
data=[1,4,9,16,25,36]
axis=[1,2,3,4,5,6]
#在终端 import matplotlib.pyplot as plt
#       plt.style.available  可以查看绘图样式
plt.style.use('Solarize_Light2')
plt.title('平方',fontsize=15)   #标题，字体大小
plt.xlabel('x 轴',fontsize=10)
plt.ylabel('y 轴',fontsize=10)
plt.tick_params(axis='both',labelsize=15)   #坐标轴大小
plt.plot(axis,data,linewidth=5) #有subplot()
plt.show()

