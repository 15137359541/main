# ecoding:UTF-8
import MyCtpApi, sys, os, time, json

reload(sys)
sys.setdefaultencoding('utf8')
from time import sleep
from copy import copy
from datetime import datetime
from Queue import Queue, Empty
from threading import Thread

from vnpy.api.ctp import defineDict
from vnpy.trader.vtGateway import *
# from vnpy.trader.vtFunction import getTempPath
# from phFunction import getCTPPath,EventPush
from vnpy.trader.gateway.ctpGateway.language import text
from vnpy.trader.vtConstant import GATEWAYTYPE_FUTURES
from vnpy.event import EventEngine, Event
from vnpy.trader.vtEngine import MainEngine
from vnpy.trader.gateway.ctpGateway.ctpGateway import *

from phCTP import *
from phFunction import *
from phObject import *
from mysql_template import SqlHelper

mainuser = phAccount()
mainuser.userID = '118336'
mainuser.password = "147258369"
mainuser.brokerID = "9999"
mainuser.company = u"模拟"
mainuser.operator = u"电信"
mainuser.tdAddress = "180.168.146.187:10001"
mainuser.mdAddress = "180.168.146.187:10011"
mainuser.mainFlag = False
mainuser.strike = 3
mainuser.accountID = ".".join((mainuser.userID, mainuser.brokerID))

mainuser.childs = []
mainuser.father = None

agentuser = phAccount()
agentuser.userID = '123141'
agentuser.password = "062929AAA"
agentuser.brokerID = "9999"
agentuser.company = u"模拟"
agentuser.operator = u"电信"
agentuser.tdAddress = "180.168.146.187:10001"
agentuser.mdAddress = "180.168.146.187:10011"
agentuser.mainFlag = False
agentuser.strike = 3
agentuser.accountID = ".".join((agentuser.userID, agentuser.brokerID))

agentuser.childs = []
agentuser.father = None


class Mform():
    def __init__(self):
        self.mainCTPList = []
        self.agentCTPList = []
        self.getAccountsM()
        self.ee = EventEngine()
        self.ee.start()
        self.setupCTP(self.ee)
        #初始化订阅列表
        self.subscribeSetup()

    def subscribeSetup(self):
        for i in self.mainAccountList:
            for j in self.mainCTPList:
                if j.userID ==i.userID:
                    j.subscribeList=i.subscribes
    def getAccountsM(self):

        filename = os.getcwd() + r"\\accounts.ph"
        self.mainAccountList, self.agentAccountList = getAccounts(filename)
        print('账号是', self.mainAccountList)
        return self.mainAccountList, self.agentAccountList

    def setupCTP(self, eventEngine):
        for i in self.agentAccountList:
            print('i is ', i)
            self.agentCTPList.append(setupAgentCTP(i, eventEngine))
        for i in self.mainAccountList:
            print('mainaccountlist_i is ', i)
            print(i.company,i.operator,i.userID,i.tdAddress,i.mdAddress,i.childs,i.subscribes)
            self.mainCTPList.append(setupMainCTP(i, eventEngine))

        for i in self.mainAccountList:
            if len(i.childs) > 0:

                mainCtp = getCTP(i, self.mainCTPList)
                for j in i.childs:
                    agentCtp = getCTP(j, self.agentCTPList)
                    mainCtp.childList.append(agentCtp)
                    agentCtp.father = mainCtp
    def getCTPList(self):
        return self.mainCTPList,self.mainAccountList

    def subscribeApi(self,subscribeObj,mainuserID):
        for i in self.mainAccountList:
            if i.userID == mainuserID:
                print('jinru')
                for sub in i.subscribes:
                    if subscribeObj.channel_id == sub.channel_id:
                        print('have subscript')
                        break
                    else:
                        pass
                else:
                    print('start subscribe...')
                    i.subscribes.append(subscribeObj)
                    self.save()
                    #ctp列表中订阅
                    for j in self.mainCTPList:
                        if j.userID == i.userID:
                            j.subscribeList.append(subscribeObj)


            else:
                print('没有此操盘手：%s' % mainuserID)
        return self.mainAccountList
    def unsubscribeApi(self,subscribeObj,mainuserID):
        for i in self.mainAccountList:
            if i.userID == mainuserID:
                print('jinru')
                for sub in i.subscribes:
                    if subscribeObj.channel_id == sub.channel_id:
                        print('delect subscribe')
                        i.subscribes.remove(sub)
                        self.save()
                        # ctp列表中删除订阅
                        for j in self.mainCTPList:
                            if j.userID == i.userID:
                                for each in j.subscribeList:
                                    if each.channel_id ==subscribeObj.channel_id:
                                        j.subscribeList.remove(each)
                        break
                    else:
                        pass
                else:
                    print('You have not subscribed ')

        return self.mainAccountList
    def save(self):
        filename = os.getcwd() + r"\\accounts.ph"
        accounts = shelve.open(filename)
        accounts['mainAccountList'] = self.mainAccountList
        accounts['agentAccountList'] = self.agentAccountList
        accounts.close()

    def new(self,userID,password,brokerID,company,operator,tdAddress,mdAddress):
        mainuser = phAccount()
        mainuser.userID = userID
        mainuser.password = password
        mainuser.brokerID =brokerID
        mainuser.company =company
        mainuser.operator = operator
        mainuser.tdAddress =tdAddress
        mainuser.mdAddress = mdAddress
        mainuser.mainFlag = True
        for i in self.mainAccountList:
            if userID == i.userID:
                print('user have exist')
                num = input('1,确定修改，2 退出')
                if num ==1:
                    print('sjsj')
                    i.userID=userID
                    i.password = password
                    i.brokerID = brokerID
                    i.company = company
                    i.operator = operator
                    i.tdAddress = tdAddress
                    i.mdAddress = mdAddress
                    # self.mainAccountList.pop()
                    self.save()
                    break
                else:
                    print('tuichu')
                    break
        else:
            print('else zhixing')
            self.mainAccountList.append(mainuser)
            self.save()
        return self.mainAccountList




