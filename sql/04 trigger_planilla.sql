create or replace function 
crear_planilla() 
returns trigger as $tgr_create_planilla$
declare
empleado RECORD;
codigo TEXT := 'BE';
begin 
	for empleado in select * from empleados loop
		INSERT INTO boleta_pago(
			codigo, fecha_pago, dias_laborales, dias_trabajados, salario_actual, total_comision, total_descuento, total_ingreso, pago_total, pago_neto, activa, empleado_id, planilla_id)
			VALUES (codigo || CAST(empleado.id as text) || CAST(new.id as text), current_date, 23, 23, empleado.salario, 0.0, 0.0, 0.0, 0.0, 0.0, True, empleado.id, new.id);
	end loop;
return NULL;
end;
$tgr_create_planilla$ language plpgsql;


create trigger tgr_create_planilla 
after insert
on planilla for each row
execute procedure crear_planilla(); 




create or replace function 
actualizar_planilla() 
returns trigger as $tgr_update_planilla$
declare
empleado RECORD;
ingreso NUMERIC :=0;
comision NUMERIC :=0;
descuento NUMERIC :=0;
descuento_ley NUMERIC :=0;
total_ingreso_p NUMERIC :=0;
total_descuento_p NUMERIC :=0;
begin 
if new.activa = False then

	for empleado in select * from empleados loop
		ingreso = get_ingreso_total_comision(empleado.id);
		descuento = get_descuento_total(empleado.id);
		descuento_ley = get_descuento_ley(empleado.salario);
		comision = get_ingreso_total_comision(empleado.id);
		total_ingreso_p = total_ingreso_p + empleado.salario +case when comision is not null then comision else 0.0 end + case when ingreso is not null then ingreso else 0.0 end;
		total_descuento_p = total_descuento_p + descuento_ley + case when descuento is not null then descuento else 0.0 end;
		UPDATE public.boleta_pago
			SET fecha_pago=current_date, salario_actual=empleado.salario, 
				total_comision = case when comision is not null then comision else 0.0 end, 
				total_descuento = descuento_ley + case when descuento is not null then descuento else 0.0 end, 
				total_ingreso = case when ingreso is not null then ingreso else 0.0 end, 
				pago_total = total_ingreso + salario_actual + total_comision - total_descuento, 
				pago_neto = pago_total, 
				activa = False
			WHERE empleado_id= empleado.id and planilla_id= old.id;
	end loop;
	new.total_pago_empleado = total_ingreso_p - total_descuento_p;
	new.total_descuento = total_descuento_p;
	new.total_pagar =  total_ingreso_p;

end if;
return new;
end;
$tgr_update_planilla$ language plpgsql;


create trigger tgr_update_planilla 
before update
on planilla for each row
execute procedure actualizar_planilla(); 



