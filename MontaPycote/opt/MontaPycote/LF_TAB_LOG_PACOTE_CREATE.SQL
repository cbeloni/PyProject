DECLARE
   V_ERRO VARCHAR2(32000) := ' ';
BEGIN
   BEGIN
      EXECUTE IMMEDIATE 'DROP TABLE LF_TAB_LOG_PACOTE';
   EXCEPTION WHEN OTHERS THEN
      null;
   END;   
   
   BEGIN 
      EXECUTE IMMEDIATE 'CREATE TABLE LF_TAB_LOG_PACOTE(ID          VARCHAR2(20),
                                                        CHAMADO     VARCHAR2(10),
                                                        NOME_SCRIPT VARCHAR2(100),
                                                        TIPO        VARCHAR2(1),
                                                        MENSAGEM    VARCHAR2(200))';
   EXCEPTION WHEN OTHERS THEN
      null;
   END;                                   
   /*
   BEGIN   
      EXECUTE IMMEDIATE 'GRANT SELECT, UPDATE, INSERT, DELETE ON LF_TAB_LOG_PACOTE TO USER_LF';
   EXCEPTION WHEN OTHERS THEN
      V_ERRO := SQLERRM;
      INSERT INTO LF_TAB_LOG_PACOTE(ID,CHAMADO,NOME_SCRIPT,TIPO,MENSAGEM) VALUES ('0.4','XXXXXXX','LF_TAB_LOG_PACOTE_CREATE.SQL','M',V_ERRO);
   END;                                
   
   BEGIN   
      EXECUTE IMMEDIATE 'GRANT SELECT, UPDATE, INSERT, DELETE ON LF_TAB_LOG_PACOTE TO LF';
   EXCEPTION WHEN OTHERS THEN
      V_ERRO := SQLERRM;
      INSERT INTO LF_TAB_LOG_PACOTE(ID,CHAMADO,NOME_SCRIPT,TIPO,MENSAGEM) VALUES ('0.5','XXXXXXX','LF_TAB_LOG_PACOTE_CREATE.SQL','M',V_ERRO);
   END;   */
END;
/