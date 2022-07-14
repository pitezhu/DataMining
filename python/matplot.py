from cProfile import label
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
data = np.arange(10)
dat = np.random.randn(50)
fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
#ax4 = fig.add_subplot(2, 2, 4)
# plt.plot(data, 'k--')
# plt.plot(dat)
# plt.show()
# fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(np.random.randn(500), bins=50, color='r', alpha=0.5)
# plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
