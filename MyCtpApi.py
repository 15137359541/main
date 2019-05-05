# encoding: UTF-8

import os
import json
from copy import copy
from datetime import datetime

from vnpy.api.ctp import MdApi, TdApi, defineDict
from vnpy.trader.vtGateway import *
from vnpy.trader.vtFunction import getTempPath
from vnpy.trader.gateway.ctpGateway.language import text
from vnpy.trader.vtConstant import GATEWAYTYPE_FUTURES

priceTypeMap = {}
priceTypeMap[PRICETYPE_LIMITPRICE] = defineDict["THOST_FTDC_OPT_LimitPrice"]
priceTypeMap[PRICETYPE_MARKETPRICE] = defineDict["THOST_FTDC_OPT_AnyPrice"]
priceTypeMapReverse = {v: k for k, v in priceTypeMap.items()} 

directionMap = {}
directionMap[DIRECTION_LONG] = defineDict['THOST_FTDC_D_Buy']
directionMap[DIRECTION_SHORT] = defineDict['THOST_FTDC_D_Sell']
directionMapReverse = {v: k for k, v in directionMap.items()}

offsetMap = {}
offsetMap[OFFSET_OPEN] = defineDict['THOST_FTDC_OF_Open']
offsetMap[OFFSET_CLOSE] = defineDict['THOST_FTDC_OF_Close']
offsetMap[OFFSET_CLOSETODAY] = defineDict['THOST_FTDC_OF_CloseToday']
offsetMap[OFFSET_CLOSEYESTERDAY] = defineDict['THOST_FTDC_OF_CloseYesterday']
offsetMapReverse = {v:k for k,v in offsetMap.items()}

exchangeMap = {}
exchangeMap[EXCHANGE_CFFEX] = 'CFFEX'
exchangeMap[EXCHANGE_SHFE] = 'SHFE'
exchangeMap[EXCHANGE_CZCE] = 'CZCE'
exchangeMap[EXCHANGE_DCE] = 'DCE'
exchangeMap[EXCHANGE_SSE] = 'SSE'
exchangeMap[EXCHANGE_INE] = 'INE'
exchangeMap[EXCHANGE_UNKNOWN] = ''
exchangeMapReverse = {v:k for k,v in exchangeMap.items()}

posiDirectionMap = {}
posiDirectionMap[DIRECTION_NET] = defineDict["THOST_FTDC_PD_Net"]
posiDirectionMap[DIRECTION_LONG] = defineDict["THOST_FTDC_PD_Long"]
posiDirectionMap[DIRECTION_SHORT] = defineDict["THOST_FTDC_PD_Short"]
posiDirectionMapReverse = {v:k for k,v in posiDirectionMap.items()}

productClassMap = {}
productClassMap[PRODUCT_FUTURES] = defineDict["THOST_FTDC_PC_Futures"]
productClassMap[PRODUCT_OPTION] = defineDict["THOST_FTDC_PC_Options"]
productClassMap[PRODUCT_COMBINATION] = defineDict["THOST_FTDC_PC_Combination"]
productClassMapReverse = {v:k for k,v in productClassMap.items()}

# 委托状态映射
statusMap = {}
statusMap[STATUS_ALLTRADED] = defineDict["THOST_FTDC_OST_AllTraded"]
statusMap[STATUS_PARTTRADED] = defineDict["THOST_FTDC_OST_PartTradedQueueing"]
statusMap[STATUS_NOTTRADED] = defineDict["THOST_FTDC_OST_NoTradeQueueing"]
statusMap[STATUS_CANCELLED] = defineDict["THOST_FTDC_OST_Canceled"]
statusMapReverse = {v:k for k,v in statusMap.items()}

