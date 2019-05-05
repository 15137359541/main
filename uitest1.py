# encoding:UTF-8
import shelve, os
import platform
import sys
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from time import sleep
import qrc_resources
from newAccountDialog import NewAccountDialog
from relevanceDialog import RelevanceDialog
from editDialog import EditDialog
from phCTP import MainCtp, AgentCtp, EventPush
from phFunction import *
from phObject import *

from vnpy.event import EventEngine, Event
import ui_mainfollow
from tt1 import mxhMysql

__version__ = "1.0.0"

EVENT_TIMER = 'eTimer'


class Form(QMainWindow, ui_mainfollow.Ui_MainWindow):
    """docstring for Form"""

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setupUi(self)

        self.ee = EventEngine()
        self.ee.start()
        self.eventPush = EventPush(self.ee)

        self.dirty = False
        mxh_a, mxh_b = self.getAccounts()

        self.mainCTPList = []
        self.agentCTPList = []

        self.mainShowCtp = ShowCtp()
        self.agentShowCtp = ShowCtp()

        self.ee.register(u"addListWidget", self.addListWidget)

        self.ee.register(u"addLog", self.addLog)

        self.ee.register(u"addTable", self.updateTable)

        self.mainFreshPushButton.clicked.connect(self.qryMainPositionDetail)
        # self.agentFreshPushButton.clicked.connect(self.qryAgentPositionDetail)

        self.setupCTP(self.ee)
        self.newAgentCtp = None
        self.newMainCtp = None

        self.editItem = EditTreeItem()
        self.filemenu = self.menuBar().addMenu(u"&菜单")
        self.editmenu = self.menuBar().addMenu(u"账户设置")
        fileToolbar = self.addToolBar("file")
        editToolbar = self.addToolBar("edit")
        self.startAction = self.createAction(u"启动", self.start, icon="start",
                                             tip=u"启动连接账号")
        self.stopAction = self.createAction(u"停止", self.stop, icon="stop",
                                            tip=u"断开账户连接")
        newAction = self.createAction(u"新建", self.new, icon="add",
                                      tip=u"新建账户")
        # self.modifyAction = self.createAction(u"账户修改", self.modify, icon="modify",
        #                                       tip=u"修改账户信息")
        self.delAction = self.createAction(u"删除账户", self.delete, icon="delete",
                                           tip=u"删除选中的账户")
        # self.relevanceAction = self.createAction(u"关联账户", self.relevance,
        #                                          icon="relevance", tip=u"关联主账户与子账户")
        startAllAction = self.createAction(u"全部启动", self.startAll,
                                           tip=u"启动全部账号")
        stopAllAction = self.createAction(u"全部停止", self.stopAll,
                                          tip=u"断开全部账号")
        exitAction = self.createAction(u"退出", self.closeEvent,
                                       tip=u"退出系统")

        self.saveAction = self.createAction(u"保存", self.save, icon="save",
                                            tip=u"保存账号信息")
        fileActions = (self.startAction, self.stopAction, None,
                       startAllAction, stopAllAction, None, exitAction)
        editActions = (newAction, self.saveAction, self.delAction, None)
        self.addActions(self.filemenu, fileActions)
        self.addActions(self.editmenu, editActions)
        self.addActions(fileToolbar, (self.startAction, self.stopAction))
        self.addActions(editToolbar, editActions)
        self.setWindowTitle(u"期货系统")

        self.updateUi()
        self.initComboBox()

        self.updateTree()

        self.setWindowIcon(QIcon(":/logo.png"))

        self.statusLabelCompany = QLabel(u"杭州易期智能科技有限公司")
        self.statusLabelTel = QLabel(u"Tel:0571-86493200")
        self.statusBar().addPermanentWidget(self.statusLabelCompany)
        self.statusBar().addPermanentWidget(self.statusLabelTel)

        self.accountTreeWidget.itemClicked.connect(self.getEditItem)
        # 初始化时，什么也没做
        self.mainAccountComboBox.currentIndexChanged.connect(self.updateMainComboBox)
        # self.agentAccountComboBox.currentIndexChanged.connect(self.updateAgentComboBox)

        # 设置输出信息
        self.setupTable(self.mainAccountTable)
        # self.setupTable(self.agentAccountTable)

        # 初始化订阅列表
        self.subscribeSetup()

    def subscribeSetup(self):

        res = mxhMysql().getSubscribes()
        for i in self.mainAccountList:
            for j in res:
                if j[0] in i.subscribes:
                    i.subscribes.append(j)

        for i in self.mainAccountList:
            for j in self.mainCTPList:
                if j.userID ==i.userID:
                    j.subscribeList=i.subscribes

    def subscribeApi(self, subscribeObj, mainuserID):
        for i in self.mainAccountList:
            if i.userID == mainuserID:
                print('jinru')
                for sub in i.subscribes:
                    if subscribeObj.channel_id == sub.channel_id:
                        print('have subscript')
                        break
                    else:
                        pass
                else:
                    print('start subscribe...')
                    i.subscribes.append(subscribeObj)
                    self.save()
                    # ctp列表中订阅
                    for j in self.mainCTPList:
                        if j.userID == i.userID:
                            j.subscribeList.append(subscribeObj)


            else:
                print('没有此操盘手：%s' % mainuserID)
        return self.mainAccountList

    def unsubscribeApi(self, subscribeObj, mainuserID):
        for i in self.mainAccountList:
            if i.userID == mainuserID:
                print('jinru')
                for sub in i.subscribes:
                    if subscribeObj.channel_id == sub.channel_id:
                        print('delect subscribe')
                        i.subscribes.remove(sub)
                        self.save()
                        # ctp列表中删除订阅
                        for j in self.mainCTPList:
                            if j.userID == i.userID:
                                for each in j.subscribeList:
                                    if each.channel_id == subscribeObj.channel_id:
                                        j.subscribeList.remove(each)
                        break
                    else:
                        pass
                else:
                    print('You have not subscribed ')

        return self.mainAccountList

    # 设置输出框的格式
    def setupTable(self, target):
        target.setSortingEnabled(False)

        target.setColumnCount(6)
        headers = [u"持仓合约", u'买卖', u'手数', u'开仓价',
                   u'开仓时间', u"持仓盈亏"]
        target.setHorizontalHeaderLabels(headers)
        target.setEditTriggers(target.NoEditTriggers)
        target.setAlternatingRowColors(True)

    def updateTable(self, event):

        data = event.dict_['data']
        rowCount = len(data)
        print u'持仓信息'
        print '就是这里'

        def setItem(target, data):

            target.clearContents()

            for i, v in enumerate(data):
                print('chi cang xin xi is:')
                print i,v
                if i == 0:
                    continue
                item = QTableWidgetItem("%s" % v['InstrumentID'])
                target.setItem(i - 1, 0, item)
                if v['Direction'] == "0":
                    item = QTableWidgetItem(u"买")
                    item.setForeground(QColor('red'))
                else:
                    item = QTableWidgetItem(u"卖")
                    item.setForeground(QColor('green'))
                target.setItem(i - 1, 1, item)
                item = QTableWidgetItem("%s" % safeUnicode(v['Volume']))
                target.setItem(i - 1, 2, item)
                item = QTableWidgetItem("%s" % safeUnicode(v['OpenPrice']))
                target.setItem(i - 1, 3, item)
                item = QTableWidgetItem("%s" % safeUnicode(v['OpenDate']))
                target.setItem(i - 1, 4, item)
                item = QTableWidgetItem("%s" % safeUnicode(v['PositionProfitByDate']))
                if v['PositionProfitByDate'] < 0:
                    item.setBackground(QColor("green"))
                    item.setForeground(QColor("white"))
                elif v['PositionProfitByDate'] > 0:
                    item.setBackground(QColor("red"))
                    item.setForeground(QColor("white"))
                target.setItem(i - 1, 5, item)

        if data[0] and rowCount != 0:

            self.mainAccountTable.setRowCount(rowCount - 1)
            setItem(self.mainAccountTable, data)
        else:
            pass


    def getEditItem(self):
        currentItem = self.accountTreeWidget.currentItem()
        parentItem = currentItem.parent()

        topIndex = self.accountTreeWidget.indexOfTopLevelItem(parentItem)

        if topIndex == 0:
            k, ctp, accountIndex, account = getCTPFromTree(currentItem.text(0),
                                                           currentItem.text(2), self.mainCTPList, self.mainAccountList)
            self.editItem.index = k
            self.editItem.ctp = ctp
            self.editItem.flag = True
            self.editItem.isNone = False
            self.editItem.accountIndex = accountIndex
            self.editItem.account = account

        elif topIndex == 1:
            k, ctp, accountIndex, account = getCTPFromTree(currentItem.text(0),
                                                           currentItem.text(2), self.agentCTPList,
                                                           self.agentAccountList)
            self.editItem.index = k
            self.editItem.ctp = ctp
            self.editItem.flag = False
            self.editItem.isNone = False
            self.editItem.accountIndex = accountIndex
            self.editItem.account = account
        else:
            self.editItem = EditTreeItem()

        self.updateUi()

    def updateTree(self):

        self.accountTreeWidget.clear()
        self.accountTreeWidget.setColumnCount(3)
        self.accountTreeWidget.setHeaderLabels([u'账号信息', u'连接状态', u'期货公司'])
        self.rootMain = QTreeWidgetItem(self.accountTreeWidget)
        self.rootMain.setText(0, u"主账号:")

        # self.rootAgent = QTreeWidgetItem(self.accountTreeWidget)
        # self.rootAgent.setText(0, u"子账号:")

        self.accountTreeWidget.expandItem(self.rootMain)
        # self.accountTreeWidget.expandItem(self.rootAgent)

        for i in self.mainCTPList:
            mainCtp = QTreeWidgetItem(self.rootMain)
            mainCtp.setText(0, i.userID)
            if i.loginStatus:
                mainCtp.setText(1, u"ON")
            else:
                mainCtp.setText(1, u"OFF")
            mainCtp.setText(2, i.company)
            # print i.childList

            if len(i.childList) > 0:
                for k, j in enumerate(i.childList):
                    childCtp = QTreeWidgetItem(mainCtp)
                    childCtp.setText(0, u"%s:" % (k + 1) + unicode(j.userID))
                    if j.connectionStatus:
                        childCtp.setText(1, u"ON")
                    else:
                        childCtp.setText(1, u"OFF")
                    childCtp.setText(2, j.company)

        # for i in self.agentCTPList:
        #     agentCtp = QTreeWidgetItem(self.rootAgent)
        #     agentCtp.setText(0, i.userID)
        #     if i.connectionStatus:
        #         agentCtp.setText(1, u"ON")
        #     else:
        #         agentCtp.setText(1, u"OFF")
        #     agentCtp.setText(2, i.company)

    def getAccounts(self):

        # filename = os.getcwd() + r"\\accounts.ph"
        # self.mainAccountList, self.agentAccountList = getAccounts(filename)
        # return self.mainAccountList, self.agentAccountList


        self.mainAccountList = mxhMysql().getAccount()
        self.agentAccountList =[]
        return self.mainAccountList, self.agentAccountList

    def setupCTP(self, eventEngine):
        self.mainCTPList = []
        self.agentCTPList = []

        for i in self.agentAccountList:
            print('i is ', i)
            self.agentCTPList.append(setupAgentCTP(i, eventEngine))
        for i in self.mainAccountList:
            print('mainaccountlist_i is ', i)
            self.mainCTPList.append(setupMainCTP(i, eventEngine))

        for i in self.mainAccountList:
            if len(i.childs) > 0:
                mainCtp = getCTP(i, self.mainCTPList)
                for j in i.childs:
                    agentCtp = getCTP(j, self.agentCTPList)
                    mainCtp.childList.append(agentCtp)
                    agentCtp.father = mainCtp

    def updateCTP(self):
        if self.newMainCtp is not None:
            self.mainCTPList.append(self.newMainCtp)
        if self.newAgentCtp is not None:
            self.agentCTPList.append(self.newAgentCtp)
        self.newMainCtp = None
        self.newAgentCtp = None

    # 账号启动连接
    def start(self):
        if self.editItem.flag:
            self.editItem.ctp.connect()
        else:
            if self.editItem.ctp.father is not None:
                self.editItem.ctp.connect()
            else:
                QMessageBox.warning(self, u"账号启动", u"启动前请先关联主账号。")

        sleep(1)
        self.updateUi()
        self.updateTree()

    def stop(self):
        self.editItem.ctp.close()
        # sleep(1)
        now = datetime.now()

        if self.editItem.flag:
            flag = u"主帐号"
        else:
            flag = u"子帐号"
        msg = " ".join((now.strftime('%Y-%m-%d %H:%M:%S'),
                        flag, self.editItem.ctp.company,
                        self.editItem.ctp.userID, u"已经断开连接"))
        self.logListWidget.insertItem(0, QListWidgetItem(msg))
        self.updateUi()
        self.updateTree()

    def startAll(self):
        for i in self.mainCTPList:
            i.connect()
        for i in self.agentCTPList:
            if i.father is not None:
                i.connect()
            else:
                QMessageBox.warning(self, u"账号启动", u"启动前请先关联主账号。")
        sleep(1)
        self.updateTree()

    def stopAll(self):
        for i in self.mainCTPList:
            if i.loginStatus:
                i.close()
        for i in self.agentCTPList:
            if i.loginStatus:
                i.close()
        self.updateTree()
        now = datetime.now()
        msg = " ".join((now.strftime('%Y-%m-%d %H:%M:%S'), u"账号已经全部断开连接"))
        self.logListWidget.insertItem(0, QListWidgetItem(msg))

    def save(self):
        if self.dirty:
            sqlAccountAll =mxhMysql().getAccount()
            for i in self.mainAccountList:
                for j in sqlAccountAll:
                    if i.userID == j.userID:
                        # self.eventPush.addListWidget('用户_%s 已存在添加%s' % (i.userID,j.userID))
                        break
                else:

                    print('保存数据到数据库')
                    # print(i.userID,i.password,i.brokerID,i.company,i.operator,i.tdAddress,i.mdAddress,i.mainFlag,i.strike,i.accountID,' '.join(i.subscribes),' '.join(i.mysqlChilds),' '.join(i.mysqlFather))
                    mxhMysql().insert(i.userID,i.password,i.brokerID,i.company,i.operator,i.tdAddress,i.mdAddress,i.mainFlag,i.strike,i.accountID,' '.join(i.subscribes),' '.join(i.mysqlChilds),' '.join(i.mysqlFather))
                    self.eventPush.addListWidget('新用户_%s 已添加' % i.userID)

            self.dirty = False
        self.updateUi()

    def new(self):
        self.newDialog = NewAccountDialog(self)
        if self.newDialog.exec_():
            newAccount = self.newDialog.newAccount
            if newAccount.mainFlag:
                self.mainAccountList.append(newAccount)
                self.newMainCtp = setupMainCTP(newAccount, self.ee)
            else:
                # self.agentAccountList.append(newAccount)
                # self.newAgentCtp = setupAgentCTP(newAccount, self.ee)
                pass
        else:
            return
        
        self.updateCTP()
        self.dirty = True
        self.updateUi()
        self.updateTree()
        self.initComboBox()

    def updateUi(self):
        if self.dirty:
            self.saveAction.setEnabled(True)
        else:
            self.saveAction.setEnabled(False)

        if self.editItem.isNone:
            self.stopAction.setEnabled(False)
            # self.relevanceAction.setEnabled(False)
            self.startAction.setEnabled(False)
            # self.modifyAction.setEnabled(False)
            self.delAction.setEnabled(False)
        else:
            if self.editItem.ctp.connectionStatus:
                self.stopAction.setEnabled(True)
                self.startAction.setEnabled(False)
            else:
                self.stopAction.setEnabled(False)
                self.startAction.setEnabled(True)
            # self.modifyAction.setEnabled(True)
            # self.relevanceAction.setEnabled(True)
            self.delAction.setEnabled(True)

        if self.editItem.isNone:
            self.startAction.setEnabled(False)
            self.stopAction.setEnabled(False)
        else:
            if self.editItem.ctp.connectionStatus:
                self.startAction.setEnabled(False)
                self.stopAction.setEnabled(True)
            else:
                self.startAction.setEnabled(True)
                self.stopAction.setEnabled(False)

    def initComboBox(self):
        self.mainAccountComboBox.clear()
        # self.agentAccountComboBox.clear()

        for i in self.mainAccountList:
            msg = u"brokerID:" + unicode(i.brokerID) + u" 账号:" + unicode(i.userID)
            self.mainAccountComboBox.addItem(msg)
        # for j in self.agentAccountList:
        #     msg = u"brokerID:" + unicode(j.brokerID) + u" 账号:" + unicode(j.userID)
        #     self.agentAccountComboBox.addItem(msg)

        self.updateMainComboBox()
        # self.updateAgentComboBox()

    def updateMainComboBox(self):
        try:
            msg = self.mainAccountComboBox.currentText()
            msg = msg.split(" ")
            brokerID = msg[0].split(":")[1]
            userID = msg[1].split(":")[1]

            k, ctp = getCTPFromBrokerID(brokerID, userID, self.mainCTPList)
            self.mainShowCtp.index = k
            self.mainShowCtp.ctp = ctp
            self.mainShowCtp.isNone = False

            self.mainCompanyLabel.setText(ctp.company)
            self.mainOperatorLabel.setText(ctp.operator)
            self.mainTdAddressLabel.setText(ctp.address)
        except IndexError:
            pass

    def updateAgentComboBox(self):
        try:
            msg = self.agentAccountComboBox.currentText()
            msg = msg.split(" ")
            brokerID = msg[0].split(":")[1]
            userID = msg[1].split(":")[1]

            k, ctp = getCTPFromBrokerID(brokerID, userID, self.agentCTPList)
            self.agentShowCtp.id = k
            self.agentShowCtp.ctp = ctp
            self.agentShowCtp.isNone = False

            self.agentCompanyLabel.setText(ctp.company)
            self.agentOperatorLabel.setText(ctp.operator)
            self.agentTdAddressLabel.setText(ctp.address)
        except IndexError:
            pass

    def qryMainPositionDetail(self, event):

        if not self.mainShowCtp.isNone and self.mainShowCtp.ctp.loginStatus:

            self.mainShowCtp.ctp.qryInvestorPositionDetail()

        else:
            # pass
            self.mainAccountTable.clearContents()
    def qryAgentPositionDetail(self, event):
        if not self.agentShowCtp.isNone and self.agentShowCtp.ctp.loginStatus:
            sleep(0.2)
            self.agentShowCtp.ctp.qryInvestorPositionDetail()
        else:
            pass

    def modify(self):
        if self.editItem.isNone:
            QMessageBox.warning(self, u"密码修改", u"请选择账号。")
            return

        self.editDialog = EditDialog(self.editItem.ctp.strike, self.editItem.ctp.multiple, self.editItem.ctp.opposite,
                                     self)
        self.editDialog.userIDLabel.setText(self.editItem.ctp.userID)
        if self.editDialog.exec_():
            password = self.editDialog.password
            multiple = self.editDialog.multiple
            strike = self.editDialog.slip
            oppositeFlag = self.editDialog.oppositeFlag
            if password != "":
                self.editItem.ctp.password = password
                self.editItem.account.password = password
            self.editItem.ctp.strike = strike
            self.editItem.ctp.multiple = multiple
            self.editItem.ctp.opposite = oppositeFlag
            self.dirty = True
            self.updateUi()
            print self.editItem.ctp.opposite
            print '是什么？'

        else:
            return

    def delete(self):
        msg = " ".join(("确定删除", self.editItem.ctp.company,
                        "账户:", self.editItem.ctp.userID, "?"))
        reply = QMessageBox.question(self, u"账户删除", msg,
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:

            if self.editItem.flag:
                self.mainAccountList.pop(self.editItem.accountIndex)
                self.mainCTPList.pop(self.editItem.index)
                for i in self.agentCTPList:
                    if self.editItem.ctp == i.father:
                        i.father = None
                for i in self.agentAccountList:
                    if self.editItem.account == i.father:
                        i.father = None
                sqlAccountAll = mxhMysql().getAccount()
                for j in sqlAccountAll:
                    for i in self.mainAccountList:

                        if i.userID == j.userID:
                            break
                    else:
                        mxhMysql().deleteAccount(j.userID)
                        print('删除数据')
                        self.eventPush.addListWidget('用户_%s 已删除' % j.userID)


            else:
                if self.editItem.ctp.father is not None:
                    for k, i in enumerate(self.editItem.ctp.father.childList):
                        if self.editItem.ctp is i:
                            self.editItem.ctp.father.childList.pop(k)

                    for k, i in enumerate(self.editItem.account.father.childs):
                        if self.editItem.account.userID == i.userID \
                                and self.editItem.account.brokerID == i.brokerID:
                            self.editItem.account.father.childs.pop(k)

                self.agentAccountList.pop(self.editItem.accountIndex)
                self.agentCTPList.pop(self.editItem.index)

            self.editItem = EditTreeItem()
            self.dirty = True
            self.updateTree()

            self.updateUi()
            self.initComboBox()
        else:
            return

    def relevance(self):
        self.relevanceDialog = RelevanceDialog(self, self.mainAccountList,
                                               self.agentAccountList)

        mainAccount = None
        agentAccount = None
        strike = 3

        if self.relevanceDialog.exec_():
            mainAccount = self.relevanceDialog.mainAccount
            agentAccount = self.relevanceDialog.agentAccount
            strike = self.relevanceDialog.strike
            multiple = self.relevanceDialog.multiple

            oppositeFlag = self.relevanceDialog.oppositeFlag

        if mainAccount is not None and agentAccount is not None:

            mainCtp = getCTP(mainAccount, self.mainCTPList)
            agentCtp = getCTP(agentAccount, self.agentCTPList)
            agentCtp.strike = strike
            agentCtp.multiple = multiple

            agentCtp.opposite = oppositeFlag
            print agentCtp.opposite
            print 'guan lian'
            for i in mainCtp.childList:
                print('guanlianxinxihanshu:', i)
                if agentCtp is i:
                    QMessageBox.warning(self, u"关联信息已存在",
                                        " ".join((u"子账户", agentCtp.company,
                                                  agentCtp.userID, u"已经关联到主账户",
                                                  mainCtp.company, mainCtp.userID,
                                                  u"中，请勿重复关联！")))
                    return

            mainAccount.childs.append(agentAccount)
            agentAccount.father = mainAccount
            mainCtp.childList.append(agentCtp)
            agentCtp.father = mainCtp
            self.dirty = True
            self.updateTree()
        return

    def closeEvent(self, event):
        reply = QMessageBox.question(self, u"退出", u"确认退出系统？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.dirty:
                saveReply = QMessageBox.question(self, u"保存",
                                                 u"账号信息有变动，是否保存？",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if saveReply == QMessageBox.Yes:
                    self.save()
            self.stopAll()
            self.ee.stop()



            event.accept()
        else:
            event.ignore()

    def createAction(self, text, slot=None, shortcut=None,
                     icon=None, tip=None, checkable=False,
                     signal="triggered"):
        action = QAction(text, self)

        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            if signal == "triggered":
                action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def getPrice(self):
        pass

    def addListWidget(self, event):
        now = datetime.now()
        msg = " ".join((now.strftime('%Y-%m-%d %H:%M:%S'),
                        event.dict_['data']))

        self.logListWidget.insertItem(0, QListWidgetItem(msg))
        print('print meg is', QListWidgetItem(msg))

    def addLog(self, event):
        print event.dict_['data']
        print '数据嘛？'


if 'Windows' in platform.uname():
    import ctypes

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('ph')

app = QApplication(sys.argv)

t = Form()
t.show()
app.exec_()
