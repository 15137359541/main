# encoding:UTF-8
from collections import Counter

# 定义账户信息数据结构
class phAccount(object):
	def __init__(self):
		self.userID=""
		self.password=""
		self.brokerID=""
		self.company=""
		self.operator=""
		self.tdAddress=""
		self.mdAddress=""
		self.mainFlag=False
		self.strike=3
		self.accountID=".".join((self.userID,self.brokerID))

		# self.ctp=None
		self.childs=[]
		self.father=None


		self.subscribes = []
		self.mysqlChilds = []
		self.mysqlFather = []

class EditTreeItem(object):
	"""docstring for EditItem"""
	def __init__(self):

		self.index=-1
		self.ctp=None

		self.flag=False

		self.isNone=True

		self.accountIndex=-1
		self.account=None

class ShowCtp(object):
	def __init__(self):

		self.index=None
		self.ctp=None
		self.isNone=True

class PositionDetail(object):
	def __init__(self):

		self.flag=True

		self.data=[]

		self.data.append(self.flag)

	def init_(self):
		self.data=[]
		self.data.append(self.flag)

class SubscribeObject():
	def __init__(self):
		self.token=''
		self.openid=''
		self.channel_id=''
		