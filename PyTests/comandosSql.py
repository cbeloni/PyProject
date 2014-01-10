#!/usr/bin/env python
# -*- coding: utf-8 -*-
class ParamPacotes(object):
	def __init__(self):
		self.set_numero_chamado('12345678')
		self.set_nome_script('padrao.sql')
		self.set_diretorio('c:\\SATI')

	def set_numero_chamado(self,NumeroChamado):
		self.NumeroChamado  = NumeroChamado		

	def set_nome_script(self,NomeScript):
		self.NomeScript = NomeScript
			
	def set_diretorio(self,Diretorio):
		self.Diretorio = Diretorio

class CorpoPacote(object):
	def __init__ (self,numero_chamado,nome_script,diretorio):
		self._numero_chamado = numero_chamado
		self._nome_script = nome_script
		self._diretorio = diretorio

		sInicio = '''PROMPT --**************************** [ INICIO DA APLICAÇAO ] ***********************************--;
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
SET SERVEROUTPUT OFF 
set linesize 1000 
set pagesize 4000 
set define off 
'''
		sAlter = '''PROMPT --**************************** [ ALTER SESSION PARA NLS_DATE_FORMAT = 'DD/MM/YYYY' ] *****--;
alter session set nls_date_format = 'dd/mm/yyyy'; 
'''

		sTabLog = '''PROMPT --**************************** [ APLICANDO 'CRIANDO TABELA DE LOG DE MENSAGENS' ] *****--;
@'''+ self._diretorio + '''\LF_TAB_LOG_PACOTE_CREATE.SQL '''

#>>não funcionou
		sScripts = '''PROMPT --**************************** [ APLICANDO ''' + self._nome_script + '''] *********************--; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
@''' + self._diretorio + '''\\''' + self._nome_script + '''
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; ''' 
		sLogMensagem = '''PROMPT --**************************** [ LOG DE MENSAGENS ] ******************************--;
SELECT * FROM LF_TAB_LOG_PACOTE WHERE CHAMADO =TRIM(' ''' + self._numero_chamado +''' '); '''
#<<não funcionou

		sCompila = '''PROMPT --**************************** [ APLICANDO 'COMPILA2.SQL' ] ******************************--;
@''' + self._diretorio + '''\compila2.sql '''

		sAllErrors = '''PROMPT --**************************** [ APLICANDO 'ALL_ERRORS.SQL' ] ****************************--;
@''' + self._diretorio +'''\\all_errors.sql '''
	
		sDadosAplic = '''PROMPT --**************************** [ DADOS DA APLICACAO ] *************************************--;
show user; 
SELECT COD_HOLDING FROM LF_EMPRESA_HOLDING; 
show parameters db_name; 
SELECT GLOBAL_NAME FROM GLOBAL_NAME; 
SELECT INSTANCE_NAME, VERSION FROM V$INSTANCE; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
PROMPT --**************************** [ FIM DA APLICAÇAO ] **************************************--;
 
spool off '''