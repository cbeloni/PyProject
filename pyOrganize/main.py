#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sqlite3
from datetime import *
from PySide import QtCore, QtGui, QtSql

class EditableSqlModel(QtSql.QSqlQueryModel):
    def flags(self, index):
        flags = super(EditableSqlModel, self).flags(index)

        if index.column() in (1, 2):
            flags |= QtCore.Qt.ItemIsEditable

        return flags

    def setData(self, index, value, role):
        if index.column() not in (1, 2):
            return False
        primaryKeyIndex = self.index(index.row(), 0)
        chamado = self.data(primaryKeyIndex)

        self.clear()

        if index.column() == 1:
            ok = self.setEmpresa(chamado, value)
        elif index.column() == 2:
            ok = self.setTempoDesenvolvimento(chamado, value)
        self.refresh()
        return ok

    def refresh(self):
        self.setAtualizaData()

        self.setQuery('select chamado,empresa,tempo_desenvolvimento,data_prevista,data_atual,ordem from ordem_atendimento order by ordem')
        self.setHeaderData(0, QtCore.Qt.Horizontal, "CHAMADO")
        self.setHeaderData(1, QtCore.Qt.Horizontal, "EMPRESA")
        self.setHeaderData(2, QtCore.Qt.Horizontal, "TEMPO DEV.")
        self.setHeaderData(3, QtCore.Qt.Horizontal, "DATA PREV.")
        self.setHeaderData(4, QtCore.Qt.Horizontal, "DATA ATUAL")
        self.setHeaderData(4, QtCore.Qt.Horizontal, "ORDEM")

    def setEmpresa(self, chamado, empresa):
        query = QtSql.QSqlQuery()
        query.prepare('update ordem_atendimento set empresa = ? where chamado = ?')
        query.addBindValue(empresa)
        query.addBindValue(chamado)
        self.refresh()
        return query.exec_()

    def setTempoDesenvolvimento(self, chamado, tempoDesenvolvimento):
        query = QtSql.QSqlQuery()
        query.prepare('update ordem_atendimento set tempo_desenvolvimento = ? where chamado = ?')
        query.addBindValue(tempoDesenvolvimento)
        query.addBindValue(chamado)

        self.refresh()
        return query.exec_()

    def setAlteraOrdem (self, peso):
        cursor_count = QtSql.QSqlQuery("select count(*) from ordem_atendimento")    
        cursor_count.next()
        valor_cursor_count = str(cursor_count.value(0))

        for index in frm.table_view.selectionModel().selectedRows():
            indexRow = index.row()
            indexOrdem = self.index(index.row(), 5)          
            indexChamado = self.index(index.row(), 0)          

            dataOrdem = self.data(indexOrdem)
            dataChamado = self.data(indexChamado)
            print ("dataOrdem: " + str(dataOrdem)) 
            print ("dataChamado: " + str(dataChamado)) 
            print ("valor_cursor_count: " + str(valor_cursor_count)) 

        if dataOrdem == 1 and peso == -1:
            print ("Não é possível priorizar o primeiro atendimento")
            return
        elif str(dataOrdem) == valor_cursor_count and peso == 1:
            print ("Não é possível postergar o último atendimento")
            return          
        
        query = QtSql.QSqlQuery()
        query.prepare('update ordem_atendimento set ordem = ? where ordem = ?')
        query.addBindValue(dataOrdem)
        query.addBindValue(dataOrdem + peso)
        query.exec_()

        query.prepare('update ordem_atendimento set ordem = ? where chamado = ?')
        query.addBindValue(dataOrdem + peso)
        query.addBindValue(dataChamado)
        query.exec_()            

        self.refresh()

        frm.table_view.selectRow(indexRow + peso) 

    def setPriorizar (self):
        self.setAlteraOrdem(-1)      
    
    def setPostergar (self):
        self.setAlteraOrdem(1)

    def setDataPrevisao (self,tempo_de_desenvolvimento,data):
        #data = '28-10-2014 08:30'
        data_formatada = datetime.strptime(data, '%d-%m-%Y %H:%M')

        #tempo = 31
        tempo = int(tempo_de_desenvolvimento)

        print (tempo)

        horas = tempo % 8
        print ("horas: " + str(horas))

        dias = tempo / 8
        print ("dias: " + str(dias))

        data_days = data_formatada + timedelta(days = dias)
        data_final = data_days + timedelta(hours = horas)

        if data_final.hour >= 12:
            data_final = data_final + timedelta(hours = 1)

        #print (data_final.strftime('%d-%m-%Y %H:%M'))
        return data_final.strftime('%d-%m-%Y %H:%M')

    def setAtualizaData (self):
        vPrimerio = True
        q = QtSql.QSqlQuery("select * from ordem_atendimento order by ordem asc")
        rec = q.record()
        colChamado = rec.indexOf("chamado")
        colDataPrevista = rec.indexOf("data_prevista")
        colTempoDesenvolvimento = rec.indexOf("tempo_desenvolvimento")

        #print (self.setDataPrevisao(19,'28-10-2014 08:30'))
        while q.next():
            #print (q.value(colChamado))
            if vPrimerio:
                vPrimerio = False
                data_prevista = self.setDataPrevisao(q.value(colTempoDesenvolvimento),q.value(colDataPrevista))
            else:                
                query_date = QtSql.QSqlQuery()
                query_date.prepare('update ordem_atendimento set data_prevista = ? where chamado = ?')
                query_date.addBindValue(data_prevista)
                query_date.addBindValue(q.value(colChamado))

                query_date.exec_()

                data_prevista = self.setDataPrevisao(q.value(colTempoDesenvolvimento),data_prevista)

