# encoding:UTF-8
from broker import brokerDict
from phObject import *
from phFunction import getAccounts
class NewAccountDialog():
    def __init__(self):

        self.brokerNameComboBox=[]
        self.operatorComboBox=[]
        self.tdAddressComboBox=[]

        self.brokerDict = brokerDict
        self.nameDict = {}  # 存储期货公司名与brokerID字典
        self.operators = [u'电信', u'联通', u'网通']  # 运营上列表
        self.newAccount = phAccount()

        self.getBrokers()
        self.getOperators()
        self.getTdAddress()

        OK_or_NOT = input('是否确定：1，确定，2，取消')
        if OK_or_NOT ==1:
            self.accountAccept()
        else:
            pass

    def accountAccept(self):
        self.newAccount.userID = raw_input('请输入你的账号：')
        self.newAccount.password = raw_input('请输入你的密码：')
        self.newAccount.brokerID = self.nameDict[self.name]
        self.newAccount.operator = self.operator
        self.newAccount.tdAddress = u"tcp://" + self.tdAddressComboBox[0]
        self.newAccount.company = self.name
        main_flag = raw_input('是否为主账户，1 是，2 不是')
        if main_flag==1:
            self.newAccount.mainFlag=True


        # print self.newAccount.password
        filename = 'G:/main/accounts.ph'
        mainAccountList, agentAccountList = getAccounts(filename)
        if self.newAccount.userID == "" or self.newAccount.password == "":
            print(self, u"添加账户信息",
                                u"用户名与密码均不能为空！")
        else:
            if main_flag==1:
                for i in mainAccountList:
                    if self.newAccount.userID == i.userID and self.newAccount.brokerID == i.brokerID:
                        print(self, u"添加账户信息  添加的主账户已存在！")
                        return
            else:
                for i in agentAccountList:
                    if self.newAccount.userID == i.userID and self.newAccount.brokerID == i.brokerID:
                        print(u"添加账户信息,添加的子账户已存在！")
                        return
            # 只要不执行accept，那么对话框就一直存在
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
            self.brokerNameComboBox.append(i)

    def getOperators(self):
        for i in self.operators:
            self.operatorComboBox.append(i)

    def getTdAddress(self):
        print(self.brokerNameComboBox)
        self.name = raw_input('请输入你的期货公司：')

        self.name=u'Z模拟'
        brokerID = self.nameDict[self.name]

        operatorText = raw_input('请选择您的网络运行商：电信，联通，移动')
        print operatorText
        if operatorText == u'电信':
            self.operator = 'telecom'
        elif operatorText == u'联通':
            self.operator = 'unicom'
        else:
            self.operator = 'netcom'

        for i in self.brokerDict[brokerID]['Servers'][self.operator]['trading']:
            self.tdAddressComboBox.append(i)
        print self.brokerDict[brokerID]['Servers'][self.operator]['trading']

if __name__=="__main__":
    NewAccountDialog()