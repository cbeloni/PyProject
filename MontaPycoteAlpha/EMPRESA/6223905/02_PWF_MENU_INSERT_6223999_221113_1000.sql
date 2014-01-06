Declare

--***********************************************************************************
--* ALTERAR APENAS NOS PONTOS INDICADOS, PROCURAR PELA PALAVRA "ALTERAR AQUI"
--***********************************************************************************

   type TMenu is record (
         descr      lf_pwf_menu.mnu_desc %type
        ,dll        lf_pwf_transaction.tra_library %type
        ,id         integer );

   type TMenuSet is table of TMenu index by binary_integer;  -- conjunto dos valores

   aMenu_1    TMenuSet;
   aMenu_2    TMenuSet;
   aMenu_3    TMenuSet;

   vMODDULO integer;

------------------------------------------------------------------------------------------
   function tiraAcento ( p_string in varchar2 )  return  varchar2 is
      v_tamanho      number;
      i              number;
      v_caracter     varchar2(1);
      v_new_string   varchar2(5000);
   begin
      if p_string is not null then
         v_tamanho    := length(p_string);
         v_new_string := null;

         for i in 1..v_tamanho loop
            v_caracter := SUBSTR(p_string, i, 1);

            if ASCII(v_caracter) = 128 then
               v_caracter := 'C';
            elsif ASCII(v_caracter) IN (129, 150, 151, 163) then
               v_caracter := 'u';
            elsif ASCII(v_caracter) IN (130, 136, 137, 138) then
               v_caracter := 'e';
            elsif ASCII(v_caracter) IN (131, 132, 133, 134, 160) then
               v_caracter := 'a';
            elsif ASCII(v_caracter) = 135 then
               v_caracter := 'c';
            elsif ASCII(v_caracter) IN (139, 140, 141, 161) then
               v_caracter := 'i';
            elsif ASCII(v_caracter) IN (142, 143) then
               v_caracter := 'A';
            elsif ASCII(v_caracter) = 144 then
               v_caracter := 'E';
            elsif ASCII(v_caracter) IN (147, 148, 149, 162) then
               v_caracter := 'o';
            elsif ASCII(v_caracter) IN (150, 151, 163) then
               v_caracter := 'u';
            elsif ASCII(v_caracter) = 153 then
               v_caracter := 'O';
            elsif ASCII(v_caracter) = 154 then
               v_caracter := 'U';
            elsif ASCII(v_caracter) = 164 then
               v_caracter := 'n';
            elsif ASCII(v_caracter) = 165 then
               v_caracter := 'N';
            elsif ASCII(v_caracter) = 166 then
               v_caracter := 'a';
            elsif ASCII(v_caracter) = 167 then
               v_caracter := 'o';
            elsif ASCII(v_caracter) < 32 or  ASCII(v_caracter) > 127 then
               v_caracter := '.';
            end if;

            v_new_string := v_new_string || v_caracter;
         end loop;

         return v_new_string;

      else
         return p_string;
      end if;
   end;

------------------------------------------------------------------------------------------
   function insereMenu(pDesc varchar2, pParent integer, pTraId integer, pNivel integer) return integer is
     vMnuId integer;
     vOrder integer;
     v_count integer;
   begin
      -- proximo ID de menu
      select nvl(max(mnu_id)+1,0)  into vMnuId
      from lf_pwf_menu where mnu_id >= 9000;

      if vMnuId = 0 then
         vMnuId := 9000;
      end if;

      select nvl(max(mnu_order), 0)+1 into vOrder
      from lf_pwf_menu
      where mnu_parent = pParent;

      -- verifico se o menu secundario existe
      select count(*) into v_count from lf_pwf_menu
       where MNU_DESC = pDesc
         and MNU_PARENT = pParent
         and MNU_LEVEL = pNivel;

       if v_count = 0 then
          -- insiro o menu secundário
          insert into lf_pwf_MENU
           ( mnu_id, mnu_guid, mod_id, mnu_desc, pwfversion,
             mnu_level,  mnu_parent, mnu_order, mnu_active, tra_id)
          values
           ( vMnuId, vMnuId, vMODDULO,pDesc,'3.0', pNivel, pParent, vOrder, 'S', pTraId);
       else
          select mnu_id into vMnuId from lf_pwf_menu where MNU_DESC = pDesc and MNU_LEVEL = pNivel;
       end if;
       
      return vMnuId;
   end;

------------------------------------------------------------------------------------------
   function insereTransacao(pDesc varchar2, pDll varchar2) return integer is
     vTraId integer;
     vCount number := 0;
   begin
      -- proximo ID de transacao
      select max(tra_id) + 1 into vTraId
      from lf_pwf_transaction;
      
      select count(1)
        into vcount
        from lf_pwf_transaction
       where tra_library = pDll;
      
      if vcount = 0 then
        -- insire transacao
        insert into lf_pwf_transaction
         ( tra_id, tra_desc, tra_library, mod_id, pwfversion )
        values
         ( vTraId, pDesc, pDll, vMODDULO,'3.0');
      end if; 

      return vTraId;
   end;

------------------------------------------------------------------------------------------
   function pegaParentId(pMenu TMenuSet, pNivel integer, pParent integer, pIncluiCaminho boolean) return integer is
     vParent integer;
