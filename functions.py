import datetime
import random
import requests

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
    elif not Minus:
        # 整点时刻
        currentState = 5
    else:
        currentState = 0
    if currentState:
        print("当前系统时间  %d:%d:%d" % (Hour, Minus, Secs))
    return currentState

def checkInternetConnection():
    try:
        requests.get("https://xxcapp.xidian.edu.cn/site/ncov/xisudailyup", timeout=5)
    except:
        return False
    return True
