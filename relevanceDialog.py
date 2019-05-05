# encoding:UTF-8
import os,sys
import shelve

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui_relevanceDialog
from phObject import phAccount

class RelevanceDialog(QDialog,ui_relevanceDialog.Ui_relevanceDialog):
	"""docstring for RelevanceDialog"""
	def __init__(self, parent=None,mainlist=None,agentlist=None):
		super(RelevanceDialog, self).__init__(parent)
		self.setupUi(self)

		self.mainlist=mainlist
		self.agentlist=agentlist
		self.strike=3
		if self.mainlist is not None:
			for i in self.mainlist:
				msg="".join((u"期货公司：",i.company,u" 账号：",i.userID))
				self.relevanceMainComboBox.addItem(unicode(msg))
		if self.agentlist is not None:
			for i in self.agentlist:
				msg="".join(("期货公司：",i.company," 账号：",i.userID))
				self.relevanceAgentComboBox.addItem(unicode(msg))


		self.buttonBox.accepted.connect(self.relevanceAccept)
		self.buttonBox.rejected.connect(self.reject)

	def relevanceAccept(self):
		self.mainAccount=self.mainlist[self.relevanceMainComboBox.currentIndex()]
		self.agentAccount=self.agentlist[self.relevanceAgentComboBox.currentIndex()]
		self.strike=self.slipSpinBox.value()
		self.multiple=self.multipleDoubleSpinBox.value()
		
	
		if self.oppositeCheckBox.checkState()==2:
			self.oppositeFlag=True
		else:
			self.oppositeFlag=False
		self.accept()

if __name__=='__main__':
	class phAccount(object):
		def __init__(self):
			self.userID = ""
			self.password = ""
			self.brokerID = ""
			self.company = ""
			self.operator = ""
			self.tdAddress = ""
			self.mdAddress = ""
			self.mainFlag = False
			self.strike = 3
			self.accountID = ".".join((self.userID, self.brokerID))

			# self.ctp=None
			self.childs = []
			self.father = None

	mainlist = phAccount()
	mainlist.userID='118336'
	mainlist.password = "147258369"
	mainlist.brokerID = "9999"
	mainlist.company = u"模拟"
	mainlist.operator = u"电信"
	mainlist.tdAddress = "180.168.146.187:10001"
	mainlist.mdAddress = "180.168.146.187:10011"
	mainlist.mainFlag = False
	mainlist.strike = 3
	mainlist.accountID = ".".join((mainlist.userID, mainlist.brokerID))

	mainlist.childs = []
	mainlist.father = None
	res =[]
	res.append(mainlist)

	app=QApplication(sys.argv)
	f=RelevanceDialog(mainlist=res,agentlist=None)
	f.show()
	app.exec_()


