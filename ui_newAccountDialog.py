# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newAccountDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(298, 220)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.userIDLineEdit = QtWidgets.QLineEdit(Dialog)
        self.userIDLineEdit.setObjectName("userIDLineEdit")
        self.gridLayout.addWidget(self.userIDLineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.passwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.brokerNameComboBox = QtWidgets.QComboBox(Dialog)
        self.brokerNameComboBox.setObjectName("brokerNameComboBox")
        self.gridLayout.addWidget(self.brokerNameComboBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.operatorComboBox = QtWidgets.QComboBox(Dialog)
        self.operatorComboBox.setObjectName("operatorComboBox")
        self.gridLayout.addWidget(self.operatorComboBox, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.tdAddressComboBox = QtWidgets.QComboBox(Dialog)
        self.tdAddressComboBox.setObjectName("tdAddressComboBox")
        self.gridLayout.addWidget(self.tdAddressComboBox, 4, 1, 1, 1)
        # self.accountCheckBox = QtWidgets.QCheckBox(Dialog)
        # self.accountCheckBox.setObjectName("accountCheckBox")
        # self.gridLayout.addWidget(self.accountCheckBox, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加账户"))
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_2.setText(_translate("Dialog", "密码（CTP）："))
        self.label_3.setText(_translate("Dialog", "期货公司："))
        self.label_4.setText(_translate("Dialog", "网络运营商："))
        self.label_5.setText(_translate("Dialog", "交易服务器："))
        # self.accountCheckBox.setText(_translate("Dialog", "主账号标志"))

