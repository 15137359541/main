# ecoding:UTF-8
import MyCtpApi, sys, os, time, json
'''
子账号可以跟单
'''
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

mainuser = phAccount()
mainuser.userID = '118336'
mainuser.password = "147258369"
mainuser.brokerID = "9999"
mainuser.company = u"Z模拟"
mainuser.operator = u"telecom"
mainuser.tdAddress = "180.168.146.187:10001"
mainuser.mdAddress = "180.168.146.187:10011"
mainuser.mainFlag = False
mainuser.strike = 3
mainuser.accountID = ".".join((mainuser.userID, mainuser.brokerID))

mainuser.childs = []
mainuser.father = None

# agentuser = phAccount()
# agentuser.userID = '123141'
# agentuser.password = "062929AAA"
# agentuser.brokerID = "9999"
# agentuser.company = u"模拟"
# agentuser.operator = u"电信"
# agentuser.tdAddress = "180.168.146.187:10001"
# agentuser.mdAddress = "180.168.146.187:10011"
# agentuser.mainFlag = False
# agentuser.strike = 3
# agentuser.accountID = ".".join((agentuser.userID, agentuser.brokerID))
#
# agentuser.childs = []
# agentuser.father = None


class Mform():
    def __init__(self):
        self.mainCTPList = []
        self.agentCTPList = []
        self.getAccounts()
        self.ee = EventEngine()
        self.ee.start()
        self.setupCTP(self.ee)


    def getAccounts(self):

        filename = 'G:/main/accounts.ph'
        self.mainAccountList, self.agentAccountList = getAccounts(filename)
        print('账号是', self.mainAccountList)
        return self.mainAccountList, self.agentAccountList

    def setupCTP(self, eventEngine):
        for i in self.agentAccountList:
            print('i is ', i)
            self.agentCTPList.append(setupAgentCTP(i, eventEngine))
        for i in self.mainAccountList:
            print('mainaccountlist_i is ', i)
            self.mainCTPList.append(setupMainCTP(i, eventEngine))

        for i in self.mainAccountList:
            if len(i.childs) > 0:
                print('有孩子')
                print(i.childs)
                print(i.userID)

                mainCtp = getCTP(i, self.mainCTPList)
                for j in i.childs:
                    agentCtp = getCTP(j, self.agentCTPList)
                    mainCtp.childList.append(agentCtp)
                    agentCtp.father = mainCtp
    def getCTPList(self):
        return self.mainCTPList,self.agentCTPList
    # 关联
    def relevance(self):
        mainAccount=self.mainAccountList[0]
        agentAccount=self.agentAccountList[0]
        mainCtp = getCTP(mainAccount,self.mainCTPList)
        agentCtp = getCTP(agentAccount,self.agentCTPList)
        agentCtp.opposite = False
        for i in mainCtp.childList:
            print('main have guanlian')
            if agentCtp is i:
                print('关联信息已经存在')
                print(agentCtp.userID)
                return
        mainAccount.childs.append(agentAccount)
        agentAccount.father = mainAccount
        mainCtp.childList.append(agentCtp)
        agentCtp.father = mainCtp


if __name__ == "__main__":
   M = Mform()
   mainctplist,agentctplist = M.getCTPList()
   for mainctp in mainctplist:
       mainctp.connect()
   # M.relevance()#必须先关联，启动子账号，否则无法跟单
   # for agentctp in agentctplist:
   #     agentctp.connect()




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
