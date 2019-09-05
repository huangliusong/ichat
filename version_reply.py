import requests
import itchat
import re
import random
import sys
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
    print('回复消息：', r.get('text'))
    return r.get('text')

# 处理私聊消息


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    if msg['Text'] == '更多':
        reply = '紧急备战状态，消息统一固定时间处理。\n\n'
    elif msg['Text'] == '99':
        reply = '99'
    else:
        reply = get_response(msg['Text'])
        reply = reply+'\n\n回复【更多】获取更多内容。'
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
