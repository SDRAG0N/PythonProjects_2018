import numpy


class Test:
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
            print("用s获取数据成功：{}".format(s))
            self.args_s = []
            for ii in range(0, s.__len__()):
                if ii % 12 == 0:
                    self.args_s.append(numpy.float64(s[ii]))
                elif ii % 12 == 1:
                    self.ax.append(numpy.float64(s[ii]))
                elif ii % 12 == 2:
                    self.ay.append(numpy.float64(s[ii]))
                elif ii % 12 == 3:
                    self.az.append(numpy.float64(s[ii]))
        # 设定一个阈值，一旦加速度小于此阈值说明人体处于失重状态
        self.values = values
        print('数据分离成功\n'
              'self.args_s:{}\n'
              'self.ax:{}\n'
              'self.ay:{}\n'
              'self.az:{}\n'.format(self.args_s, self.ax, self.ay, self.az))


if __name__ == "__main__":
    go = Test(path=r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第四次测试\侧摔.txt', values='3000')



