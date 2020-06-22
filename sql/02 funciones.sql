/*
** Antes de empezar es de recordar que en POSTGRESQL no existe el concepto de procedimientos almacenados, aqui todos son funciones. 
*/


/**
*** Funcion para obtener el total de descuento de un empleado especifico
**/

create or replace function 
get_descuento_total(p_empleado_id int, p_planilla_id int) 
returns numeric AS $$
DECLARE
v_descuento_total NUMERIC := 0;
BEGIN 
	select round(sum(
		case when c.fijo then c.descuento
			when c.descuento < 100 then e.salario * c.descuento / 100 else 0 end),2) 
			into v_descuento_total 
		from empleados as e inner join 
		descuento_empleado as d on e.id = d.empleado_id 
		inner join catalogo_descuento c 
			on c.id = d.descuento_id 
			and d.empleado_id= p_empleado_id 
			and current_date between c.fecha_inicio and c.fecha_fin and d.activo
			and d.planilla_id = p_planilla_id;
RETURN v_descuento_total;
END;
$$ LANGUAGE plpgsql;





/*
** Funcion para obtener el ingreso total con base al catalogo correspondiente (Sin comisiones)
*/

create or replace function 
get_ingreso_total_de_catalogo(p_empleado_id int, p_planilla_id int) 
returns numeric AS $$
DECLARE
v_ingreso_por_catalogo NUMERIC := 0;
BEGIN 
	select round(sum(
		case when c.comision is False and e.tipo_empleado not like '%EC' then c.ingreso 
			else 0 end),2) 
		into v_ingreso_por_catalogo 
		from empleados as e 
			inner join ingreso_empleado as d 
			on e.id = d.empleado_id 
			inner join catalogo_ingreso c 
			on c.id = d.ingreso_id 
			and d.empleado_id= p_empleado_id 
			and current_date between c.fecha_inicio and c.fecha_fin and d.activo
			and d.planilla_id = p_planilla_id;
RETURN v_ingreso_por_catalogo;
END;
$$ LANGUAGE plpgsql;




/*
** Obtener todas las comisiones de un empleado en particular
*/


create or replace function 
get_ingreso_total_comision(p_empleado_id int, p_planilla_id int) 
returns numeric AS $$
DECLARE
v_ingreso_comision NUMERIC := 0;
BEGIN 
	select round(
		sum(
			case 
			when c.comision and e.tipo_empleado like '%EC' then 
			c.ingreso * c.porcentaje 
			else 0 end),2) 
		into v_ingreso_comision 
	from empleados as e 
		inner join ingreso_empleado as d on e.id = d.empleado_id 
		inner join catalogo_ingreso c on c.id = d.ingreso_id 
			and d.empleado_id= p_empleado_id and d.activo
			and d.planilla_id = p_planilla_id;
RETURN v_ingreso_comision;
END;
$$ LANGUAGE plpgsql;

/*
** Obtener todos los descuentos de ley de un monto
*/


create or replace function 
get_descuento_ley(p_monto numeric) 
returns numeric AS $$
DECLARE
rec_descuento_gral RECORD;
v_descuento_e NUMERIC := 0;
BEGIN 
	for rec_descuento_gral in select * from descuento_general where activo = true loop
		v_descuento_e = v_descuento_e + p_monto * rec_descuento_gral.porcentaje;
	end loop;
RETURN v_descuento_e;
END;
$$ LANGUAGE plpgsql;



/*
** Obtener la renta de un monto
*/

create or replace function 
get_renta(p_monto numeric) 
returns numeric AS $$
DECLARE
v_descuento_e NUMERIC := 0;
BEGIN 
	select round(avg(porcentaje)*p_monto/100,2) + sum(cuota_fija) into v_descuento_e from impuesto_renta where p_monto between minimo and maximo;
	if v_descuento_e is null then
		v_descuento_e = 0;
	end if;
RETURN v_descuento_e;
END;
$$ LANGUAGE plpgsql;




