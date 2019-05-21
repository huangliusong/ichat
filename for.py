n = 100
itchat.search_friends(name='佳秀')
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    itchat.send(u'测试消息发送', '@9336e41564991ee051cc87a971ccbf473c15a4679cd8f47723da6cc803ae5b6c')
