declare
    cursor c is
      select owner, object_type, object_name
        from all_objects
       where status = 'INVALID'
         and object_type in ('FUNCTION','PACKAGE','PACKAGE BODY','PROCEDURE','TRIGGER')
         and owner = 'LF';
    r c%rowtype;        
    v_qtd_invalidos       number := 0;
    v_qtd_invalidos_bk    number := 0;
    
    procedure p_compila_parcial is        
    begin
        for r in c loop
            begin
                dbms_ddl.alter_compile (r.object_type, r.owner, r.object_name);
            exception when others then
                dbms_output.put_line (sqlerrm);
                dbms_output.put_line(lpad(r.object_type,15) || r.object_name);                
            end;
        end loop;
    exception when others then
        dbms_output.put_line('Erro não previsto Codigo: ' || sqlcode || ' Mensagem: ' || sqlerrm);
    end;
begin
    loop
        select count (*)
          into v_qtd_invalidos
          from all_objects
         where status = 'INVALID'
           and owner  = 'LF';

        if v_qtd_invalidos <> v_qtd_invalidos_bk then
            p_compila_parcial;
            v_qtd_invalidos_bk := v_qtd_invalidos;
        else
            exit;
        end if;
    end loop;
end;
/

PROMPT --**************************** [ Objetos inválidos depois da compilação ] ****************************--;
select object_type, object_name
 from all_objects
where status = 'INVALID'
  and object_type in ('FUNCTION','PACKAGE','PACKAGE BODY','PROCEDURE','TRIGGER')
  and owner = 'LF'
/

