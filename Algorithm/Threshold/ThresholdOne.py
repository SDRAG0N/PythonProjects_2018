import numpy
import math


class Threshold:
    def __init__(self, path, values):
        # 数据分离获取
        self.ax, self.ay, self.az = [], [], []
        with open(path, 'r+') as self.args_ss:
            self.args_ss = tuple(self.args_ss)
            print("self.args_ss:", self.args_ss)
            # self.args_ss = str(self.args_ss[0])
            # ss = self.args_ss.split(' ')
            s, s1 = [], []
            for jjj in range(0, self.args_ss.__len__()):
                s1 = self.args_ss[jjj]
                s1 = s1.split(' ')
                for iii in range(0, s1.__len__()):
                    if s1[iii] == '\n':
                        continue
                    else:
                        s.append(s1[iii])
            # print("用s获取数据成功：{}".format(s))
            self.args_s = []
            for ii in range(0, s.__len__()):
                if ii % 12 == 0:
                    self.args_s.append(numpy.float64(s[ii]))
                else:
                    continue
        # 设定一个阈值，一旦加速大于此阈值报警
        self.values = values
        # print('数据分离成功\n'
        #       'self.args_s:{}\n'
        #       'self.ax:{}\n'
        #       'self.ay:{}\n'
        #       'self.az:{}\n'.format(self.args_s, self.ax, self.ay, self.az))

    def deal(self):
        # print(1111)
        print('deal self.args_s:', self.args_s)
        for i in range(0, self.args_s.__len__()):
            if self.args_s[i] > self.values:
                # 报警
                return "报警"
            else:
                return  "正常"

if __name__ == "__main__":
    go = Threshold(path=r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第四次测试\报警测试.txt', values=300)
    print(go.deal())
