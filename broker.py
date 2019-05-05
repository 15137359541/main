# encoding:UTF-8

import shelve,os
filename='G:/main/broker.ph'
db=shelve.open(filename)
brokerDict=db['brokerDict']
# 添加入模拟账号

brokerDict[u'9999']={'name':u'Z模拟','nameEN':"",
            'Servers':{
                'telecom':{
                    'trading':["180.168.146.187:10001"],
                    'market':["180.168.146.187:10011"]
                },'unicom':{
                    'trading':[],
                    'market':[]},
                'netcom':{
                    'trading':[],
                    'market':[]
            }}}
db.close()

if __name__ =="__main__":
    print brokerDict
  

