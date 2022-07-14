import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

rw=RandomWalk(1000)
rw.Fill_Walk()
plt.scatter(rw.xvalues,rw.yvalues,cmap=plt.cm.Blues,s=1)
plt.show()
