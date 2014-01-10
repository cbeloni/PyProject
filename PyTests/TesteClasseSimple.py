#!/usr/bin/env python
# -*- coding: utf-8 -*-
class ParamPacotes(object):
	def __init__(self,numero_chamado,nome_script,diretorio):
		self._numero_chamado = numero_chamado
		self._nome_script = nome_script
		self._diretorio = diretorio
	def set_numero_chamado(self,numero_chamado):
		self._numero_chamado = numero_chamado
	def textos (self):
		self.sScripts = ''' PROMPT --**************************** [ APLICANDO ''' + self._numero_chamado + ''' ] *********************--; '''

cp = ParamPacotes('31234343', ' abcde ', 'c:')

cp.textos()

print cp.sScripts

cp.set_numero_chamado('12334325')

cp.textos()

print cp.sScripts

