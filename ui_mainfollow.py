# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainfollow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 828)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 1, 1, 1)
        self.accountTreeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountTreeWidget.sizePolicy().hasHeightForWidth())
        self.accountTreeWidget.setSizePolicy(sizePolicy)
        self.accountTreeWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.accountTreeWidget.setAutoScroll(True)
        self.accountTreeWidget.setAutoScrollMargin(15)
        self.accountTreeWidget.setItemsExpandable(True)
        self.accountTreeWidget.setColumnCount(3)
        self.accountTreeWidget.setObjectName("accountTreeWidget")
        self.accountTreeWidget.headerItem().setText(0, "1")
        self.accountTreeWidget.headerItem().setText(1, "2")
        self.accountTreeWidget.headerItem().setText(2, "3")
        self.accountTreeWidget.header().setDefaultSectionSize(100)
        self.accountTreeWidget.header().setMinimumSectionSize(30)
        self.gridLayout_3.addWidget(self.accountTreeWidget, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.mainAccountComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainAccountComboBox.sizePolicy().hasHeightForWidth())
        self.mainAccountComboBox.setSizePolicy(sizePolicy)
        self.mainAccountComboBox.setObjectName("mainAccountComboBox")
        self.gridLayout_2.addWidget(self.mainAccountComboBox, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.mainCompanyLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainCompanyLabel.setText("")
        self.mainCompanyLabel.setObjectName("mainCompanyLabel")
        self.gridLayout_2.addWidget(self.mainCompanyLabel, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.mainOperatorLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainOperatorLabel.setText("")
        self.mainOperatorLabel.setObjectName("mainOperatorLabel")
        self.gridLayout_2.addWidget(self.mainOperatorLabel, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.mainTdAddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainTdAddressLabel.setText("")
        self.mainTdAddressLabel.setObjectName("mainTdAddressLabel")
        self.gridLayout_2.addWidget(self.mainTdAddressLabel, 3, 1, 1, 1)
        self.mainFreshPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainFreshPushButton.setObjectName("mainFreshPushButton")
        self.gridLayout_2.addWidget(self.mainFreshPushButton, 3, 2, 1, 1)
        self.mainAccountTable = QtWidgets.QTableWidget(self.centralwidget)
        self.mainAccountTable.setObjectName("mainAccountTable")
        self.mainAccountTable.setColumnCount(0)
        self.mainAccountTable.setRowCount(0)
        self.gridLayout_2.addWidget(self.mainAccountTable, 4, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        # self.agentAccountComboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.agentAccountComboBox.sizePolicy().hasHeightForWidth())
        # self.agentAccountComboBox.setSizePolicy(sizePolicy)
        # self.agentAccountComboBox.setObjectName("agentAccountComboBox")
        # self.gridLayout.addWidget(self.agentAccountComboBox, 0, 1, 1, 1)
        # self.label_9 = QtWidgets.QLabel(self.centralwidget)
        # self.label_9.setObjectName("label_9")
        # self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        # self.agentCompanyLabel = QtWidgets.QLabel(self.centralwidget)
        # self.agentCompanyLabel.setText("")
        # self.agentCompanyLabel.setObjectName("agentCompanyLabel")
        # self.gridLayout.addWidget(self.agentCompanyLabel, 1, 1, 1, 1)
        # self.label_8 = QtWidgets.QLabel(self.centralwidget)
        # self.label_8.setObjectName("label_8")
        # self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        # self.agentOperatorLabel = QtWidgets.QLabel(self.centralwidget)
        # self.agentOperatorLabel.setText("")
        # self.agentOperatorLabel.setObjectName("agentOperatorLabel")
        # self.gridLayout.addWidget(self.agentOperatorLabel, 2, 1, 1, 1)
        # self.label_7 = QtWidgets.QLabel(self.centralwidget)
        # self.label_7.setObjectName("label_7")
        # self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        # self.agentTdAddressLabel = QtWidgets.QLabel(self.centralwidget)
        # self.agentTdAddressLabel.setText("")
        # self.agentTdAddressLabel.setObjectName("agentTdAddressLabel")
        # self.gridLayout.addWidget(self.agentTdAddressLabel, 3, 1, 1, 1)
        # self.agentFreshPushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.agentFreshPushButton.setObjectName("agentFreshPushButton")
        # self.gridLayout.addWidget(self.agentFreshPushButton, 3, 2, 1, 1)
        # self.agentAccountTable = QtWidgets.QTableWidget(self.centralwidget)
        # self.agentAccountTable.setObjectName("agentAccountTable")
        # self.agentAccountTable.setColumnCount(0)
        # self.agentAccountTable.setRowCount(0)
        # self.gridLayout.addWidget(self.agentAccountTable, 4, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.logListWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logListWidget.sizePolicy().hasHeightForWidth())
        self.logListWidget.setSizePolicy(sizePolicy)
        self.logListWidget.setObjectName("logListWidget")
        self.verticalLayout.addWidget(self.logListWidget)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1576, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "账户列表："))
        self.label_10.setText(_translate("MainWindow", "账户信息："))
        self.label_2.setText(_translate("MainWindow", "主帐号："))
        self.label_4.setText(_translate("MainWindow", "开户公司："))
        self.label_5.setText(_translate("MainWindow", "运营商："))
        self.label_6.setText(_translate("MainWindow", "服务器地址："))
        self.mainFreshPushButton.setText(_translate("MainWindow", "刷新持仓信息"))
        # self.label_3.setText(_translate("MainWindow", "子帐号："))
        # self.label_9.setText(_translate("MainWindow", "开户公司："))
        # self.label_8.setText(_translate("MainWindow", "运营商："))
        # self.label_7.setText(_translate("MainWindow", "服务器地址："))
        # self.agentFreshPushButton.setText(_translate("MainWindow", "刷新持仓信息"))

