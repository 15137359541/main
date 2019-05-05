# encoding:UTF-8
import os, sys
import shelve

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui_newAccountDialog
from broker import brokerDict
from phObject import *
from phFunction import getAccounts
from tt1 import mxhMysql


class NewAccountDialog(QDialog, ui_newAccountDialog.Ui_Dialog):
    def __init__(self, parent=None):
        super(NewAccountDialog, self).__init__(parent)
        self.setupUi(self)
        # self.setAttribute(Qt.WA_DeleteOnClose) # 关闭即删除
        self.brokerDict = brokerDict
        self.nameDict = {}  # 存储期货公司名与brokerID字典
        self.operators = [u'电信', u'联通', u'网通']  # 运营上列表
        self.newAccount = phAccount()
        # 设置文本框输入保护为密码
        self.passwordLineEdit.setEchoMode(2)
        self.getBrokers()
        self.getOperators()
        self.getTdAddress()

        self.brokerNameComboBox.currentIndexChanged.connect(self.getTdAddress)
        self.operatorComboBox.currentIndexChanged.connect(self.getTdAddress)

        self.buttonBox.accepted.connect(self.accountAccept)
        self.buttonBox.rejected.connect(self.reject)

    def accountAccept(self):
        self.newAccount.userID = self.userIDLineEdit.text()
        self.newAccount.password = self.passwordLineEdit.text()
        self.newAccount.brokerID = self.nameDict[self.brokerNameComboBox.currentText()]
        self.newAccount.operator = self.operatorComboBox.currentText()
        self.newAccount.tdAddress = u"tcp://" + self.tdAddressComboBox.currentText()
        self.newAccount.company = self.brokerNameComboBox.currentText()[1:]

        # if self.accountCheckBox.checkState() == 2:#2代表选中，0代表没有选中
        self.newAccount.mainFlag = True
        # print self.newAccount.password
        # filename = os.getcwd() + r"\\accounts.ph"
        # mainAccountList, agentAccountList = getAccounts(filename)
        mainAccountList = mxhMysql().getAccount()

        if self.newAccount.userID == "" or self.newAccount.password == "":
            QMessageBox.warning(self, u"添加账户信息",
                                u"用户名与密码均不能为空！")
        else:
            for i in mainAccountList:
                if self.newAccount.userID == i.userID and self.newAccount.brokerID == i.brokerID:
                    QMessageBox.warning(self, u"添加账户信息",
                                        u"添加的主账户已存在！")
                    return
            # 只要不执行accept，那么对话框就一直存在
            self.accept()
        # return self.newAccount

    def getBrokers(self):
        # 填充期货公司下拉框
        for brokerID, values in self.brokerDict.items():
            self.nameDict[values['name']] = brokerID
        borkerList = []
        for i in self.nameDict.keys():
            borkerList.append(i)

        borkerList.sort()
        for i in borkerList:
            self.brokerNameComboBox.addItem(i)

    def getOperators(self):
        for i in self.operators:
            self.operatorComboBox.addItem(i)

    def getTdAddress(self):
        name = self.brokerNameComboBox.currentText()
        brokerID = self.nameDict[name]
        self.tdAddressComboBox.clear()

        operatorText = self.operatorComboBox.currentText()
        print operatorText
        if operatorText == u'电信':
            operator = 'telecom'
        elif operatorText == u'联通':
            operator = 'unicom'
        else:
            operator = 'netcom'

        for i in self.brokerDict[brokerID]['Servers'][operator]['trading']:
            self.tdAddressComboBox.addItem(i)
        print self.brokerDict[brokerID]['Servers'][operator]['trading']


if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = NewAccountDialog()
    f.show()
    app.exec_()
