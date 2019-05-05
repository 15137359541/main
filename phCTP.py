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
from vnpy.trader.gateway.ctpGateway.language import text
from vnpy.trader.vtConstant import GATEWAYTYPE_FUTURES
from vnpy.event import EventEngine, Event
from vnpy.trader.vtEngine import MainEngine
from vnpy.trader.gateway.ctpGateway.ctpGateway import *
from tt1 import mxhMysql

from phObject import PositionDetail
from mxh_work.wechat_main import wechatInterface
from mxh_work.getIP import IpMain


class BaseCtp(MyCtpApi.CtpTdApi):
    def __init__(self, eventEngine, userID, password, brokerID,
                 tdaddress, mdAddress, company, operator):
        super(BaseCtp, self).__init__()
        self.userID = userID
        self.password = password
        self.brokerID = brokerID
        self.address = tdaddress
        self.mdAddress = mdAddress
        self.company = company
        self.operator = operator

        self.reqID = 0
        self.orderRef = 0
        self.connectionStatus = False
        self.loginStatus = False
        self.eventEngine = eventEngine
        self.eventPush = EventPush(self.eventEngine)
        self.accountID = "".join((self.userID, self.brokerID))

        self.multiple = 1

        self.opposite = False

        self.positionDetail = PositionDetail()

    def connect(self):
        self.accountID = "".join((self.userID, self.brokerID))
        self.path = getCTPPath(self.accountID)
        if not self.connectionStatus:
            self.createFtdcTraderApi(str(self.path))
            self.subscribePrivateTopic(0)
            self.subscribePublicTopic(0)
            self.registerFront(str(self.address))
            self.init()
        else:
            self.login()

    def getListMsg(self, string):
        return " ".join((self.company, u"账号：", self.userID, string))

    def onFrontConnected(self):
        self.connectionStatus = True
        self.login()

    def login(self):
        req = {}
        req['UserID'] = self.userID
        req['Password'] = self.password
        req['BrokerID'] = self.brokerID
        self.reqID += 1
        if not self.loginStatus:
            self.reqUserLogin(req, self.reqID)
        else:
            # self.eventPush.addListWidget(self.getListMsg(u"-已经登录"))
            pass

    def onFrontDisconnected(self, n):
        self.connectionStatus = False

    def onRspUserLogin(self, data, error, n, last):
        if error['ErrorID'] == 0:
            self.frontID = str(data['FrontID'])
            self.sessionID = str(data['SessionID'])
            self.loginStatus = True
            req = {}
            req['BrokerID'] = self.brokerID
            req['InvestorID'] = self.userID
            self.reqID += 1
            self.reqSettlementInfoConfirm(req, self.reqID)

        else:
            pass

    def onRspSettlementInfoConfirm(self, data, error, n, last):
        # sleep(1)
        pass

    def close(self):
        self.loginStatus = False
        self.connectionStatus = False
        sleep(1)
        self.exit()

    def qryInvestorPositionDetail(self):
        sleep(1)
        self.reqID += 1
        req = {}
        req['BrokerID'] = self.brokerID
        req['InvestorID'] = self.userID
        self.reqQryInvestorPositionDetail(req, self.reqID)

    def onRspQryInvestorPositionDetail(self, data, error, n, last):

        if data['Volume'] != 0:
            self.positionDetail.data.append(data)
        if last:
            self.eventPush.addTable(self.positionDetail.data)
            self.positionDetail.init_()