--     vTraId integer;
   begin
      if pMenu.exists(pNivel) then
         begin

            for rMenu in ( select mnu_id, tra_id, mnu_desc
                           from lf_pwf_menu
                           where mod_id = vMODDULO
                             and nvl(mnu_parent, -1) = nvl(pParent, -1) )
            loop
               if tiraAcento(rMenu.mnu_desc) = tiraAcento(pMenu(pNivel).descr) then
                  if rMenu.tra_id is not null then
                     raise_application_error(-20001, 'O menu ' || pMenu(pNivel).descr || ' (nivel ' || pNivel || ') ja e final e nao pode receber sub-menu.');
                  end if;
                  vParent := rMenu.mnu_id;
                  
                  --***********
                  -- ATIVA O MENU CASO ESTEJA DESATIVADO
                  dbms_output.put_line('pParent        : '||vParent);
                  dbms_output.put_line('rMenu.mnu_desc : '||rMenu.mnu_desc);
                  
                  update lf_pwf_menu
                     set mnu_active = 'S'
                   where MNU_ID     = vParent
                     and mnu_desc   = rMenu.mnu_desc;
                  --***********                  
                  
                  exit;
               end if;
            end loop;

            if vParent is null then
               if pIncluiCaminho then
                  vParent := insereMenu( pMenu(pNivel).descr, pParent, null, pNivel);
               else
                  raise_application_error(-20001, 'O menu ' || pMenu(pNivel).descr || ' (nivel ' || pNivel || ') nao existe.');
               end if;
            end if;
         end;

         return pegaParentId(pMenu, pNivel + 1, vParent, pIncluiCaminho);
      else
         return pParent;
      end if;
   end;

------------------------------------------------------------------------------------------

   procedure cadastraMenu(pMenu TMenuSet, pIncluiCaminho boolean) is
     vParent integer;
     vTraId integer;
     vNivel integer;
     ret integer;
   begin
      vParent := pegaParentId(pMenu, 0, null, pIncluiCaminho);

      vTraId := insereTransacao(pMenu(99).descr, pMenu(99).dll);

      vNivel := pMenu.prior(99) + 1;

      ret := insereMenu( pMenu(99).descr, vParent, vTraId, vNivel );
   end;

------------------------------------------------------------------------------------------
-- inicio do processo
------------------------------------------------------------------------------------------

Begin
   vMODDULO := 1;         -- 1-SATI  2-IRPJ
   
--*** ALTERAR AQUI - INICIO
 
   -- MENU RAIZ, LEVEL 0
   aMenu_3(0).descr := 'Específicos';  --> SEMPRE SERÁ ESPECÍFICO

   -- SUBMENU, LEVEL 1
   aMenu_3(1).descr := 'Gerência';  --> MUDAR CASO FOR CRIAR NOVO SUBMENU

   -- CHAMADA DA TELA, QUE FICARÁ ABAIXO DO SUBMENU ACIMA
   aMenu_3(99).descr := 'Arcelor - Alteração em Lote'; -- DESCRICAO DA CHAMADA DA TELA
   aMenu_3(99).dll   := 'AlterarEmLote.exe';  -- TELA QUE SERÁ CHAMADA, EXE OU DLL

--*** ALTERAR AQUI - FIM

   -- GRAVA OS MENUS
   cadastraMenu(aMenu_3, true); 
 
   -- ATIVA O MENU DE ESPECIFICOS CASO NO CLIENTE ESTEJA DESATIVADO
   UPDATE LF_PWF_MENU
      SET MNU_ACTIVE = 'S'
    WHERE MNU_DESC   = 'Específicos'
      AND MNU_LEVEL  = 0;

   commit;
end;

/
Insert into LF_FUNCOES (COD_FUNCAO,MODULO,DESCRICAO,COD_STATUS,USUARIO,DATATUAL,HORATUAL,ATIVO,CUSTOM,MNU_ID,PWFGUID) 
values 
('ESP','ALTERAREMLOTE','Alteraçao de lote tp_lanc','01','LF',sysdate,'00:00:00','S',null,null,sys_guid())
/
INSERT INTO LF_RELATORIOS_GENERICOS (SEQUENCIA,COMANDO,PROCEDURE,PARAMETROS,PWFGUID) VALUES (1,'CTMARCALT2','P_CTM_RELAT_ALTERARLOTE',NULL,sys_guid())
/
INSERT INTO LF_MENUREL (CODREL,DESCRICAO,COMANDO,ATIVO,IND_ARQUIVO,NOME_ARQUIVO,COD_HOLDING,COD_GRUPO,CODCLAS,DESCRICAO_ESP,EXECUTA_BACKGROUND,IND_SATIWEB,TRA_ID,NOME_RPT,SQL_QUERY,PWFGUID) 
VALUES ('P_CTM_RELAT_ALTERARLOTE','RELATÓRIO DE ALTERAÇÃO DO COD_TP_LANC_IMP','CTMARCALT2','S','N',NULL,'%',NULL,NULL,'RELATÓRIO DE ALTERAÇÃO DO COD_TP_LANC_IMP','S','SG01',NULL,NULL,NULL,SYS_GUID())
/