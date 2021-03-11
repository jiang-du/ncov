# -*- coding: utf-8 -*-
"""
@Time        : 2021/3/11 12:29
@Author      : Jiang Du
@Email       : 39544089+jiang-du@users.noreply.github.com
@File        : Utils.py
@Description : 
@Version     : 0.4

@Time        : 2020/7/19 12:25
@Author      : NingWang
@Email       : yogehaoren@gmail.com
@File        : Utils.py
@Description : 
@Version     : 0.1-dev

@Project     : https://github.com/jiang-du/Auto-dailyup
@Project     : https://gitee.com/jiangdu/Auto-dailyup
"""

import requests

DEFAULT_HEADER = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/84.0.4147.89",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://xxcapp.xidian.edu.cn/site/ncov/xisudailyup",
    "Origin": "https://xxcapp.xidian.edu.cn"
}

UPLOAD_URL = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save"

# 0 - 北校区
NORTH_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",  # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5,
    # 38.5℃到39℃->6, 39℃到40℃->7, 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"VDa\":\"jsonp_324977_\","
                    "\"position\":{\"Q\":34.23254,\"R\":108.91516000000001,\"lng\":108.91802,\"lat\":34.23231},"
                    "\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\","
                    "\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"029\","
                    "\"adcode\":\"610113\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"白沙路\",\"streetNumber\":\"238号\","
                    "\"country\":\"中国\",\"province\":\"陕西省\",\"city\":\"西安市\",\"district\":\"雁塔区\","
                    "\"township\":\"电子城街道\"},\"formattedAddress\":\"陕西省西安市雁塔区电子城街道西安电子科技大学北校区\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[]}",
    "area": "陕西省 西安市 雁塔区",  # 地区
    "city": "西安市",  # 城市
    "province": "陕西省",  # 省份
    "address": "陕西省西安市雁塔区电子城街道西安电子科技大学北校区"  # 实际地址
}

# 0 - 南校区
SOUTH_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",
    # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5, 38.5℃到39℃->6, 39℃到40℃->7,
    # 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":34.121994628907,\"R\":108.83715983073,"
                    "\"lng\":108.83716,\"lat\":34.121995},\"location_type\":\"html5\",\"message\":\"Get ipLocation "
                    "failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":65,"
                    "\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"029\","
                    "\"adcode\":\"610116\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"雷甘路\",\"streetNumber\":\"264号\","
                    "\"country\":\"中国\",\"province\":\"陕西省\",\"city\":\"西安市\",\"district\":\"长安区\","
                    "\"township\":\"兴隆街道\"},\"formattedAddress\":\"陕西省西安市长安区兴隆街道西安电子科技大学长安校区办公辅楼\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "area": "陕西省 西安市 长安区",  # 地区
    "city": "西安市",  # 城市
    "province": "陕西省",  # 省份
    "address": "陕西省西安市长安区兴隆街道西安电子科技大学长安校区行政辅楼",  # 实际地址
}

# 2 - 广州研究院 (测试)
GZ_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",
    # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5, 38.5℃到39℃->6, 39℃到40℃->7,
    # 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":23.327658,\"R\":113.54548,"
                    "\"lng\":113.54548,\"lat\":23.327658},\"location_type\":\"html5\",\"message\":\"Get ipLocation "
                    "failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":65,"
                    "\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"020\","
                    "\"adcode\":\"510555\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"九龙大道\",\"streetNumber\":\"海丝知识中心\","
                    "\"country\":\"中国\",\"province\":\"广东省\",\"city\":\"广州市\",\"district\":\"黄埔区\","
                    "\"township\":\"九龙街道\"},\"formattedAddress\":\"广东省广州市黄埔区九龙大道海丝知识中心\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "area": "广东省 广州市 黄埔区",  # 地区
    "city": "广州市",  # 城市
    "province": "广东省",  # 省份
    "address": "广东省广州市黄埔区九龙大道海丝知识中心",  # 实际地址
}

