#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#import tkMessageBox
import re
import os
import pdb
from comandosSql import *

# Verifica diretório
vDirAlpha = "~/Documentos/PyProjects/MontaPycoteAlpha/"
vDirProd  = "/opt/MontaPycote"
vVersao = "1" # 0 = Produção, 1 = alpha
sChamadoVers = ""

#altera de acordo com vVersao
if vVersao == "0":
	vDir = vDirProd
else:
	vDir = vDirAlpha	

#abre arquivo de log se parâmetro inicial não apenas o diretório atual. 
#Isto é. Caso haja arquivos a serem tratrados
param1 ='''['/home/beloni/Documentos/PyProjects/MontaPycoteAlpha/main.py']'''
if (param1 != str(sys.argv)):	
	text_file = open("logFile.txt", "w")
	for param in sys.argv:
	    text_file.write(param + "\n")
	text_file.close()

#pdb.set_trace()

#inicia variável para concatená-la sem erro
DATA = ''

#cria log com o nome dos arquivos
f = open('logFile.txt',"r")
for linha in f:
	DATA = DATA + linha	
f.close()

#split de todos os arquivos selecionados
entParametros = re.split('\\n',DATA)

#identifica o nome do arquivo e o caminho atual
sArquivo = str((re.split(r'[/\\]+',entParametros[1])[-1:]))[2:-2]
sChamado = str((re.split(r'[/\\]+',entParametros[1])[-2:-1]))[2:-2]
sCaminho = entParametros[1].replace(sArquivo,'')

#define lista com o nome dos arquivos
lArquivos = DATA.replace(sCaminho, '')
lArquivos = re.split('\\n',lArquivos)[1:]

#cria pasta a ser compacatada
valida = True
sChamadoVers = sChamado
pacVersao = 2
while valida:
	try:
		os.mkdir('Chamado_'+sChamadoVers)
		valida = False
	except :
	    sChamadoVers = sChamado+'_V' + str(pacVersao)
	    pacVersao += 1


sChamado = sChamadoVers

#Copia arquivos default para pasta do chamado
for l in lArquivos:
	os.system('cp '+ l + ' Chamado_'+sChamado+'')
os.system('cp '+ vDir +'/ALL_ERRORS.sql Chamado_'+sChamado +'')
os.system('cp '+ vDir +'/compila2.sql Chamado_'+sChamado+'')
os.system('cp '+ vDir +'/LF_TAB_LOG_PACOTE_CREATE.SQL Chamado_' + sChamado+'')


#instancia classe com os comandos do script sql
corpo = CorpoPacote()
corpo.set_numero_chamado(sChamado)
corpo.texto()

text_file = open("Chamado_"+sChamado+"/Chamado_"+sChamado+".sql", "w")
text_file.write("spool c:\sati\log_Chamado_" + sChamado +".txt \n")
text_file.write(corpo.sInicio + "\n")
text_file.write(corpo.sAlter + "\n")
text_file.write(corpo.sTabLog + "\n")

for l in lArquivos:
	if (l != ''):
		corpo.set_nome_script(l)
		corpo.texto()

		text_file.write(corpo.sScripts + "\n")

text_file.write(corpo.sLogMensagem + "\n")
text_file.write(corpo.sCompila + "\n")
text_file.write(corpo.sAllErrors + "\n")
text_file.write(corpo.sDadosAplic + "\n")

#tkMessageBox.showinfo("lArquivos", str(lArquivos))
#tkMessageBox.showinfo('sCaminho: ', sCaminho)
#tkMessageBox.showinfo('sChamado: ', sChamado)