class MainCtp(BaseCtp):
    def __init__(self, eventEngine, userID, password, brokerID,
                 tdaddress, mdAddress, company, operator):
        super(MainCtp, self).__init__(eventEngine, userID, password, brokerID,
                                      tdaddress, mdAddress, company, operator)
        self.childList = []
        self.flag = True

        self.strike = 3

        self.positionDetail.flag = True
        self.positionDetail.data[0] = True
        self.subscribeList =[]

    def onRtnTrade(self, data):

        if data:
            for i in data:
                print(i,':',data[i])
        print('________________')
        # for i in defineDict:
        #     print(i,':',defineDict[i])
        newRef = data['OrderRef']
        self.orderRef = max(self.orderRef, int(newRef))
        self.symbol = data['InstrumentID']
        self.exchange = data['ExchangeID']
        self.tradeID = data['TradeID']
        self.direction = data['Direction']
        self.offset = data['OffsetFlag']
        self.price = data['Price']
        self.volume = data['Volume']
        self.tradeTime = data['TradeTime']
        if self.direction == "0":
            direction = "买"
        else:
            direction = "卖"

        if self.offset == "0":
            offset = "开仓"
        elif self.offset == "1":
            offset = "平仓"
        elif self.offset == "2":
            offset = "强平"
        elif self.offset == "3":
            offset = "平今"
        elif self.offset == "4":
            offset = "平昨"
        elif self.offset == "5":
            offset = "强减"
        elif self.offset == "6":
            offset = "本地强平"
        string = u"开单信息 "
        string += u"方向:" + unicode(direction)
        string += u",开平仓:" + unicode(offset)
        string += u",价格:" + unicode(self.price)
        string += u",手数:" + unicode(self.volume)
        string += u",成交时间(服务器时间):" + unicode(self.tradeTime)

        print ('main_ctp_onreturntrade kai dan xin xi ',string)

        eventType = str(".".join(("orderSend", self.accountID)))
        event = Event(type_=eventType)
        orderData = {}
        orderData['InstrumentID'] = data['InstrumentID']
        orderData['ExchangeID'] = data['ExchangeID']
        orderData['TradeID'] = data['TradeID']
        orderData['Direction'] = data['Direction']
        orderData['OffsetFlag'] = data['OffsetFlag']
        orderData['Price'] = data['Price']
        orderData['Volume'] = data['Volume']
        orderData['TradeTime'] = data['TradeTime']

        event.dict_['data'] = orderData
        t = self.tradeTime.split(":")
        t = float(t[0]) * 60 * 60 + float(t[1]) * 60 + float(t[2])

        from datetime import datetime
        now = datetime.now()
        now = now.hour * 60 * 60 + now.minute * 60 + now.second

        print ('onreturntrade time',now - t)
        if now - t < 10:
            self.eventEngine.put(event)
            self.eventPush.addListWidget(u"主帐号" + \
                                         self.getListMsg(u" 监听到下单信息::") + string)
            self.eventPush.addLog(string)
            #将交易记录保存在数据库中
            res=mxhMysql().transactionRecord(data)
            if res:
                print('save data yes',res)
            else:
                print('save data No',res)

            if self.subscribeList:
                for i in self.subscribeList:
                    print('i is', i)
                    if type(i) == tuple or type(i) == list:
                        url = 'https://wechat.17aitec.xyz/api/trade/temmsg'

                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
                        }

                        post_data = {
                            'token': i[1],
                            'channel_id': i[0],
                            'keyword1': data['InstrumentID'],
                            'keyword2': data['Price'],
                            'keyword3': direction + '/' + offset,
                            'keyword4': data['Volume'],
                            'keyword5': data['TradeTime'],
                        }
                        con = wechatInterface(url, post_data).run()
                        print(con)
            else:
                print('self.subscribe is none')


            # #给微信发消息
            # if self.subscribeList:
            #     print(self.subscribeList)
            #     for i in self.subscribeList:
            #         url = 'https://wechat.17aitec.xyz/api/trade/temmsg'
            #
            #         headers = {
            #             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
            #         }
            #
            #         post_data = {
            #             'token': i.token,
            #             'channel_id': i.channel_id,
            #             'keyword1': data['InstrumentID'],
            #             'keyword2': data['Price'],
            #             'keyword3': direction + '/' + offset,
            #             'keyword4': data['Volume'],
            #             'keyword5': data['TradeTime'],
            #         }
            #         con = wechatInterface(url, post_data).run()
            #         print(con)



    def onRspOrderInsert(self, data, error, n, last):
        self.eventPush.addLog(
            self.getListMsg(error['ErrorMsg'].decode('gbk')))

    def onRtnOrder(self, data):
        pass

    def onErrRtnOrderInsert(self, data, error):
        self.eventPush.addLog(
            self.getListMsg(error['ErrorMsg'].decode('gbk')))

    def connect(self):
        super(MainCtp, self).connect()
        if not self.connectionStatus:
            self.eventPush.addListWidget(u"主帐号" + self.getListMsg(u"-尝试连接"))
            print('mxh_尝试连接')
        else:
            self.eventPush.addListWidget(u"主帐号" + self.getListMsg(u"-已经连接"))
            print('mxh_已经连接')

    def onFrontConnected(self):
        super(MainCtp, self).onFrontConnected()
        # self.eventPush.addListWidget(u"主帐号" + self.getListMsg(u"-连接成功"))
        # print('mxh_连接成功')

    def onRspUserLogin(self, data, error, n, last):
        super(MainCtp, self).onRspUserLogin(data, error, n, last)
        if self.loginStatus:
            self.eventPush.addListWidget(u"主帐号" + self.getListMsg(u"-登录成功"))

            #跟新登陆日志
            #得到ip
            ip = IpMain()
            logintime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            Account_all = mxhMysql().updateLog(self.userID,ip,logintime)
            print('是否插入数据，whether or not insert data',Account_all)

            print('mxh_登陆成功')
        else:
            self.eventPush.addListWidget(u"主帐号" + self.getListMsg(u"-登录失败，请查看账号或者密码"))
            print('登录失败')

    def onRspSettlementInfoConfirm(self, data, error, n, last):
        super(MainCtp, self).onRspSettlementInfoConfirm(data, error, n, last)
        self.eventPush.addListWidget(u"主帐号" + self.getListMsg(u"-合约确认完成"))
        print('mxh_合约确定完成')

    def onFrontDisConnected(self, n):
        super(MainCtp, self).onFrontDisconnected(n)
        self.eventPush.addListWidget(u"主帐号" + self.getListMsg(u"-连接不成功"))
        print('mxh_连接不成功')

    def onRspUserLogout(self, data, error, n, last):
        pass


