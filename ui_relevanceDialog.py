# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relevanceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_relevanceDialog(object):
    def setupUi(self, relevanceDialog):
        relevanceDialog.setObjectName("relevanceDialog")
        relevanceDialog.resize(312, 244)
        self.verticalLayout = QtWidgets.QVBoxLayout(relevanceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(relevanceDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.relevanceMainComboBox = QtWidgets.QComboBox(relevanceDialog)
        self.relevanceMainComboBox.setObjectName("relevanceMainComboBox")
        self.gridLayout.addWidget(self.relevanceMainComboBox, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(relevanceDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.relevanceAgentComboBox = QtWidgets.QComboBox(relevanceDialog)
        self.relevanceAgentComboBox.setObjectName("relevanceAgentComboBox")
        self.gridLayout.addWidget(self.relevanceAgentComboBox, 3, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(relevanceDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.slipSpinBox = QtWidgets.QSpinBox(relevanceDialog)
        self.slipSpinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.slipSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.slipSpinBox.setPrefix("")
        self.slipSpinBox.setMinimum(1)
        self.slipSpinBox.setProperty("value", 3)
        self.slipSpinBox.setObjectName("slipSpinBox")
        self.gridLayout.addWidget(self.slipSpinBox, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(relevanceDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.multipleDoubleSpinBox = QtWidgets.QDoubleSpinBox(relevanceDialog)
        self.multipleDoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.multipleDoubleSpinBox.setMinimum(0.01)
        self.multipleDoubleSpinBox.setSingleStep(0.01)
        self.multipleDoubleSpinBox.setProperty("value", 1.0)
        self.multipleDoubleSpinBox.setObjectName("multipleDoubleSpinBox")
        self.gridLayout.addWidget(self.multipleDoubleSpinBox, 5, 1, 1, 1)
        self.oppositeCheckBox = QtWidgets.QCheckBox(relevanceDialog)
        self.oppositeCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.oppositeCheckBox.setObjectName("oppositeCheckBox")
        self.gridLayout.addWidget(self.oppositeCheckBox, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(relevanceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(relevanceDialog)
        self.buttonBox.accepted.connect(relevanceDialog.accept)
        self.buttonBox.rejected.connect(relevanceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(relevanceDialog)

    def retranslateUi(self, relevanceDialog):
        _translate = QtCore.QCoreApplication.translate
        relevanceDialog.setWindowTitle(_translate("relevanceDialog", "设置账户关联"))
        self.label.setText(_translate("relevanceDialog", "选择关联主账户："))
        self.label_2.setText(_translate("relevanceDialog", "选择关联子账户："))
        self.label_3.setText(_translate("relevanceDialog", "设置子帐号跟单滑点："))
        self.slipSpinBox.setSuffix(_translate("relevanceDialog", " 跳"))
        self.label_4.setText(_translate("relevanceDialog", "设置子帐号跟单倍数："))
        self.multipleDoubleSpinBox.setSuffix(_translate("relevanceDialog", "倍"))
        self.oppositeCheckBox.setText(_translate("relevanceDialog", "子帐号反向跟单"))

