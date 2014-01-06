spool c:\sati\log_Chamado_EMPRESA.txt 
PROMPT --**************************** [ INICIO DA APLICAÇAO ] ***********************************--;
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
SET SERVEROUTPUT OFF 
set linesize 1000 
set pagesize 4000 
set define off 

PROMPT --**************************** [ ALTER SESSION PARA NLS_DATE_FORMAT = 'DD/MM/YYYY' ] *****--;
alter session set nls_date_format = 'dd/mm/yyyy'; 

PROMPT --**************************** [ APLICANDO 'CRIANDO TABELA DE LOG DE MENSAGENS' ] *****--;
@c:\SATI\LF_TAB_LOG_PACOTE_CREATE.SQL 
PROMPT --**************************** [ APLICANDO 6223999] *********************--; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
@c:\SATI\6223999
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
PROMPT --**************************** [ LOG DE MENSAGENS ] ******************************--;
SELECT * FROM LF_TAB_LOG_PACOTE WHERE CHAMADO =TRIM(' EMPRESA '); 
PROMPT --**************************** [ APLICANDO 'COMPILA2.SQL' ] ******************************--;
@c:\SATI\compila2.sql 
PROMPT --**************************** [ APLICANDO 'ALL_ERRORS.SQL' ] ****************************--;
@c:\SATI\all_errors.sql 
PROMPT --**************************** [ DADOS DA APLICACAO ] *************************************--;
show user; 
SELECT COD_HOLDING FROM LF_EMPRESA_HOLDING; 
show parameters db_name; 
SELECT GLOBAL_NAME FROM GLOBAL_NAME; 
SELECT INSTANCE_NAME, VERSION FROM V$INSTANCE; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
PROMPT --**************************** [ FIM DA APLICAÇAO ] **************************************--;
 
spool off 