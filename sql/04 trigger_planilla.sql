create or replace function 
crear_planilla() 
returns trigger as $tgr_create_planilla$
declare
rec_empleado RECORD;
c_codigo TEXT := 'BE';
begin 
	for rec_empleado in select * from empleados loop
		INSERT INTO boleta_pago(
			codigo, fecha_pago, dias_laborales, dias_trabajados, salario_actual, total_comision, total_descuento, total_ingreso, pago_total, pago_neto, activa, empleado_id, planilla_id)
			VALUES (c_codigo || CAST(rec_empleado.id as text) || CAST(new.id as text), current_date, 23, 23, rec_empleado.salario, 0.0, 0.0, 0.0, 0.0, 0.0, True, rec_empleado.id, new.id);
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
rec_empleado RECORD;
v_ingreso NUMERIC :=0;
v_comision NUMERIC :=0;
v_descuento NUMERIC :=0;
v_descuento_ley NUMERIC :=0;
v_total_ingreso NUMERIC :=0;
v_total_descuento NUMERIC :=0;
v_renta NUMERIC :=0;
begin 
if new.activa = False then
	for rec_empleado in select * from empleados loop
		v_ingreso = get_ingreso_total_comision(rec_empleado.id, new.id);
		v_descuento = get_descuento_total(rec_empleado.id, new.id);
		v_descuento_ley = get_descuento_ley(rec_empleado.salario);
		v_comision = get_ingreso_total_comision(rec_empleado.id, new.id);
		v_renta = get_renta(rec_empleado.salario);
		v_total_ingreso = v_total_ingreso + rec_empleado.salario +case when v_comision is not null then v_comision else 0.0 end + case when v_ingreso is not null then v_ingreso else 0.0 end;
		v_total_descuento = v_total_descuento + v_descuento_ley + v_renta + case when v_descuento is not null then v_descuento else 0.0 end;
		UPDATE public.boleta_pago
			SET fecha_pago=current_date, salario_actual=rec_empleado.salario, 
				total_comision = case when v_comision is not null then v_comision else 0.0 end, 
				total_descuento = v_renta + v_descuento_ley + case when v_descuento is not null then v_descuento else 0.0 end, 
				total_ingreso = case when v_ingreso is not null then v_ingreso else 0.0 end, 
				pago_total = total_ingreso + salario_actual + total_comision - total_descuento, 
				pago_neto = pago_total, 
				activa = False
			WHERE empleado_id= rec_empleado.id and planilla_id= old.id;
	end loop;
	new.total_pago_empleado = v_total_ingreso - v_total_descuento;
	new.total_descuento = v_total_descuento;
	new.total_pagar =  v_total_ingreso;

end if;
return new;
end;
$tgr_update_planilla$ language plpgsql;


create trigger tgr_update_planilla 
before update
on planilla for each row
execute procedure actualizar_planilla(); 






