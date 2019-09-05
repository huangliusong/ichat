# -*- coding: utf-8 -*
import requests
import itchat
import re
import random
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = TimedRotatingFileHandler("a.log", when='D', encoding="utf-8")
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
itchat.auto_login(enableCmdQR=2)

print u'系统默认编码为', sys.getdefaultencoding()

default_encoding = 'utf-8'  # 重新设置编码方式为uft-8
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

print u'系统修改编码为', sys.getdefaultencoding()

key = '6dde22b7692b48fe9f89ce52b2673e0f'  # 这里是你自己机器人的apikey
arr = ['dd6710813403477689911f4b322cf685', 'c3c69290cf9d4357923d2f6ece25ecdd',
       '6dde22b7692b48fe9f89ce52b2673e0f', '6fce7ad8fb354b6a91c30eb05681590a', 'dd6710813403477689911f4b322cf685']

nickName = '小兔几'  # 这里是昵称或群昵称，用于检测群聊是否被艾特


def get_response(msg):
    a = random.randint(1, 4)
    key = arr[a]
    print(key)
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {'key': key, 'info': msg, 'userid': 'wechat-robot'}
    r = requests.post(apiUrl, data=data).json()
    # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
    print('==================================================')
    print('收到消息：', msg)
    logger.info('收到消息：'+msg)
    print('回复消息：', r.get('text'))
    logger.info('收到消息：'+r.get('text'))
    return r.get('text')

# 处理私聊消息


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    logger.info(msg)
    if msg['Text'] == '更多':
        reply = '全程准备状态，消息统一固定时间处理。\n回复【99】为什么?\n回复【98】什么时候有空？\n回复【97】紧急联系\n回复【96】十万火急\n回复【95】履约\n回复【94】都不是'
    elif msg['Text'] == '99':
        reply = '没有为什么呢，亲亲，这边建议您别老往脑子灌水，会坏掉的呢'
    elif msg['Text'] == '98':
        reply = '明年呢亲亲，2019-12-31 星期二'
    elif msg['Text'] == '97':
        reply = '发送问题到邮箱huangliusong2020@qq.com，附上电话，看到立即回电呢亲亲'
    elif msg['Text'] == '96':
        reply = '十万火急就直接打电话啊还发什么微信呢亲亲'
    elif msg['Text'] == '95':
        reply = '未曾忘记，延后'
    elif msg['Text'] == '94':
        reply = '这个问题可难倒hls了，请将问题简化，稍后处理。[大哭]'
    else:
        reply = get_response(msg['Text'])
        reply = reply+'\n\n回复【更多】获取更多内容。'
    logger.info('\n')
    return reply

# 处理群聊消息


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def tuling_reply(msg):
    pattern = re.compile('.*@' + nickName + '.*')
    match = pattern.match(msg['Text'])
    # 被艾特才回复
    if match != None:
        # 去掉艾特和名字，以此作为收到的消息
        r = msg['Text'].replace('@' + nickName, '')
        reply = get_response(r)
        return reply


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
# itchat.auto_login(hotReload=True)
itchat.run()