class FrmMenu(QtGui.QWidget):
    def __init__(self,title, model):
        super(FrmMenu, self).__init__()

        x, y, w, h = 300, 300, 725, 300
        self.setGeometry(x, y, w, h)


        hbox = QtGui.QGridLayout()

        self.table_view = QtGui.QTableView()
        self.table_view.setModel(model)
        self.table_view.setColumnHidden(5,True)
        self.table_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_view.resizeColumnsToContents()
        self.table_view.selectRow(0)
        # handle ao alterar seleção de row em table_view
        #self.table_selecao = self.table_view.selectionModel()                       
        #self.table_selecao.selectionChanged.connect(editableModel.setPriorizar) 

        self.btnPriorizar = QtGui.QPushButton('Priorizar', self)
        self.btnPostergar = QtGui.QPushButton('Postergar', self)
        self.btnInserir   = QtGui.QPushButton('Inserir', self)
        self.btnExcluir   = QtGui.QPushButton('Excluir', self)

        hbox.addWidget(self.table_view, 0, 2, 5, 1)
        hbox.addWidget(self.btnPriorizar,0,1)
        hbox.addWidget(self.btnPostergar,1,1)
        hbox.addWidget(self.btnInserir,2,1)
        hbox.addWidget(self.btnExcluir,3,1)

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
    model.setQuery('select chamado,empresa,tempo_desenvolvimento,data_prevista,data_atual,ordem from ordem_atendimento order by ordem')
    model.setHeaderData(0, QtCore.Qt.Horizontal, "CHAMADO")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "EMPRESA")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "TEMPO DEV.")
    model.setHeaderData(3, QtCore.Qt.Horizontal, "DATA PREV.")
    model.setHeaderData(4, QtCore.Qt.Horizontal, "DATA ATUAL")
    model.setHeaderData(5, QtCore.Qt.Horizontal, "ORDEM")

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    if not abreConexao():
        sys.exit(1)

    editableModel = EditableSqlModel()

    initializeModel(editableModel)
    frm = FrmMenu("Editable Query Model", editableModel)
    frm.btnPriorizar.clicked.connect(editableModel.setPriorizar)
    frm.btnPostergar.clicked.connect(editableModel.setPostergar)
    frm.show()

    sys.exit(app.exec_())                