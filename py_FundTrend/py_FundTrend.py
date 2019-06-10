import matplotlib.gridspec as gridspec
import matplotlib.image as imgplt
import matplotlib.pyplot as plt
import time
plt.ion()
gs = gridspec.GridSpec(2, 1)
plt.figure(figsize=(6,8))
# plt.subplots_adjust(left=0.3, wspace =0, hspace =0.5)#调整子图间距
while True:
    plt.clf()
    plt.subplot(gs[0, :])
    fund_000656 = imgplt.imread('http://j4.dfcfw.com/charts/pic6/000656.png')
    plt.imshow(fund_000656)
    plt.subplot(gs[1, 0])
    fund_519697 = imgplt.imread('http://j4.dfcfw.com/charts/pic6/519697.png')
    plt.imshow(fund_519697)
    plt.pause(1)
    plt.ioff()