class CtpMdApi(MdApi):

	def __init__(self):
		super(CtpMdApi, self).__init__()
		
		pass
		
	#----------------------------------------------------------------------
	def onFrontConnected(self):
		pass
	
	#----------------------------------------------------------------------  
	def onFrontDisconnected(self, n):
		pass
		
	#---------------------------------------------------------------------- 
	def onHeartBeatWarning(self, n):
		pass
	
	#----------------------------------------------------------------------   
	def onRspError(self, error, n, last):
		pass

	def onRspUserLogin(self, data, error, n, last):
		pass

	#---------------------------------------------------------------------- 
	def onRspUserLogout(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------  
	def onRspSubMarketData(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------  
	def onRspUnSubMarketData(self, data, error, n, last):
		pass  
		
	#----------------------------------------------------------------------  
	def onRtnDepthMarketData(self, data):
		pass
		
	#---------------------------------------------------------------------- 
	def onRspSubForQuoteRsp(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspUnSubForQuoteRsp(self, data, error, n, last):
		pass 
		
	#---------------------------------------------------------------------- 
	def onRtnForQuoteRsp(self, data):
		pass		
		
	#----------------------------------------------------------------------
	def connect(self, userID, password, brokerID, address):
		pass
		
	#----------------------------------------------------------------------
	def subscribe(self, subscribeReq):
		pass  
		
	#----------------------------------------------------------------------
	def login(self):
		pass
	
	#----------------------------------------------------------------------
	def close(self):
		self.exit()
		
	#----------------------------------------------------------------------
	def writeLog(self, content):
		log = VtLogData()
		log.gatewayName = self.gatewayName
		log.logContent = content
		self.gateway.onLog(log)		

class CtpTdApi(TdApi):
	
	#----------------------------------------------------------------------
	def __init__(self):
		super(CtpTdApi, self).__init__()
		
	#----------------------------------------------------------------------
	def onFrontConnected(self):
		pass
		
	#----------------------------------------------------------------------
	def onFrontDisconnected(self, n):
		pass
		
	#----------------------------------------------------------------------
	def onHeartBeatWarning(self, n):
		pass
		
	#----------------------------------------------------------------------
	def onRspAuthenticate(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspUserLogin(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspUserLogout(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspUserPasswordUpdate(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspTradingAccountPasswordUpdate(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspOrderInsert(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspParkedOrderInsert(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspParkedOrderAction(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspOrderAction(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspQueryMaxOrderVolume(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspSettlementInfoConfirm(self, data, error, n, last):
		pass
		
	#----------------------------------------------------------------------
	def onRspRemoveParkedOrder(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspRemoveParkedOrderAction(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspExecOrderInsert(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspExecOrderAction(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspForQuoteInsert(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQuoteInsert(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQuoteAction(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspLockInsert(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspCombActionInsert(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryOrder(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryTrade(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInvestorPosition(self, data, error, n, last):
		"""持仓查询回报"""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryTradingAccount(self, data, error, n, last):
		"""资金账户查询回报"""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInvestor(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryTradingCode(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInstrumentMarginRate(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInstrumentCommissionRate(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryExchange(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryProduct(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInstrument(self, data, error, n, last):
		"""合约查询回报"""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryDepthMarketData(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQrySettlementInfo(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryTransferBank(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInvestorPositionDetail(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryNotice(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQrySettlementInfoConfirm(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInvestorPositionCombineDetail(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryCFMMCTradingAccountKey(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryEWarrantOffset(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInvestorProductGroupMargin(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryExchangeMarginRate(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryExchangeMarginRateAdjust(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryExchangeRate(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQrySecAgentACIDMap(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryProductExchRate(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryProductGroup(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryOptionInstrTradeCost(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryOptionInstrCommRate(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryExecOrder(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryForQuote(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryQuote(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryLock(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryLockPosition(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryInvestorLevel(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryExecFreeze(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryCombInstrumentGuard(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryCombAction(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryTransferSerial(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryAccountregister(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspError(self, error, n, last):
		"""错误回报"""
		pass
		
	#----------------------------------------------------------------------
	def onRtnOrder(self, data):
		"""报单回报"""
		# 更新最大报单编号
		pass
		
	#----------------------------------------------------------------------
	def onRtnTrade(self, data):
		"""成交回报"""
		# 创建报单数据对象
		pass
	#----------------------------------------------------------------------
	def onErrRtnOrderInsert(self, data, error):
		"""发单错误回报（交易所）"""
		# 推送委托信息
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnOrderAction(self, data, error):
		"""撤单错误回报（交易所）"""
		pass
		
	#----------------------------------------------------------------------
	def onRtnInstrumentStatus(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnTradingNotice(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnErrorConditionalOrder(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnExecOrder(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnExecOrderInsert(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnExecOrderAction(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnForQuoteInsert(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnQuote(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnQuoteInsert(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnQuoteAction(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnForQuoteRsp(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnCFMMCTradingAccountToken(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnLock(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnLockInsert(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnCombAction(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnCombActionInsert(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryContractBank(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryParkedOrder(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryParkedOrderAction(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryTradingNotice(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryBrokerTradingParams(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQryBrokerTradingAlgos(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQueryCFMMCTradingAccountToken(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnFromBankToFutureByBank(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnFromFutureToBankByBank(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnRepealFromBankToFutureByBank(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnRepealFromFutureToBankByBank(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnFromBankToFutureByFuture(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnFromFutureToBankByFuture(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnRepealFromBankToFutureByFutureManual(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnRepealFromFutureToBankByFutureManual(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnQueryBankBalanceByFuture(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnBankToFutureByFuture(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnFutureToBankByFuture(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnRepealBankToFutureByFutureManual(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnRepealFutureToBankByFutureManual(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onErrRtnQueryBankBalanceByFuture(self, data, error):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnRepealFromBankToFutureByFuture(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnRepealFromFutureToBankByFuture(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspFromBankToFutureByFuture(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspFromFutureToBankByFuture(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRspQueryBankAccountMoneyByFuture(self, data, error, n, last):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnOpenAccountByBank(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnCancelAccountByBank(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def onRtnChangeAccountByBank(self, data):
		""""""
		pass
		
	#----------------------------------------------------------------------
	def connect(self, userID, password, brokerID, address, authCode, userProductInfo):
		"""初始化连接"""
		pass
	
	#----------------------------------------------------------------------
	def login(self):
		"""连接服务器"""
		# 如果填入了用户名密码等，则登录
		pass 
			
	#----------------------------------------------------------------------
	def authenticate(self):
		"""申请验证"""
		pass

	#----------------------------------------------------------------------
	def qryAccount(self):
		"""查询账户"""
		pass
		
	#----------------------------------------------------------------------
	def qryPosition(self):
		"""查询持仓"""
		pass
		
	#----------------------------------------------------------------------
	def sendOrder(self, orderReq):
		"""发单"""
		pass
	
	#----------------------------------------------------------------------
	def cancelOrder(self, cancelOrderReq):
		"""撤单"""
		pass
		
	#----------------------------------------------------------------------
	def close(self):
		"""关闭"""
		self.exit() # 这个是TdApi自带的Api

	#----------------------------------------------------------------------
	def writeLog(self, content):
		"""发出日志"""
		pass	