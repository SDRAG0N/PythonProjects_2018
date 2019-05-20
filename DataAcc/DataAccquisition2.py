# encoding=utf-8
from __future__ import division
import  matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']


class DataAcquisition:
    def __init__(self, new_path1, new_path2):
        # self.old_path = old_path
        self.new_path1 = new_path1
        self.new_path2 = new_path2

    def readAcceleration(self):
        with open(self.new_path1, 'r+') as acceleration:
            # 描绘线状图
            a = list(acceleration)
            # print('a', a)
            y1 = []
            for i in range(0, a.__len__()):
                d = float(a[i])
                y1.append(d)
            for d in range(0, len(y1)):
                if y1[d] > 5:
                    y1 = y1[d:-800:20]
                    break
            # xzh = int(len(y1)/10)
            print(type(len(y1)))
            x = range(len(y1))

            plt.plot(x, y1, mec='r', mfc='w', label=u'加速度')
            plt.legend()  # 让图例生效
            plt.xticks(x, range(0, a.__len__()), rotation=45)
            plt.margins(0)
            plt.subplots_adjust(bottom=0.15)
            plt.xlabel(u"time(ms)")  # X轴标签
            plt.ylabel("m/s^2 ")  # Y轴标签
            plt.title("侧摔 加速度波形图")  # 标题
            plt.show()

    def readAngularVelocity(self):
        with open(self.new_path2, 'r+') as angularVelocity:
            # 描绘线状图
            b = list(angularVelocity)
            # print('b', b)
            y2 = []
            for i in range(0, b.__len__()):
                iii = float(b[i])
                y2.append(iii)
            for d in range(0, len(y2)):
                if y2[d] > 5:
                    y2 = y2[d:-800:20]
                    break
            # x轴
            x = range(len(y2))

            plt.plot(x, y2, mec='r', mfc='w', label=u'角速度')
            # plt.plot(x, y2, ms=10, label=u'角速度')
            plt.legend()  # 让图例生效
            plt.xticks(x, range(0, b.__len__()), rotation=45)
            plt.margins(0)
            plt.subplots_adjust(bottom=0.15)
            plt.xlabel(u"time(s)")  # X轴标签
            plt.ylabel(" rad/s")  # Y轴标签
            plt.title("侧摔 角速度波形图")  # 标题
            plt.show()


if __name__ == "__main__":
    # go = DataAcquisition(r'D:\data(1).txt', r'D:\Data_acceleration.txt', r'D:\Data_angularVelocity.txt')
    go = DataAcquisition(new_path1=r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第二次测试\分离数据\侧摔_加速度.txt', new_path2=r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第二次测试\分离数据\侧摔_角速度.txt')
    # go.write_()
    # print('writie ok')
    go.readAcceleration()
    go.readAngularVelocity()
    print('is over')
