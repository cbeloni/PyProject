#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

#DATA = '''/home/beloni/Documentos/PyProjetos/MontaPycote/main.py
#/home/beloni/Documentos/PyProjetos/MontaPycote/EMPRESA/95142496/01_P_CTM_ALT_PERM_6223905_221113_1000.SQL
#/home/beloni/Documentos/PyProjetos/MontaPycote/EMPRESA/95142496/02_P_CTM_RELAT_ALT_6223905_221113_1000.SQL
#/home/beloni/Documentos/PyProjetos/MontaPycote/EMPRESA/95142496/02_PWF_MENU_INSERT_6223905_221113_1000.sql
#/home/beloni/Documentos/PyProjetos/MontaPycote/EMPRESA/95142496/03_P_CTM_ALTERARLOTE_6223905_221113_1000.SQL'''

DATA = ''

f = open('logFile.txt',"r")
for linha in f:
	DATA = DATA + linha	

print DATA
f.close()

entParametros = re.split('\\n',DATA)

sArquivo = str((re.split(r'[/\\]+',entParametros[1])[-1:]))[2:-2]
sCaminho = entParametros[1].replace(sArquivo,'')

sChamado = str((re.split(r'[/\\]+',entParametros[1])[-2:-1]))[2:-2]
print 'sChamado: ' + sChamado

#for i in range(len(entParametros)):
#	if (i > 0):
#		sCaminho = entParametros[i].replace('main.py','')
lArquivos = DATA.replace(sCaminho, '')
lArquivos = re.split('\\n',lArquivos)[1:]

print 'sCaminho: '+ sCaminho
print 'Arquivos' + str(lArquivos)