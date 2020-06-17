create or replace 
view vista_planilla  
as 
select 	b.planilla_id, e.id, b.salario_actual, e.primer_nombre, e.apellido_paterno, b.total_ingreso, b.total_comision , round(b.total_descuento, 2)  as "total_descuento", get_renta((b.salario_actual)) as renta,round(b.salario_actual + b.total_ingreso + b.total_comision - b.total_descuento,2) as total from empleados as e inner join boleta_pago as b on b.empleado_id = e.id;


create or replace 
view vista_departamento
as 
select 	b.planilla_id, 
		d.id, 
		d.nombre,
		sum (b.salario_actual) as total_salario, 
		sum(b.total_ingreso) as total_ingreso, 
		sum(b.total_comision) as total_comision, 
		sum (round(b.total_descuento, 2)) as "total_descuento", 
		sum(get_renta((b.salario_actual))) as renta,
		sum(round(b.salario_actual + b.total_ingreso + b.total_comision - b.total_descuento,2)) as total 
		from empleados as e 
		inner join boleta_pago as b on b.empleado_id = e.id 
		inner join departamento_organizacion as d on e.departamento_organizacion_id = d.id
		group by (b.planilla_id, d.id, d.nombre);


