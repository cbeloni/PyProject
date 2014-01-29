#!/usr/bin/env python
# -*- coding: utf-8 -*-
class CorpoPacote(object):
	def __init__(self):
		self.set_numero_chamado('NAOINFORMADO')
		self.set_nome_script('NAOINFORMADO.sql')
		self.set_diretorio('c:\\SATI')

	def set_numero_chamado(self,NumeroChamado):
		self.NumeroChamado  = NumeroChamado		

	def set_nome_script(self,NomeScript):
		self.NomeScript = NomeScript
			
	def set_diretorio(self,Diretorio):
		self.Diretorio = Diretorio

	def texto (self):
		self.sInicio = '''PROMPT --**************************** [ INICIO DA APLICAÇAO ] ***********************************--;
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
SET SERVEROUTPUT OFF 
set linesize 1000 
set pagesize 4000 
set define off 
'''
		self.sAlter = '''PROMPT --**************************** [ ALTER SESSION PARA NLS_DATE_FORMAT = 'DD/MM/YYYY' ] *****--;
alter session set nls_date_format = 'dd/mm/yyyy'; 
'''

		self.sTabLog = '''PROMPT --**************************** [ APLICANDO 'CRIANDO TABELA DE LOG DE MENSAGENS' ] *****--;
@'''+ self.Diretorio + '''\LF_TAB_LOG_PACOTE_CREATE.SQL '''

#>>não funcionou
		self.sScripts = '''PROMPT --**************************** [ APLICANDO ''' + self.NomeScript + '''] *********************--; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
@''' + self.Diretorio + '''\\''' + self.NomeScript + '''
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; ''' 
		self.sLogMensagem = '''PROMPT --**************************** [ LOG DE MENSAGENS ] ******************************--;
SELECT * FROM LF_TAB_LOG_PACOTE WHERE CHAMADO like TRIM('%''' + [self.NumeroChamado[0:self.NumeroChamado.find('_')], self.NumeroChamado] [ self.NumeroChamado.find('_') < 0] +'''%'); '''
#<<não funcionou

		self.sCompila = '''PROMPT --**************************** [ APLICANDO 'COMPILA2.SQL' ] ******************************--;
@''' + self.Diretorio + '''\compila2.sql '''

		self.sAllErrors = '''PROMPT --**************************** [ APLICANDO 'ALL_ERRORS.SQL' ] ****************************--;
@''' + self.Diretorio +'''\\all_errors.sql '''
	
		self.sDadosAplic = '''PROMPT --**************************** [ DADOS DA APLICACAO ] *************************************--;
show user; 
SELECT COD_HOLDING FROM LF_EMPRESA_HOLDING; 
show parameters db_name; 
SELECT GLOBAL_NAME FROM GLOBAL_NAME; 
SELECT INSTANCE_NAME, VERSION FROM V$INSTANCE; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
PROMPT --**************************** [ FIM DA APLICAÇAO ] **************************************--;
 
spool off '''
