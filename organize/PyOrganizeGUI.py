# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyOrganizeGUI.ui'
#
# Created: Fri Jan 17 22:30:25 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 621, 421))
        #self.tableView.setModel(tableModelo) #incluído
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.BtAtualizar = QtGui.QPushButton(Dialog)
        self.BtAtualizar.setGeometry(QtCore.QRect(520, 440, 96, 27))
        self.BtAtualizar.setObjectName(_fromUtf8("BtAtualizar"))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Lista de Chamados", None))
        self.BtAtualizar.setText(_translate("Dialog", "Atualizar!", None))