# 3 - 杭州研究院 (预留)
HZ_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",
    # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5, 38.5℃到39℃->6, 39℃到40℃->7,
    # 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":30.261994621906,\"R\":120.19715981072,"
                    "\"lng\":120.19715,\"lat\":30.26199},\"location_type\":\"html5\",\"message\":\"Get ipLocation "
                    "failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":65,"
                    "\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"0571\","
                    "\"adcode\":\"310000\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"龙井路\",\"streetNumber\":\"1号\","
                    "\"country\":\"中国\",\"province\":\"浙江省\",\"city\":\"杭州市\",\"district\":\"西湖区\","
                    "\"township\":\"西湖街道\"},\"formattedAddress\":\"浙江省杭州市西湖区西湖街道龙井路1号杭州西湖风景名胜区\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "area": "浙江省 杭州市 西湖区",  # 地区
    "city": "杭州市",  # 城市
    "province": "浙江省",  # 省份
    "address": "浙江省杭州市西湖区西湖街道龙井路1号杭州西湖风景名胜区",  # 实际地址
}

# 4 - 备用(出差)
BAK_UPLOAD_MSG = {
    "sfzx": "1",  # 是否在校(0->否, 1->是)
    "tw": "1",
    # 体温 (36℃->0, 36℃到36.5℃->1, 36.5℃到36.9℃->2, 36.9℃到37℃.3->3, 37.3℃到38℃->4, 38℃到38.5℃->5, 38.5℃到39℃->6, 39℃到40℃->7,
    # 40℃以上->8)
    "sfcyglq": "0",  # 是否处于隔离期? (0->否, 1->是)
    "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状？ (0->否, 1->是)
    "qtqk": "",  # 其他情况 (文本)
    "askforleave": "0",  # 是否请假外出? (0->否, 1->是)
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":31.142927,\"R\":121.81332,"
                    "\"lng\":121.81332,\"lat\":31.142927},\"location_type\":\"html5\",\"message\":\"Get ipLocation "
                    "failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":65,"
                    "\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\","
                    "\"adcode\":\"200120\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\","
                    "\"building\":\"\",\"buildingType\":\"\",\"street\":\"迎宾大道\",\"streetNumber\":\"6000号\","
                    "\"country\":\"中国\",\"province\":\"上海市\",\"city\":\"上海市\",\"district\":\"浦东新区\","
                    "\"township\":\"祝桥镇\"},\"formattedAddress\":\"上海市浦东新区祝桥镇迎宾大道6000号浦东国际机场T2航站楼\",\"roads\":[],"
                    "\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "area": "上海市 浦东新区",  # 地区
    "city": "上海市",  # 城市
    "province": "上海市",  # 省份
    "address": "上海市浦东新区祝桥镇迎宾大道6000号浦东国际机场T2航站楼",  # 实际地址
}


def send_msg(state, config):
    """
    使用server酱发送消息
    :param title: 消息标题
    :param msg: 消息内容
    :return: 无
    """
    token = config["ServerToken"]
    if state == 666:
        title = "上报成功"
        if token:
            requests.post('https://sc.ftqq.com/{}.send?text={}&desp={}'.format(token, title, title))
        print(title)
    else:
        # msg = "错误信息: {}".format(state)
        if (state == "您已上报过"):
            title = "警告"
            msg = "您已上报过，本次无法重复上报，系统将在下个时间段自动恢复上报"
        else:
            title = "错误"
            msg = "错误信息: {}".format(state)
        if token:
            requests.post('https://sc.ftqq.com/{}.send?text={}&desp={}'.format(token, title, msg))
        print(title)
        print(msg)


def get_upload_msg(config):
    """
    获取要提交的内容
    :return: 提交的内容
    """
    location = config["Location"]
    if location == 1:
        upload_msg = NORTH_UPLOAD_MSG
    elif location == 2:
        upload_msg = SOUTH_UPLOAD_MSG
    elif location == 3:
        upload_msg = GZ_UPLOAD_MSG
    elif location == 4:
        upload_msg = HZ_UPLOAD_MSG
    else:
        upload_msg = BAK_UPLOAD_MSG
    return upload_msg


def upload_ncov_message(cookie, config):
    """
    提交内容的高阶API
    外部使用提交功能就是调用这个API，传入cookies即可提交
    :param cookie: cookies
    :return: 无
    """
    header = DEFAULT_HEADER
    upload_message = get_upload_msg(config)
    print("您当前的地点：" + upload_message["address"])
    r = requests.post(UPLOAD_URL, cookies=cookie, headers=header, data=upload_message)
    if r.json()['e'] == 0:
        send_msg(666, config)
        return 0        # "Upload successful"
    else:
        state = r.json()['m']
        send_msg(state, config)
        return (state != "您已上报过")
