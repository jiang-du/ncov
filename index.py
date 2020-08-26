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
    print("更新晨午晚检上报时间成功！下一天的上报时间为:")
    print("晨检 - %d点%d分，午检 - %d点%d分，晚检 - %d点%d分。" % tuple(new_time))
    return new_time

def checkTime(time_lib):
    """
    判断当前时刻是否需要上报，以及对应模式
    输入值： 上报时间
    返回值： 上报模式(1, 2, 3分别对应晨午晚检)
    """
    Hour, Minus, Secs = getNowHourMinSec()
    if Hour == time_lib[0] and Minus == time_lib[1]:
        # 晨检
        currentState = 1
    elif Hour == time_lib[2] and Minus == time_lib[3]:
        # 午检
        currentState = 2
    elif Hour == time_lib[4] and Minus == time_lib[5]:
        # 晚检
        currentState = 3
    elif Hour == 23 and Minus == 55:
        # 夜间模式
        currentState = 4
    else:
        currentState = 0
    if currentState:
        print("当前系统时间  %d:%d:%d" % (Hour, Minus, Secs))
    return currentState

if __name__ == '__main__':
    # 程序运行时立即上报一次
    cookie = USER.login()
    # 第一次上报不判断函数返回值，因为假设用户还在电脑旁，可以实时观察程序输出结果
    Utils.upload_ncov_message(cookie)
    # 定义程序上报的时间，初始值为 7:15, 12:05, 18:10
    time_lib = [7, 15, 12, 5, 18, 10]
    # 立即更新今日上报时间
    time_lib = updateTimeLib(time_lib)
    # 定义上报结束之后的冷却时间(s)
    cd_time = 180
    # 是否开启夜间睡眠模式
    night_mood = True
    # 开始上报
    while True:
        # 获取当前是否需要上报的模式，1, 2, 3分别对应晨午晚检
        currentState = checkTime(time_lib)
        if currentState in (1, 2, 3):
            cookie = USER.login()
            # 函数返回值为1表示上报失败，将自动重试3次
            if Utils.upload_ncov_message(cookie):
                time.sleep(90)
                if Utils.upload_ncov_message(cookie):
                    time.sleep(180)
                    if Utils.upload_ncov_message(cookie):
                        print("连续尝试了3次都上报失败啦，嘤～")
            # 上报结束之后的冷却时间
            time.sleep(cd_time)
        elif currentState == 4:
            # 每天23点55分，更新下一天上报的随机时刻
            time_lib = updateTimeLib(time_lib)
            if night_mood:
                # 进入夜间睡眠模式
                print("程序将进入睡眠模式，祝您晚安！")
                # 夜间暂停6小时
                time.sleep(6*60*60)
                print("早上好！")
        else:
            time.sleep(30)
