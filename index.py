from utils import Utils
from utils import USER
import time
from functions import updateTimeLib, checkTime, checkInternetConnection

def index(event, context):
    """
    腾讯云函数的入口函数
    :param event:
    :param context:
    :return:
    """
    _cookie = USER.login()
    return Utils.upload_ncov_message(_cookie)

if __name__ == '__main__':
    if checkInternetConnection():
        print("联网成功！")
    else:
        raise Exception("没有网，填个锤子呀，嘤～")
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
        elif currentState == 5:
            # 整点报时
            time.sleep(60)
        else:
            time.sleep(30)
