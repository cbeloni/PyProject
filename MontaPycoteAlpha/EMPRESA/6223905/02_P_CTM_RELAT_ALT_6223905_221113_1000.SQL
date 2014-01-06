CREATE OR REPLACE PROCEDURE 
P_CTM_RELAT_ALTERARLOTE (P_HOLDING   IN  LF_NF_ENTRADA.COD_HOLDING   %TYPE,
					     P_MATRIZ    IN  LF_NF_ENTRADA.COD_MATRIZ    %TYPE,
					     P_FILIAL    IN  LF_NF_ENTRADA.COD_FILIAL    %TYPE,
					     P_DATAINI   IN  VARCHAR2,
					     P_DATAFIM   IN  VARCHAR2,
					     P_USUARIO   IN  VARCHAR2,
					     P_EXIST     OUT INTEGER) IS 

V_TABELA NUMBER(2);
V_CFOP   VARCHAR2(4);



CURSOR cLog IS
	SELECT A.COD_MATRIZ,
		   A.COD_FILIAL,
		   A.USUARIO,
		   A.DATATUAL,
		   A.NUM_NF,
		   A.SERIE,
		   A.DT_ENTRADA,
		   A.DOCNUM,
		   A.CFOP
	 FROM  T_LOG_ALTERARLOTE A
	WHERE  UPPER(A.COD_MATRIZ) 	= UPPER(P_MATRIZ)
	  AND  UPPER(A.COD_FILIAL)	LIKE UPPER(P_FILIAL)
	  AND  A.DT_ENTRADA BETWEEN TO_DATE(P_DATAINI,'DD/MM/YYYY') 
	   					    AND TO_DATE(P_DATAFIM,'DD/MM/YYYY');
vLog  cLog  %ROWTYPE;

BEGIN
	P_EXIST := 0;

	-- CABEÇALHO
	PKG_RELATORIO.INICIALIZA(P_HOLDING,
	                         P_MATRIZ,
	                         P_FILIAL,
	                         'CTMARCALT2',
	                         'RELATÓRIO DE ALTERAÇÃO DO COD_TP_LANC_IMP',
	                         TO_DATE(P_DATAINI, 'DD/MM/YYYY'),
	                         TO_DATE(P_DATAFIM, 'DD/MM/YYYY'));
	

    --CABEÇALHO CORRIGIR NOME DE USUÁRIO
	--PKG_RELATORIO.V_CABECALHO(1) := 'CTMARCALTL                                                                 RELATÓRIO DE ALTERAÇÃO DO COD_TP_LANC_IMP                                               Data Geração: '|| sysdate;
	--PKG_RELATORIO.V_CABECALHO(2) := 'MATRIZ: '|| P_MATRIZ || '                                                                 																            Nome: '|| P_USUARIO;
	--PKG_RELATORIO.V_CABECALHO(3) := 'FILIAL: '|| P_FILIAL || '                                                  PERÍODO:' || P_DATAINI ||' A '|| P_DATAFIM ||'                                          Data de Alteração: 01/01/2001';
    

    -- COLUNAS		         
    PKG_RELATORIO.DELCOLUNA(1,1);
    PKG_RELATORIO.INCCOLUNA('NÚMERO NF'                               , 15, 'E', FALSE); -- 1
    PKG_RELATORIO.INCCOLUNA('SERIE'                                   , 10, 'E', FALSE); -- 2
    PKG_RELATORIO.INCCOLUNA('DATA DE ENTRADA'                         , 15, 'E', FALSE); -- 3
    PKG_RELATORIO.INCCOLUNA('DOCNUM'                                  , 15, 'E', FALSE); -- 4
    PKG_RELATORIO.INCCOLUNA('CFOP'                                    , 10, 'E', FALSE); -- 5
    PKG_RELATORIO.INCCOLUNA('NOME USUÁRIO'                            , 20, 'E', FALSE); -- 6
    PKG_RELATORIO.INCCOLUNA('DATA ALTERAÇÃO'                          , 10, 'E', FALSE); -- 7
	
	--PKG_RELATORIO.GRVLINHA(' Nome usuário: '||P_USUARIO);

	

	


		OPEN cLog;
		FETCH cLog INTO vLog;
    	
    	IF (cLog%FOUND = TRUE ) THEN
	    	PKG_RELATORIO.ALTFILIAL (P_HOLDING,vLog.COD_MATRIZ,vLog.COD_FILIAL,TRUE);      
        END IF; 


	  	WHILE cLog%FOUND 
	  	LOOP
			--DBMS_OUTPUT.PUT_LINE('GERAÇÃO DO RELATÓRIO');			 

             PKG_relatorio.valorcol(1,1,vLog.NUM_NF);
             PKG_relatorio.valorcol(1,2,vLog.SERIE);
             PKG_relatorio.valorcol(1,3,vLog.DT_ENTRADA);
             PKG_relatorio.valorcol(1,4,vLog.DOCNUM);
             PKG_relatorio.valorcol(1,5,vLog.CFOP);
             PKG_relatorio.valorcol(1,6,vLog.USUARIO);
             PKG_relatorio.valorcol(1,7,vLog.DATATUAL);
             PKG_RELATORIO.IMPVALORCOL(1);

			 P_EXIST := 1;
		FETCH cLog INTO vLog;
		END LOOP;

		CLOSE cLog;	

	
	--PKG_Relatorio.GrvLinha('');
	IF (P_EXIST = 1) THEN
		COMMIT;
	ELSE
		ROLLBACK; 
	END IF; 	
END;
/
GRANT EXECUTE ON  P_CTM_RELAT_ALTERARLOTE TO USER_LF
/