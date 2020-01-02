# ichat

ichat记录型project

## 项目文档
[文档地址](https://itchat.readthedocs.io/zh/latest/)

## linux screen工具
~~~
screen -S yourname -> 新建一个叫yourname的session
screen -ls -> 列出当前所有的session
screen -r yourname -> 回到yourname这个session
screen -d yourname -> 远程detach某个session
screen -d -r yourname -> 结束当前session并回到yourname这个session
~~~
  

## 命令行二维码显示

通过以下命令可以在登陆的时候使用命令行显示二维码：
> itchat.auto_login(enableCmdQR=True)


部分系统可能字幅宽度有出入，可以通过将enableCmdQR赋值为特定的倍数进行调整：

> itchat.auto_login(enableCmdQR=2)

默认控制台背景色为暗色（黑色），若背景色为浅色（白色），可以将enableCmdQR赋值为负值：

> itchat.auto_login(enableCmdQR=-1)


[更多详情](https://itchat.readthedocs.io/zh/latest/intro/login/#_3)

## 回复配置
~~~
import requests
import itchat
import re
import random

key = '6dde22b7692b48fe9f89ce52b2673e0f' # 这里是你自己机器人的apikey
arr=['dd6710813403477689911f4b322cf685','c3c69290cf9d4357923d2f6ece25ecdd','6dde22b7692b48fe9f89ce52b2673e0f','6fce7ad8fb354b6a91c30eb05681590a','dd6710813403477689911f4b322cf685']

nickName = '小兔几' # 这里是昵称或群昵称，用于检测群聊是否被艾特

def get_response(msg):
    a=random.randint(1,4)
    key=arr[a]
    print(key)
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {'key': key, 'info': msg, 'userid' : 'wechat-robot'}
    r = requests.post(apiUrl, data=data).json()
    # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
    print('==================================================')
    print('收到消息：', msg)
    print('回复消息：', r.get('text'))
    return r.get('text')

# 处理私聊消息
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    reply = get_response(msg['Text'])
    return reply

# 处理群聊消息
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def tuling_reply(msg):
    pattern = re.compile('.*@' + nickName + '.*')
    match = pattern.match(msg['Text'])
    # 被艾特才回复
    if match!=None:
        # 去掉艾特和名字，以此作为收到的消息
        r = msg['Text'].replace('@' + nickName, '')
        reply = get_response(r)
        return reply

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
#itchat.auto_login(hotReload=True)
itchat.run()


~~~
# for循环刷屏
## 根据备注获取这个用户的id
> itchat.search_friends(name='佳秀')


~~~
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    itchat.send(u'测试消息发送', '@9336e41564991ee051cc87a971ccbf473c15a4679cd8f47723da6cc803ae5b6c')

~~~

# 系统默认编码
~~~
import sys
print u'系统默认编码为', sys.getdefaultencoding()

default_encoding = 'utf-8'  # 重新设置编码方式为uft-8
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
print u'系统修改编码为', sys.getdefaultencoding()
~~~


~~~
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    itchat.send(u'9点了，雀儿喜起床啦！[呲牙][呲牙]', '@3b69abe6793fcce8c1910019141211192c4ea8fe924e790b8bf29f34b972dd78')

~~~



~~~
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    itchat.send(u'9点了，雀儿喜起床啦！[呲牙][呲牙]', '@2d4a92b3d9c656dba86ce30fea4a5c7ab31c42d6a9331b987048c89f43642868')

~~~
