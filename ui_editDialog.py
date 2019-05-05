# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editDialog(object):
    def setupUi(self, editDialog):
        editDialog.setObjectName("editDialog")
        editDialog.resize(304, 192)
        self.verticalLayout = QtWidgets.QVBoxLayout(editDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(editDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.userIDLabel = QtWidgets.QLabel(editDialog)
        self.userIDLabel.setText("")
        self.userIDLabel.setObjectName("userIDLabel")
        self.gridLayout.addWidget(self.userIDLabel, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(editDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.passwordLineEdit = QtWidgets.QLineEdit(editDialog)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(editDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.slipSpinBox = QtWidgets.QSpinBox(editDialog)
        self.slipSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.slipSpinBox.setMinimum(1)
        self.slipSpinBox.setProperty("value", 3)
        self.slipSpinBox.setObjectName("slipSpinBox")
        self.gridLayout.addWidget(self.slipSpinBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(editDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(editDialog)
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setPrefix("")
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setSingleStep(1.0)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 3, 1, 1, 1)
        self.oppositeCheckBox = QtWidgets.QCheckBox(editDialog)
        self.oppositeCheckBox.setObjectName("oppositeCheckBox")
        self.gridLayout.addWidget(self.oppositeCheckBox, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.okPushButton = QtWidgets.QPushButton(editDialog)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(editDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(editDialog)
        QtCore.QMetaObject.connectSlotsByName(editDialog)

    def retranslateUi(self, editDialog):
        _translate = QtCore.QCoreApplication.translate
        editDialog.setWindowTitle(_translate("editDialog", "账户信息修改"))
        self.label.setText(_translate("editDialog", "用户名："))
        self.label_2.setText(_translate("editDialog", "密码(CTP)："))
        self.label_3.setText(_translate("editDialog", "账号跟单滑点："))
        self.slipSpinBox.setSuffix(_translate("editDialog", " 跳"))
        self.label_4.setText(_translate("editDialog", "账号跟单倍数："))
        self.doubleSpinBox.setSuffix(_translate("editDialog", "倍"))
        self.oppositeCheckBox.setText(_translate("editDialog", "子帐号反向跟单"))
        self.okPushButton.setText(_translate("editDialog", "OK"))
        self.cancelPushButton.setText(_translate("editDialog", "Cancel"))

