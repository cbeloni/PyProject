#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import PyOrganizeGUI
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3

#Importar valores da base SQLite
def obterValores():
    conn = sqlite3.connect("chamados.db")
    cursor = conn.cursor()
    sql =  ''' SELECT * FROM orcamento '''
    resultado = cursor.execute(sql)
    return resultado

#classe main    
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = PyOrganizeGUI.Ui_Dialog()
        self.ui.setupUi(self)
        
        tablemodel = MyTableModel(list(obterValores()), self)
        self.ui.tableView.setModel(tablemodel)
        self.ui.BtAtualizar.clicked.connect(self.Atualizar)

    def Atualizar(self):
        tablemodel = MyTableModel(list(obterValores()), self)     
        #self.ui.setupUi(self,tablemodel)
        self.ui.tableView.setModel(tablemodel)
        print ('Atualizado')

# création du modèle
class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent = None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return (self.arraydata[index.row()][index.column()])

app = QtGui.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
