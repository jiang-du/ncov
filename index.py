from utils import Utils
from utils import USER
import datetime
import time


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


if __name__ == '__main__':
    while True:
        Hour, Minus, Secs = getNowHourMinSec()
        # 程序上报的时间点8:02 13:09 18:05
        if Hour == 8 and Minus == 2 or Hour == 13 and Minus == 9 or Hour == 18 and Minus == 5:
            # if True:
            cookie = USER.login()
            Utils.upload_ncov_message(cookie)
        else:
            time.sleep(30)
