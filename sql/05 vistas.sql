create or replace 
view vista_planilla  
as 
select 	b.planilla_id, e.id, b.salario_actual, e.primer_nombre,e.apellido_paterno, b.total_ingreso, b.total_comision , b.total_descuento , (b.salario_actual + b.total_ingreso - b.total_descuento) as total from empleados as e inner join boleta_pago as b on b.empleado_id = e.id;

