import datetime
import config
import json
import os

def sign_in(user_id):
    user_id = str(user_id)
    if os.path.exists(config.DATA_FILE):
        with open(config.DATA_FILE, 'r') as fp:
            data = json.load(fp)
    else:
        data = {}
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    if user_id in data and data[user_id]['last_sign_in'] == today:
        return "你今天已经签到过了！"
    if user_id in data:
        data[user_id]['points'] += config.POINTS_PER_DAY
        data[user_id]['last_sign_in'] = today
    else:
        data[user_id] = {'points':config.POINTS_PER_DAY, 'last_sign_in': today}
    with open(config.DATA_FILE, 'w') as fp:
        json.dump(data, fp)
        return "签到成功！"


def deduct_points(user_id):
    user_id = str(user_id)
    if os.path.exists(config.DATA_FILE):
        with open(config.DATA_FILE, 'r') as fp:
            data = json.load(fp)
    else:
        data = {}
    
    if user_id in data:
        if data[user_id]['points'] <= 0:
            return False
        data[user_id]['points'] -= config.POINTS_PER_DAY
        data[user_id] = {'points':data[user_id]['points'], 'last_sign_in': data[user_id]['last_sign_in']}
        with open(config.DATA_FILE, 'w') as fp:
            json.dump(data, fp)
        return True
    else:
        return False


def get_deduct(user_id):
    user_id = str(user_id)
    if os.path.exists(config.DATA_FILE):
        with open(config.DATA_FILE, 'r') as fp:
            data = json.load(fp)
    else:
        data = {}
    
    if user_id in data:
        return "您的有效积分为：" + str(data[user_id]['points'])
    else:
        return "用户不存在！\n请先使用 /sign 签到"

