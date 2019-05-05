# encoding:UTF-8
from vnpy.event import EventEngine,Event
import os,shelve
from phCTP import MainCtp,AgentCtp
import decimal



def getAccounts(filename):
	accounts=shelve.open(filename)
	try:
		mainAccountList=accounts['mainAccountList']
	except KeyError:
		mainAccountList=[]
	try:
		agentAccountList=accounts['agentAccountList']
	except KeyError:
		agentAccountList=[]
	accounts.close()
	return mainAccountList,agentAccountList

def getCTP(account,ctplist):
	for i in ctplist:
		if account.userID==i.userID and account.brokerID==i.brokerID:
			return i
	return False

def getCTPFromTree(userID,company,ctplist,accountlist):
	index=-1
	accountIndex=-1
	ctp=None
	account=None
	for k,i in enumerate(ctplist):
		if userID==i.userID and company==i.company:
			index=k
			ctp=i
	for k,i in enumerate(accountlist):
		if userID==i.userID and company==i.company:
			accountIndex=k
			account=i
	return index,ctp,accountIndex,account
def getCTPFromBrokerID(brokerID,userID,ctplist):
	for k,i in enumerate(ctplist):
		if brokerID==i.brokerID and userID==i.userID:
			return k,i
	return False


def setupMainCTP(account,eventEngine):
	main=MainCtp(eventEngine,str(account.userID),str(account.password),
		str(account.brokerID),str(account.tdAddress),str(account.mdAddress),
		account.company,account.operator)	
	return main

def setupAgentCTP(account,eventEngine):
	agent=AgentCtp(eventEngine,str(account.userID),str(account.password),
		str(account.brokerID),str(account.tdAddress),str(account.mdAddress),
		account.company,account.operator,account.strike)
	return agent

def getLogFilePath(filename):
	tempPath=os.path.join(os.getcwd(),'temp','log')
	if not os.path.exists(tempPath):
		os.makedirs(tempPath)
	path=os.path.join(tempPath,filename)
	return path

MAX_NUMBER = 10000000000000
MAX_DECIMAL = 4


#----------------------------------------------------------------------
def safeUnicode(value):

    if type(value) is int or type(value) is float:
        if value > MAX_NUMBER:
            value = 0

    if type(value) is float:
        d = decimal.Decimal(str(value))
        if abs(d.as_tuple().exponent) > MAX_DECIMAL:
            value = round(value, ndigits=MAX_DECIMAL)
    
    return unicode(value)


