#!/usr/bin/env python
# -*- coding: utf-8 -*-
class ParamPacotes(object):
	def __init__(self,numero_chamado,nome_script,diretorio):
		self._numero_chamado = numero_chamado
		self._nome_script = nome_script
		self._diretorio = diretorio

class CorpoPacote(ParamPacotes):
	def __init__ (self,numero_chamado,nome_script,diretorio):
		self._numero_chamado = numero_chamado
		self.sScripts = ''' PROMPT --**************************** [ APLICANDO ''' + numero_chamado + ''' ] *********************--; '''

cp = CorpoPacote('1234323','script','c:\\sati')
#pp = ParamPacotes('1234323','script','c:\\sati')

print cp._numero_chamado
print cp.sScripts