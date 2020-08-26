from utils import Utils
from utils import USER
import datetime
import time
import random


def index(event, context):
    """
    腾讯云函数的入口函数
    :param event:
    :param context:
    :return:
    """
    _cookie = USER.login()
    return Utils.upload_ncov_message(_cookie)


def getNowHourMinSec():
    """
    获取现在的时分秒
    输入值： 无
    返回值： 当前是时、分、秒，返回的形式是HOUR、MINIUTE、SECONDS
    """
    d = datetime.datetime.now()
    hour = int(str(d)[11:13])
    miniute = int(str(d)[14:16])
    seconds = int(str(d)[17:19])
    return hour, miniute, seconds

def updateTimeLib(time_lib):
    """
    随机更新下一天上报的时间
    输入值： 原来的上报时间
    返回值： 更新的上报时间
    """
    assert len(time_lib) == 6
    new_time = time_lib
    new_time[1] = random.randint(2,59)
    new_time[3] = random.randint(2,59)
    new_time[5] = random.randint(2,59)
    print("Update submission time successfully:")
    print(new_time)
    return new_time

if __name__ == '__main__':
    # 程序运行时立即上报一次
    cookie = USER.login()
    # 第一次上报不判断函数返回值，因为假设用户还在电脑旁，可以实时观察程序输出结果
    Utils.upload_ncov_message(cookie)
    # 定义程序上报的时间，初始值为 7:15, 12:05, 18:10
    time_lib = [7, 15, 12, 5, 18, 10]
    # 更新上报时间
    time_lib = updateTimeLib(time_lib)
    # 定义上报结束之后的冷却时间(s)
    cd_time = 180
    # 开始上报
    while True:
        Hour, Minus, Secs = getNowHourMinSec()
        # 程序上报的时间点8:02 13:09 18:05
        if Hour == time_lib[0] and Minus == time_lib[1] or Hour == time_lib[2] and Minus == time_lib[3] or Hour == Hour == time_lib[4] and Minus == time_lib[5]:
            print("Current Time: %d:%d:%d" % (Hour, Minus, Secs))
            cookie = USER.login()
            # 函数返回值为1表示上报失败，将自动重试3次
            if Utils.upload_ncov_message(cookie):
                time.sleep(90)
                if Utils.upload_ncov_message(cookie):
                    time.sleep(180)
                    if Utils.upload_ncov_message(cookie):
                        print("I have no idea to try again.")
            # 上报结束之后的冷却时间
            time.sleep(cd_time)
        else:
            time.sleep(30)
