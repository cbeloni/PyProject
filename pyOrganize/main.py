#!/usr/bin/env python
import sqlite3
from PySide import QtCore, QtGui, QtSql


class EditableSqlModel(QtSql.QSqlQueryModel):
    def flags(self, index):
        flags = super(EditableSqlModel, self).flags(index)

        if index.column() in (1, 2, 3):
            flags |= QtCore.Qt.ItemIsEditable

        return flags

    def setData(self, index, value, role):
        if index.column() not in (1, 2, 3):
            return False
        primaryKeyIndex = self.index(index.row(), 0)
        chamado = self.data(primaryKeyIndex)

        self.clear()

        if index.column() == 1:
            ok = self.setEmpresa(chamado, value)
        elif index.column() == 2:
            ok = self.setDataPrevista(chamado, value)
        elif index.column() == 3:
            ok = self.setDataAtual(chamado, value)
        self.refresh()
        return ok

    def refresh(self):
        self.setQuery('select chamado,empresa,data_prevista,data_atual from ordem_atendimento order by chamado')
        self.setHeaderData(0, QtCore.Qt.Horizontal, "CHAMADO")
        self.setHeaderData(1, QtCore.Qt.Horizontal, "EMPRESA")
        self.setHeaderData(2, QtCore.Qt.Horizontal, "DATA PREVISTA")
        self.setHeaderData(3, QtCore.Qt.Horizontal, "DATA ATUAL")

    def setEmpresa(self, chamado, empresa):
        query = QtSql.QSqlQuery()
        query.prepare('update ordem_atendimento set empresa = ? where chamado = ?')
        query.addBindValue(empresa)
        query.addBindValue(chamado)
        self.refresh()
        return query.exec_()

    def setDataPrevista(self, chamado, dataprevista):
        query = QtSql.QSqlQuery()
        query.prepare('update ordem_atendimento set data_prevista = ? where chamado = ?')
        query.addBindValue(dataprevista)
        query.addBindValue(chamado)

        self.refresh()
        return query.exec_()
    
    def setDataAtual(self, chamado, dataAtual):
        query = QtSql.QSqlQuery()
        query.prepare('update ordem_atendimento set data_atual = ? where chamado = ?')
        query.addBindValue(dataAtual)
        query.addBindValue(chamado)

        self.refresh()
        return query.exec_()
class FrmMenu(QtGui.QWidget):
    def __init__(self,title, model):
        super(FrmMenu, self).__init__()

        x, y, w, h = 300, 300, 725, 300
        self.setGeometry(x, y, w, h)


        hbox = QtGui.QGridLayout()

        self.table_view = QtGui.QTableView()
        self.table_view.setModel(model)

        self.table_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_selecao = self.table_view.selectionModel()
        self.table_selecao.selectionChanged.connect(printaMensagem)

        self.btn2 = QtGui.QPushButton('Priorizar', self)
        self.btn3 = QtGui.QPushButton('Postergar', self)

        hbox.addWidget(self.table_view, 0, 2, 4, 1)
        hbox.addWidget(self.btn2,0,1)
        #hbox.addWidget(self.btn3)
        hbox.addWidget(self.btn3,1,1)
        self.setLayout(hbox)

    def show_and_raise(self):
        self.show()
        self.raise_()

def abreConexao():
    ''' Abreconexao (nome do banco de dados sqlite)
    '''
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName('dados.db')
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                              "This example needs SQLite support. Please read "
                              "the Qt SQL driver documentation for information "
                              "how to build it.\n\nClick Cancel to exit."),
                QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)
        return False
    
    query = QtSql.QSqlQuery()
    return True

def printaMensagem():
    print ("Clicado")     
    for index in frm.table_view.selectionModel().selectedRows():
        print('Row %d is selected' % index.row())
        id = editableModel.data(index, 0)
        print (id)

def initializeModel(model):
    model.setQuery('select chamado,empresa,data_prevista,data_atual from ordem_atendimento order by chamado')
    model.setHeaderData(0, QtCore.Qt.Horizontal, "CHAMADO")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "EMPRESA")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "DATA PREVISTA")
    model.setHeaderData(3, QtCore.Qt.Horizontal, "DATA ATUAL")



if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    if not abreConexao():
        sys.exit(1)

    editableModel = EditableSqlModel()

    initializeModel(editableModel)
    frm = FrmMenu("Editable Query Model", editableModel)
    frm.btn2.clicked.connect(printaMensagem)
    frm.show()

    sys.exit(app.exec_())                