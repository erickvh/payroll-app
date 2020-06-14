/*
** Antes de empezar es de recordar que en POSTGRESQL no existe el concepto de procedimientos almacenados, aqui todos son funciones. 
*/


/**
*** Funcion para obtener el total de descuento de un empleado especifico
**/

create or replace function 
get_descuento_total(id_empleado int) 
returns numeric AS $$
DECLARE
descuento_total NUMERIC := 0;
BEGIN 
select round(sum(case when c.fijo then c.descuento when c.descuento < 100 then e.salario * c.descuento / 100 else 0 end),2) into descuento_total from empleados as e inner join descuento_empleado as d on e.id = d.empleado_id inner join catalogo_descuento c on c.id = d.descuento_id and d.empleado_id= id_empleado and c.fecha_fin < current_date and d.activo;
RETURN descuento_total;
END;
$$ LANGUAGE plpgsql;




/*
** Funcion para obtener el ingreso total con base al catalogo correspondiente (Sin comisiones)
*/

create or replace function 
get_ingreso_total_de_catalogo(id_empleado int) 
returns numeric AS $$
DECLARE
ingreso_por_catalogo NUMERIC := 0;
BEGIN 
select round(sum(case when c.comision is False and e.tipo_empleado not like '%EC' then c.ingreso else 0 end),2) into ingreso_por_catalogo from empleados as e inner join ingreso_empleado as d on e.id = d.empleado_id inner join catalogo_ingreso c on c.id = d.ingreso_id and d.empleado_id= id_empleado and c.fecha_fin < current_date and d.activo;
RETURN ingreso_por_catalogo;
END;
$$ LANGUAGE plpgsql;




/*
** Obtener todas las comisiones de un empleado en particular
*/


create or replace function 
get_ingreso_total_comision(id_empleado int) 
returns numeric AS $$
DECLARE
ingreso_comision NUMERIC := 0;
BEGIN 
	select round(
		sum(
			case 
			when c.comision and e.tipo_empleado like '%EC' then 
			e.salario * c.porcentaje 
			else 0 end),2) 
		into ingreso_comision 
	from empleados as e 
		inner join ingreso_empleado as d on e.id = d.empleado_id 
		inner join catalogo_ingreso c on c.id = d.ingreso_id 
			and d.empleado_id= id_empleado and d.activo;
RETURN ingreso_comision;
END;
$$ LANGUAGE plpgsql;