class AgentCtp(BaseCtp):
    def __init__(self, eventEngine, userID, password, brokerID,
                 tdaddress, mdAddress, company, operator, strike=3):
        super(AgentCtp, self).__init__(eventEngine, userID, password, brokerID,
                                       tdaddress, mdAddress, company, operator)
        self.eventEngine = eventEngine
        self.eventPush = EventPush(self.eventEngine)
        self.flag = False
        self.father = None

        self.strikePrice = {}
        self.strike = strike
        self.positionDetail.flag = False
        self.positionDetail.data[0] = False

    def onRtnOrder(self, data, error, n, last):
        newRef = data['OrderRef']
        print('newRef is ', newRef)
        self.orderRef = max(self.orderRef, int(newRef))

    def orderSend(self, event):
        self.reqID += 1
        self.orderRef += 1

        orderReq = event.dict_['data']
        print orderReq
        req = {}
        req['InstrumentID'] = orderReq['InstrumentID']
        req['VolumeTotalOriginal'] = int(orderReq['Volume'] * self.multiple)
        req['ContingentCondition'] = defineDict['THOST_FTDC_CC_Immediately']

        req['OrderPriceType'] = defineDict['THOST_FTDC_OPT_LimitPrice']

        req['TimeCondition'] = defineDict['THOST_FTDC_TC_GFD']
        #print self.opposite #false
        if not self.opposite:
            print u"正向跟单"
            print type(orderReq['Direction'])
            req['Direction'] = orderReq['Direction']
            if req['Direction'] == str(0):
                req['LimitPrice'] = float(orderReq['Price']) + \
                                    self.strike * self.strikePrice.get(req['InstrumentID'], 1)
            if req['Direction'] == str(1):
                req['LimitPrice'] = float(orderReq['Price']) - \
                                    self.strike * self.strikePrice.get(req['InstrumentID'], 1)

        else:
            print u"反向跟单"
            if orderReq['Direction'] == u'0':
                print u"反向 卖出"
                req['Direction'] = str(1)
                req['LimitPrice'] = float(orderReq['Price']) - (self.strike + 1) * self.strikePrice.get(
                    req['InstrumentID'], 1)
            else:
                print u"反向 买入"
                req['Direction'] = str(0)
                req['LimitPrice'] = float(orderReq['Price']) + (self.strike + 1) * self.strikePrice.get(
                    req['InstrumentID'], 1)

        req['CombOffsetFlag'] = orderReq['OffsetFlag']
        req['OrderRef'] = str(self.orderRef)
        req['InvestorID'] = self.userID
        req['UserID'] = self.userID
        req['BrokerID'] = self.brokerID

        req['CombHedgeFlag'] = defineDict['THOST_FTDC_HF_Speculation']
        req['ForceCloseReason'] = defineDict['THOST_FTDC_FCC_NotForceClose']
        req['IsAutoSuspend'] = 0

        req['VolumeCondition'] = defineDict['THOST_FTDC_VC_AV']
        req['MinVolume'] = 1
        req['UserForceClose'] = 0
        if req['VolumeTotalOriginal'] > 0:
            print ('req is: ', req)
            print u"买卖命令执行"
            self.reqOrderInsert(req, self.reqID)
        else:
            pass

    def connect(self):

        super(AgentCtp, self).connect()
        if not self.connectionStatus:
            self.eventPush.addListWidget(u"子帐号" + self.getListMsg(u"-尝试连接"))
            print('mxh_子账号尝试连接')
        else:
            self.eventPush.addListWidget(u"子帐号" + self.getListMsg(u"-已经连接"))
            print('mxh_子账号已经连接')

        if self.father is not None:
            self.eventEngine.register(str(".".join((u"orderSend",
                                                    self.father.accountID))), self.orderSend)

    def onFrontConnected(self):
        super(AgentCtp, self).onFrontConnected()
        self.eventPush.addListWidget(u"子帐号" + self.getListMsg(u"-连接成功"))
        print('mxh_子账号连接成功')

    def onRspUserLogin(self, data, error, n, last):
        super(AgentCtp, self).onRspUserLogin(data, error, n, last)
        if not self.loginStatus:
            self.eventPush.addListWidget(u"子帐号" + self.getListMsg(u"-登录成功"))
            print('mxh_子账号登陆成功')
        else:
            self.eventPush.addListWidget(u"子帐号" + self.getListMsg(u"-已经登录"))
            print('mxh_子账号已经登陆')

    def onRspSettlementInfoConfirm(self, data, error, n, last):
        super(AgentCtp, self).onRspSettlementInfoConfirm(data, error, n, last)
        self.eventPush.addListWidget(u"子帐号" + self.getListMsg(u"-合约确认完成"))
        self.reqID += 1
        self.reqQryInstrument({}, self.reqID)
        print('mxh——子账号合约确定完成')

    def onRspQryInstrument(self, data, error, n, last):
        symbol = data['InstrumentID']
        strikePrice = data['PriceTick']
        self.strikePrice[symbol] = float(strikePrice)

    def onFrontDisConnected(self, n):
        super(MainCtp, self).onFrontDisconnected(n)
        self.eventPush.addListWidget(u"子帐号" + self.getListMsg(u"-连接断开"))

    def onRspUserLogout(self, data, error, n, last):
        self.eventPush.addListWidget(u"子帐号" + self.getListMsg(u"-登出"))
        self.reqOrderInsert(req, self.myctp.reqID)

    def onRspOrderInsert(self, data, error, n, last):
        pass

    def onRtnOrder(self, data):
        pass

    def onRtnTrade(self, data):

        if data:
            for i in data:
                print(i, ':', data[i])
        print('*****************')
        newRef = data['OrderRef']
        print('newref_on is:', newRef)
        self.orderRef = max(self.orderRef, int(newRef))
        self.symbol = data['InstrumentID']
        self.exchange = data['ExchangeID']
        self.tradeID = data['TradeID']
        self.direction = data['Direction']
        self.offset = data['OffsetFlag']
        self.price = data['Price']
        self.volume = data['Volume']
        self.tradeTime = data['TradeTime']

        if self.direction == "0":
            direction = "买"
        else:
            direction = "卖"

        if self.offset == "0":
            offset = "开仓"
        elif self.offset == "1":
            offset = "平仓"
        elif self.offset == "2":
            offset = "强平"
        elif self.offset == "3":
            offset = "平今"
        elif self.offset == "4":
            offset = "平昨"
        elif self.offset == "5":
            offset = "强减"
        elif self.offset == "6":
            offset = "本地强平"
        string = u"开单信息 "
        string += u"方向:" + unicode(direction)
        string += u",开平仓:" + unicode(offset)
        string += u",价格:" + unicode(self.price)
        string += u",手数:" + unicode(self.volume)
        string += u",成交时间(服务器时间):" + unicode(self.tradeTime)

        print (' agent ctp kai dan xin xi ,',string)

        eventType = str(".".join(("orderSend", self.accountID)))
        event = Event(type_=eventType)
        orderData = {}
        orderData['InstrumentID'] = data['InstrumentID']
        orderData['ExchangeID'] = data['ExchangeID']
        orderData['TradeID'] = data['TradeID']
        orderData['Direction'] = data['Direction']
        orderData['OffsetFlag'] = data['OffsetFlag']
        orderData['Price'] = data['Price']
        orderData['Volume'] = data['Volume']
        orderData['TradeTime'] = data['TradeTime']

        event.dict_['data'] = orderData
        t = self.tradeTime.split(":")
        t = float(t[0]) * 60 * 60 + float(t[1]) * 60 + float(t[2])
        print ('time is', t)
        from datetime import datetime
        now = datetime.now()
        now = now.hour * 60 * 60 + now.minute * 60 + now.second
        print('now is ,',now)
        print ('now-t',now - t)
        print('event is ',event)
        if now - t < 10:
            print('t is zhixing')
            self.eventEngine.put(event)

            self.eventPush.addListWidget(u"子帐号" + \
                                         self.getListMsg(u" 监听到跟单信息::") + string)
            self.eventPush.addLog(string)

    def onErrRtnOrderInsert(self, data, error):
        pass


def getCTPPath(name):
    """
    得到流文件路径："当前目录\temp\name\"
    """
    tempPath = os.path.join(os.getcwd(), 'temp', name)
    if not os.path.exists(tempPath):
        os.makedirs(tempPath)
    path = os.path.join(tempPath, name)
    return path


class EventPush(object):
    def __init__(self, eventEngine):
        self.eventEngine = eventEngine

    def addListWidget(self, data):
        event = Event(type_=u"addListWidget")
        event.dict_['data'] = data
        self.eventEngine.put(event)

    def addLog(self, data):
        event = Event(type_=u"addLog")
        event.dict_['data'] = data
        self.eventEngine.put(event)

    def addTable(self, data):
        event = Event(type_=u"addTable")
        event.dict_['data'] = data
        self.eventEngine.put(event)


