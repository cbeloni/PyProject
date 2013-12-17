#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gi.repository import Gtk
import sys
import os

class Handler:
    def __init__(self):
        global entryUser
        global entryPass
        global entryEnder
        global entryPort
        try:
            ler = open('/etc/apt/apt.conf')
            linha = ler.readline()

            linha = linha[27:]
            loops = 0               
            coluna = 0

            for x in linha:
                loops += 1
                if x == '/':
                    coluna += 1
                if x == '/'  and coluna == 2:
                    usuarioIn = loops
                if x == ':' and coluna == 3:
                    portaIn = loops                
                if x == ':' and coluna != 3:
                    coluna += 1
                    senhaIn = loops
                if x == '@':
                    siteIn = loops
                if x == '/' and coluna >= 3:
                    portaFin = loops   

            entryUser.set_text(linha[usuarioIn:senhaIn-1])
            entryPass.set_text(linha[senhaIn:siteIn-1])
            entryEnder.set_text(linha[siteIn:portaIn-1])
            entryPort.set_text(linha[portaIn:portaFin-1])
        except:
            msg = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,'Arquivo de configuração não encontrado.')
            msg.run()
            msg.destroy()

    def on_delete_window(self, *args):
        Gtk.main_quit(*args)

    def on_botaoGravar_pressed(self, button):
        usuario = entryUser.get_text()	
        senha = entryPass.get_text()	
        ender = entryEnder.get_text()
        port = entryPort.get_text()
        #text = '''Acquire::http::proxy "http://%s:%s@proxy.sondait.com.br:3128/";\nAcquire::https::proxy "https://proxy.sondait.com.br:3128/";\nAcquire::ftp::proxy "ftp://proxy.sondait.com.br:3128/";\nAcquire::socks::proxy "socks://proxy.sondait.com.br:3128/";''' % usuario,senha
        text = '''Acquire::http::proxy "http://%s:%s@%s:%s/";
Acquire::https::proxy "https://%s:%s@%s:%s/";
Acquire::ftp::proxy "ftp://%s:%s@%s:%s/";
Acquire::socks::proxy "socks://%s:%s@%s:%s/";
        ''' % (usuario,senha,ender,port,usuario,senha,ender,port,usuario,senha,ender,port,usuario,senha,ender,port)
        #entryDois.set_text(text) 
        #f = open('/etc/apt/apt.conf', 'w')  
        try:      
            f = open('/etc/apt/apt.conf', 'w')        
            f.write(text)
            f.close()
        except:
            msg = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,'É necessário que o programa seja iniciado como root: sudo python autenticarProxy.py') 
            msg.run()
            msg.destroy()   
            sys.exit()
        #arquivo = file('/home/beloni/Documentos/Python/teste3.txt').read()     #linha funcionando                   		       
        msg = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,'Configuração realizada com sucesso.') 
        msg.run()
        msg.destroy()	
    def on_btnRemover_pressed(self, button):
        os.system("rm /etc/apt/apt.conf")

builder = Gtk.Builder()
builder.add_from_file("/opt/pAuthentication2/autenticarProxy.glade")

window = builder.get_object("window1")
entryUser = builder.get_object("entry1")
entryPass = builder.get_object("entry2")
entryEnder = builder.get_object("entry3")
entryPort = builder.get_object("entry4")
botaoGravarUm = builder.get_object("botaoGravar")
entryPass.set_visibility(False)
builder.connect_signals(Handler())
window.show_all()
Gtk.main()
