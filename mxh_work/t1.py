# ecoding:UTF-8
import MyCtpApi,sys,os,time,json
reload(sys)
sys.setdefaultencoding('utf8')
from time import sleep
from copy import copy
from datetime import datetime
from Queue import Queue,Empty
from threading import Thread

from vnpy.api.ctp import defineDict
from vnpy.trader.vtGateway import *
# from vnpy.trader.vtFunction import getTempPath
# from phFunction import getCTPPath,EventPush
from vnpy.trader.gateway.ctpGateway.language import text
from vnpy.trader.vtConstant import GATEWAYTYPE_FUTURES
from vnpy.event import EventEngine,Event
from vnpy.trader.vtEngine import MainEngine
from vnpy.trader.gateway.ctpGateway.ctpGateway import *

from phCTP import *

userID='118336'
brokerID='9999'
accountID = "".join((userID, brokerID))
def atest(event):
	print event.dict_['data']
	print('ddd')
ee=EventEngine()
# ee.register(".".join(("orderSend",accountID)),atest)
# ee.start(timer=True)

a=MainCtp(ee,userID,'147258369',"9999",
	"tcp://180.168.146.187:10001","tcp://180.168.146.187:10001","Z模拟","telecom")
print a
a.connect()
ee.register(".".join(("orderSend",a.accountID)),atest)
# ee.register(EVENT_TIMER, atest)


ee.start()
eventType = str(".".join(("orderSend", a.accountID)))
event = Event(type_=eventType)
event.dict_ = {'data':'1','2':'b'}
ee.put(event)
ee.put(event)

# ee.register(".".join(("orderSend",a.accountID)),atest)

