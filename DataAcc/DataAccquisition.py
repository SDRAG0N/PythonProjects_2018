# encoding=utf-8
from __future__ import division
import  matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']


class DataAcquisition:
    def __init__(self, old_path, new_path1, new_path2):
        self.old_path = old_path
        self.new_path1 = new_path1
        self.new_path2 = new_path2

    # 数据分离，写入文件
    def write_(self):
        with open(self.old_path, 'r+') as old, \
                open(self.new_path1, 'w+') as new1, \
                open(self.new_path2, 'w+') as new2:
            text_ = tuple(old)
            # print(text_)
            for i in range(0, text_.__len__()):
                a = str(text_[i])
                # print(11111)
                for j in range(0, len(a)):
                    # print(123)
                    # print(a[j])
                    if a[j] is not None and a[j] != ' ':
                        # print(a[j])
                        b = a[j]
                        # print(b)
                        # new1.seek(0)
                        new1.writelines(b)

                    elif a[j] == ' ':
                        new1.write('\n')
                        c = a[j+1:]
                        # new2.seek(0)
                        new2.writelines(c)
                        break


    def readAcceleration(self):
        with open(self.new_path1, 'r+') as acceleration:
            # 描绘线状图
            a = list(acceleration)
            # print('a', a)
            y1 = []
            for i in range(0, a.__len__()):
                d = float(a[i])
                y1.append(d)
            x = range(len(a))

            plt.plot(x, y1, mec='r', mfc='w', label=u'加速度')
            plt.legend()  # 让图例生效
            plt.xticks(x, range(0, a.__len__()), rotation=45)
            plt.margins(0)
            plt.subplots_adjust(bottom=0.15)
            plt.xlabel(u"time(ms)")  # X轴标签
            plt.ylabel("m/s^2 ")  # Y轴标签
            plt.title("坐 加速度波形图")  # 标题
            plt.show()

    def readAngularVelocity(self):
        with  open(self.new_path2, 'r+') as angularVelocity:
            # 描绘线状图
            b = list(angularVelocity)
            # print('b', b)
            y2 = []
            for i in range(0, b.__len__()):
                e = float(b[i])
                y2.append(e)
            x = range(len(b))

            plt.plot(x, y2, mec='r', mfc='w', label=u'角速度')
            # plt.plot(x, y2, ms=10, label=u'角速度')
            plt.legend()  # 让图例生效
            plt.xticks(x, range(0, b.__len__()), rotation=45)
            plt.margins(0)
            plt.subplots_adjust(bottom=0.15)
            plt.xlabel(u"time(s)")  # X轴标签
            plt.ylabel(" rad/s")  # Y轴标签
            plt.title("坐 角速度波形图")  # 标题
            plt.show()


if __name__ == "__main__":
    # go = DataAcquisition(r'D:\data(1).txt', r'D:\Data_acceleration.txt', r'D:\Data_angularVelocity.txt')
    go = DataAcquisition(r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第二次测试\坐.txt', r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第二次测试\分离数据\坐_加速度.txt', r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第二次测试\分离数据\坐_角速度.txt')
    go.write_()
    print('writie ok')
    go.readAcceleration()
    go.readAngularVelocity()
    print('is over')