if __name__ == "__main__":
   M = Mform()
   userID = '118336'
   password = "147258369"
   brokerID = "9999"
   company = u"模拟"
   operator = u"电信"
   tdAddress = u"tcp://"+"180.168.146.187:10001"
   mdAddress = ''

   subObject = SubscribeObject()
   subObject.token ='1e74812f38fa0a8707567dfbc9b6cfda'
   subObject.openid ='o7K_g04fAv1dExrgfGFqnz33E7mA'
   subObject.channel_id = '1'



   # s = M.unsubscribeApi(subObject, '118336')
   # for i in s:
   #      print('zhu',i.userID,i.subscribes)


   # n = M.new(userID,password,brokerID,company,operator,tdAddress,mdAddress)
   # for i in n:
   #     print(i.userID,i.brokerID)


   # n =M.subscribeApi(subObject,'118336')
   # for i in n:
   #     print('zhu',i.userID,i.subscribes)


   mainctplist,mainaccountlist = M.getCTPList()
   print(len(mainctplist))

   for i in mainctplist:
       print('i is ',i)
       print('dd',i.subscribeList)
       i.connect()
   # for i in mainaccountlist:
   #     print(i.userID, i.password, i.brokerID, i.company, i.operator, i.tdAddress, i.mdAddress, i.mainFlag, i.accountID)




# userID='118336'
# brokerID='9999'
# accountID = "".join((userID, brokerID))
# def atest(event):
# 	print event.dict_['data']
# 	print('ddd')
# ee=EventEngine()
# # ee.register(".".join(("orderSend",accountID)),atest)
# # ee.start(timer=True)
#
# a=MainCtp(ee,userID,'147258369',"9999",
# 	"tcp://180.168.146.187:10001","tcp://180.168.146.187:10001","Z模拟","telecom")
# print a
# a.connect()
# # ee.register(".".join(("orderSend",a.accountID)),atest)
# ee.start()
#
# agentID = '123141'
# agent_accountID = "".join((userID, brokerID))
# # ee1=EventEngine()
#
# mainuser.childs.append(agentuser)
# agentuser.father = mainuser
#
# b = AgentCtp(ee,agentID,'062929AAA','9999',"tcp://180.168.146.187:10001","tcp://180.168.146.187:10001","Z模拟","telecom")
# b.connect()
# # ee1.start()
#
#
#
# a.childList.append(b)
# b.father = a
