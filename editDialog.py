# encoding:UTF-8
import os,sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui_editDialog

class EditDialog(QDialog,ui_editDialog.Ui_editDialog):
	def __init__(self, slip,multiple,opposite,parent=None):
		super(EditDialog, self).__init__(parent)
		self.setupUi(self)
		self.passwordLineEdit.setEchoMode(2) #设置保密形式，看不见
		self.slipSpinBox.setValue(int(slip))
		self.doubleSpinBox.setValue(multiple)
		self.okPushButton.clicked.connect(self.editAccept)
		self.cancelPushButton.clicked.connect(self.reject)
		self.password=""
		
		self.oppositeFlag=False
		if opposite:
			self.oppositeCheckBox.setCheckState(2)
		else:
			self.oppositeCheckBox.setCheckState(0)

	def editAccept(self):
		text=self.passwordLineEdit.text()
		self.password=text
		self.slip=self.slipSpinBox.value()
		self.multiple=self.doubleSpinBox.value()

		if self.oppositeCheckBox.checkState()==2:
			self.oppositeFlag=True
		if self.oppositeCheckBox.checkState()==0:
			self.oppositeFlag=False
		if text == "":
			QMessageBox.warning(self,u"密码修改",u"密码为空，密码将不会修改。")
			self.accept()
		else:
			self.accept()


		
