# encoding:UTF-8

class RelevanceDialog():
    def __init__(self,parent=None,mainlist=None,agentlist=None):
        self.mainlist = mainlist
        self.agentlist = agentlist
        self.strike = 3
        self.relevanceMainComboBox = []
        self.relevanceAgentComboBox=[]
        if self.mainlist is not None:
            for i in self.mainlist:
                msg=''.join((u'期货公司： ',i.company,u'账号：',i.userID))
                self.relevanceMainComboBox.append(unicode(msg))
        if self.agentlist is not None:
            for i in self.agentlist:
                msg = "".join(("期货公司：", i.company, " 账号：", i.userID))
                self.relevanceAgentComboBox.append(unicode(msg))

        xiugai = input('是否确定修改账户；1 确定修改，2 取消修改')
        if xiugai ==1:
            if self.mainlist:
                self.mainAccount = self.mainlist[0]
            else:
                print('没有主账户')
            if self.agentlist:
                self.agentAccount = self.agentlist[0]
            else:
                print('没有关联账户')
            self.multiple =1

            fanxiangcaozuo = input('是否反向跟单 1，是 2 否')
            if fanxiangcaozuo==1:
                self.oppositeFlag=True
            else:
                self.oppositeFlag = False
        else:
            print('退出修改账户界面')

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
    mainlist.userID = '118336'
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
    res = []
    res.append(mainlist)

    f = RelevanceDialog(mainlist=res, agentlist=None)
