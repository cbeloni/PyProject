#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import tkMessageBox
import re
import os
from comandosSql import *

#abre arquivo de log se parâmetro inicial não apenas o diretório atual. 
#Isto é. Caso haja arquivos a serem tratrados
param1 ='''['/home/beloni/Documentos/PyProjetos/MontaPycote/main.py']'''
if (param1 != str(sys.argv)):	
	text_file = open("logFile.txt", "w")
	for param in sys.argv:
	    text_file.write(param + "\n")
	text_file.close()

#inicia variável para concatená-la sem erro
DATA = ''

#cria log com o nome dos arquivos
f = open('logFile.txt',"r")
for linha in f:
	DATA = DATA + linha	
f.close()

#split de com de todos os arquivos selecionados
entParametros = re.split('\\n',DATA)

#identifica o nome do arquivo e o caminho atual
sArquivo = str((re.split(r'[/\\]+',entParametros[1])[-1:]))[2:-2]
sChamado = str((re.split(r'[/\\]+',entParametros[1])[-2:-1]))[2:-2]
sCaminho = entParametros[1].replace(sArquivo,'')

#define lista com o nome dos arquivos
lArquivos = DATA.replace(sCaminho, '')
lArquivos = re.split('\\n',lArquivos)[1:]

#cria pasta a ser compacatada
os.mkdir('Chamado_'+sChamado)
for l in lArquivos:
	os.system('cp '+ l + ' Chamado_'+sChamado)

#instancia classe para parâmetros dos comandos do script sql
parPacote = ParamPacotes()
parPacote.set_numero_chamado(sChamado)

#instancia classe com os comandos do script sql
corpo = CorpoPacote()
corpo.sInicio

text_file = open("Chamado_"+sChamado+"/Chamado_"+sChamado+".sql", "w")
text_file.write("spool c:\sati\log_Chamado_" + sChamado +".txt \n")
text_file.write(corpo.sInicio + "\n")
text_file.write(corpo.sAlter + "\n")
text_file.write(corpo.sTabLog + "\n")

for l in lArquivos:
	if (l != ''):

		parPacote.set_nome_script(l)
		sScripts = '''PROMPT --**************************** [ APLICANDO ''' + parPacote.NomeScript + '''] *********************--; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
@''' + parPacote.Diretorio + '''\\''' + parPacote.NomeScript + '''
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; '''	
		text_file.write(sScripts + "\n")

text_file.write(corpo.sLogMensagem + "\n")
text_file.write(corpo.sCompila + "\n")
text_file.write(corpo.sAllErrors + "\n")
text_file.write(corpo.sDadosAplic + "\n")

#tkMessageBox.showinfo("lArquivos", str(lArquivos))
#tkMessageBox.showinfo('sCaminho: ', sCaminho)
#tkMessageBox.showinfo('sChamado: ', sChamado)