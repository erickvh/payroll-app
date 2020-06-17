/*
** Inicio de trigger para verificar que cuando se selecciona fijo = false en la tabla catalogo_descuento
** sea un porcentaje valido el que se pretende ingresar
*/

create or replace function 
catalogo_descuento_trigger() 
returns trigger as $tgr_catalogo$
declare
begin 
if (new.fijo = False and (new.descuento >= 100 or new.descuento<1)) then
  raise exception '%','catalogo_descuento_trigger';
end if;
return new;
end;
$tgr_catalogo$ language plpgsql;


create trigger tgr_catalogo 
before insert or update
on catalogo_descuento for each row
execute procedure catalogo_descuento_trigger(); 



create or replace function 
agregar_comision() 
returns trigger as $tgr_comision$
declare
v_porcentaje numeric :=0;
begin 
if new.comision = True then
	select round(avg(c.porcentaje)/100,2) into v_porcentaje from comisiones as c where new.ingreso between c.minimo and c.maximo;
end if;

if v_porcentaje is not null then
    new.porcentaje := v_porcentaje;
end if;

return new;
end;
$tgr_comision$ language plpgsql;


create trigger tgr_comision 
before insert or update
on catalogo_ingreso for each row
execute procedure agregar_comision(); 

/*
** Fin de la definicion del trigger
*/



create or replace function 
actualizar_centro_costo() 
returns trigger as $tgr_costo$
declare
begin 
if (new.remanente > new.presupuesto) then
  raise exception '%','No se puede actualizar centro de costo';
end if;
return new;
end;
$tgr_costo$ language plpgsql;


create trigger tgr_costo 
before insert or update
on centro_costos for each row
execute procedure actualizar_centro_costo(); 



