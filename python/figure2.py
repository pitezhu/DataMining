#散点图
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
data=list(range(1,1001))
axis=[x**2 for x in data]
#plt.axis=[0,1100,0,1100000]
#plt.style.use('Solarize_Light2')
plt.title('散点图',fontsize=15)   #标题，字体大小
plt.xlabel('x 轴',fontsize=10)
plt.ylabel('y 轴',fontsize=10)
plt.tick_params(axis='both',which='minor',labelsize=15)   #坐标轴大小
plt.scatter(data,axis,cmap=plt.cm.Blues,edgecolor='none',s=40) #有subplot()
plt.show()
#plt.savefig('zhixian.png',bbox_inches='tight')  #保存图片
