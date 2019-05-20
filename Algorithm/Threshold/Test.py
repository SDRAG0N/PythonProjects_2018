class Threshold:
    def __init__(self,  args_s):
        print(11111)
        # 数据分离获取
        self.ax, self.ay, self.az = [], [], []
        with open(args_s, 'r+') as self.args_ss:
            self.args_ss = tuple(self.args_ss)
            self.args_ss = str(self.args_ss[0])
            s = self.args_ss.split(' ')
            self.args_s = []
            for ii in range(0, s.__len__()):
                while ii % 12 == 0:
                    self.args_s.append(self.args_ss[ii])
                while ii % 12 == 1:
                    self.ax.append(self.args_ss[ii])
                while ii % 12 == 2:
                    self.ay.append(self.args_ss[ii])
                while ii % 12 == 3:
                    self.az.append(self.args_ss[ii])
        # print('args_ss'+self.args_ss)
        # print('args_ss'+self.args_s )
        # print('args_ss'+self.ax)
        # print('args_ss'+self.ay )
        # print('args_ss'+self.az )

    def avg(self):
        print("avg:", )

if __name__ == "__main__":
    go = Threshold(r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第三次测试\侧摔.txt')
