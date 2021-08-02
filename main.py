from utils import Utils
from utils import USER
import time
from functions import updateTimeLib, checkTime, checkInternetConnection, getInfo, replace_char

if __name__ == '__main__':
    if checkInternetConnection():
        print("联网成功！")
    else:
        raise RuntimeError("没有网，填个锤子呀，嘤～")
    # 获取配置信息
    config = getInfo()
    # 用户登录
    cookie = USER.login(config)
    if config["passWord"]:
        # 登录后立即销毁内存空间中的密码，采用逐字节擦写，更大限度的隐私保护
        if replace_char(config["passWord"], len(config["passWord"])):
            raise RuntimeError("内存地址访问失败，嘤～")
        print("为了保护用户隐私，登录成功后已自动销毁密码，可以放心使用。")
    # 选择模式
    line = input("请选择：1-疫情通，2-晨午晚检，按回车键结束：")
    # 定义上报结束之后的冷却时间(s)
    cd_time = 180
    # 是否开启夜间睡眠模式
    night_mood = True
    # 定义程序上报的时间，初始值为 7:15, 12:05, 18:10
    time_lib = [7, 15, 12, 5, 18, 10]
    if line[0]=='1':
        config["mode"] = "疫情通"
        print("已选择疫情通")
        # 程序运行时立即上报一次
        # 第一次上报不判断函数返回值，因为假设用户还在电脑旁，可以实时观察程序输出结果
        Utils.upload_ncov_message(cookie, config) 
        # 立即更新今日上报时间
        time_lib = updateTimeLib(time_lib, single = True)
        # 开始上报
        while True:
            # 每天早上自动填疫情通
            currentState = checkTime(time_lib)
            if currentState == 1:
                # 如果还没登录的话，先登录
                if not cookie:
                    cookie = USER.login()
                # 函数返回值为1表示上报失败，将自动重试3次
                if Utils.upload_ncov_message(cookie, config):
                    time.sleep(90)
                    if Utils.upload_ncov_message(cookie, config):
                        time.sleep(180)
                        if Utils.upload_ncov_message(cookie, config):
                            print("连续尝试了3次都上报失败啦，嘤嘤嘤！")
                # 上报结束之后的冷却时间
                time.sleep(cd_time)
            elif currentState == 4:
                # 每天23点55分，更新下一天填疫情通的随机时刻
                time_lib = updateTimeLib(time_lib, single = True)
                if night_mood:
                    # 进入夜间睡眠模式
                    print("程序将进入睡眠模式，祝您晚安！")
                    # 夜间暂停6小时
                    time.sleep(6*60*60)
                    print("早上好！")
            else:
                time.sleep(30)
    else:
        config["mode"] = "晨午晚检"
        print("已选择晨午晚检")
        # 程序运行时立即上报一次
        Utils.upload_ncov_message(cookie, config)
        # 立即更新今日上报时间
        time_lib = updateTimeLib(time_lib)
        # 开始上报
        while True:
            # 获取当前是否需要上报的模式，1, 2, 3分别对应晨午晚检
            currentState = checkTime(time_lib)
            if currentState in (1, 2, 3):
                # 如果还没登录的话，先登录
                if not cookie:
                    cookie = USER.login()
                # 函数返回值为1表示上报失败，将自动重试3次
                if Utils.upload_ncov_message(cookie, config):
                    time.sleep(90)
                    if Utils.upload_ncov_message(cookie, config):
                        time.sleep(180)
                        if Utils.upload_ncov_message(cookie, config):
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
