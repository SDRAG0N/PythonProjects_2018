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
                elif ii % 12 == 1:
                    self.ax.append(numpy.float64(s[ii]))
                elif ii % 12 == 2:
                    self.ay.append(numpy.float64(s[ii]))
                elif ii % 12 == 3:
                    self.az.append(numpy.float64(s[ii]))
        # 设定一个阈值，一旦加速度小于此阈值说明人体处于失重状态
        self.values = values
        # print('数据分离成功\n'
        #       'self.args_s:{}\n'
        #       'self.ax:{}\n'
        #       'self.ay:{}\n'
        #       'self.az:{}\n'.format(self.args_s, self.ax, self.ay, self.az))

    # 一级检测 判断加速度值是否小于设定的值 是则触发FreeFall事件，
    # 判断是否连续6次小于阈值
    def free_fall(self):
        # print('FREEFALL事件: self.args传入成功:{}'.format(self.args_s))
        for i in range(0, self.args_s.__len__()):
            if self.args_s[i] < self.values:
                # 获取引发事件值位置
                self.i = i
                # 触发事件次数
                free_fall = 1
                for j in range(1, 6):
                    if self.args_s[i+j] > self.values:
                        # 进入第二层检测
                        self.activity()
                        return "已进入第二层检测"
                    else:
                        free_fall += 1
                if free_fall == 6:
                    # 报警
                    print("!!!!!!!!!!!!!!!!!!")
                    break

    # 二级检测
    # activity中断检测阶段主要判断是否有连续5次以上并且 SVM值大于1.5g的采样点，
    # 再进行MADS判断，如果通过检测，然后采集50个采样点，为后期的姿态角求解提供数据；
    # 当Activity中断触发后进入Inactivity中断检测
    def activity(self):
        print('进入第二层检测')
        kk, s = 0, 0
        for k in range(self.i, self.i+6):
            svm = numpy.sqrt(self.ax[k] + self.ay[k] + self.az[k])
            if svm > 1.59:
                kk += 1
                s += svm
        # 判断触发activity中断
        if kk >= 5:
            # 进行 MADS 通过判断则触发inactivity中断
            if s/5 > 0.36:
                # 采集50个采样点
                self.ss, self.aax, self.aay, self.aaz = [], [], []
                for a in range(0, 50):
                    self.ss.append(self.args_s[a])
                    self.aax.append(self.ax[a])
                    self.aay.append(self.ay[a])
                    self.aay.append(self.az[a])
                self.inactivity()



    # 三级检测
    # 当本次采样点的加速度值与本次采样点之前的上一个采样点之差超过THRESH INACT寄存器存储值时，那么本次采集的数据则覆盖上一次采集到的数据。
    # 反之，则发生Inactivity中断，经过多次实验，此门限值可以设定为O.1875g。
    # 此阶段判断人体是否处于平静阶段，如果Inactivity中断触发，对之前的50个采样数据进行姿态角计算，最后根据检测状态确认人体运动状态信息。
    def inactivity(self):
        print('进入第三层检测')
        for i in range(1, self.ss.__len__()):
            if abs(self.ss[i] - self.ss[i-1]) > 0.1875:
                # 本次采集的数据则覆盖上一次采集到的数据
                print("覆盖数据")
            else:
                # 对之前的50个采样数据进行姿态角计算，
                for j in range(0, self.ax.__len__()):
                    pitch = math.atan(self.aax[j]/abs(self.aay[j]**2+self.aaz[j]**2))
                    roll = math.atan(self.aay[j]/abs(self.aax[j]**2+self.aaz[j]**2))
                    if pitch > 2/3:
                        print("摔倒!!!!!!!!!!")
                        break
                    elif roll > 2/3:
                        print("跌倒!11111111")
                        break


if __name__ == "__main__":
    # value 是判断人体平静的阈值
    go = Threshold(path=r'C:\Users\S-DRAGON\Desktop\跌倒检测实验\第四次测试\侧摔.txt', values=100)
    go.free_fall()
