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

    def read_(self):
        with open(self.new_path1, 'r+') as acceleration, \
                open(self.new_path2, 'r+') as angularVelocity:
            print('acceleration', acceleration)
            print('angularVelocity', angularVelocity)
            a = list(acceleration)
            print('a', a)
            b = list(angularVelocity)
            print('b', b)
            c = []
            for i in range(0, a.__len__()):
                d = float(a[i])
                c.append(d)
            print('c',c)



if __name__ == "__main__":
    go = DataAcquisition(r'D:\data(1).txt', r'D:\Data_acceleration.txt', r'D:\Data_angularVelocity.txt')
    # go.write_()
    # print('writie ok')
    go.read_()
    print('is over')
