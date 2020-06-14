INSERT INTO public.catalogo_descuento(
	id, nombre, fecha_inicio, fecha_fin, descuento, fijo)
	VALUES (1, 'Pago de manutencion', '2009-05-20', '2009-05-20', 20, False);

INSERT INTO public.catalogo_descuento(
	id, nombre, fecha_inicio, fecha_fin, descuento, fijo)
	VALUES (2, 'Pago de manutencion', '2009-05-20', '2009-05-20', 30, False);

INSERT INTO public.catalogo_descuento(
	id, nombre, fecha_inicio, fecha_fin, descuento, fijo)
	VALUES (3, 'Pago de manutencion', '2009-05-20', '2009-05-20', 400, True);

INSERT INTO public.catalogo_descuento(
	id, nombre, fecha_inicio, fecha_fin, descuento, fijo)
	VALUES (4, 'Pago de manutencion', '2009-05-20', '2009-05-20', 500, True);

INSERT INTO public.catalogo_descuento(
	id, nombre, fecha_inicio, fecha_fin, descuento, fijo)
	VALUES (5, 'Pago de manutencion', '2009-05-20', '2009-05-20', 600, True);

	

INSERT INTO public.catalogo_ingreso(
	id, nombre, fecha_inicio, fecha_fin, ingreso, comision, porcentaje)
	VALUES (1, 'nose 1','2009-05-20' , '2020-05-20', 200, False, 0);

INSERT INTO public.catalogo_ingreso(
	id, nombre, fecha_inicio, fecha_fin, ingreso, comision, porcentaje)
	VALUES (2, 'nose 1','2009-05-20' , '2020-05-20', 300, False, 0);

INSERT INTO public.catalogo_ingreso(
	id, nombre, fecha_inicio, fecha_fin, ingreso, comision, porcentaje)
	VALUES (3, 'nose 1','2009-05-20' , '2020-05-20', 400, False,0);

INSERT INTO public.catalogo_ingreso(
	id, nombre, fecha_inicio, fecha_fin, ingreso, comision, porcentaje)
	VALUES (4, 'nose 1','2009-05-20' , '2020-05-20', 500, False,0);

INSERT INTO public.catalogo_ingreso(
	id, nombre, fecha_inicio, fecha_fin, ingreso, comision, porcentaje)
	VALUES (5, 'nose 1','2009-05-20' , '2020-05-20', 600, False,0);

INSERT INTO public.catalogo_ingreso(
	id, nombre, fecha_inicio, fecha_fin, ingreso, comision, porcentaje)
	VALUES (6, 'nose 1','2009-05-20' , '2020-05-20', 700, False,0);

	
INSERT INTO public.descuento_empleado(
	id, activo, descuento_id, empleado_id)
	VALUES (1, True, 1, 1);

INSERT INTO public.descuento_empleado(
	id, activo, descuento_id, empleado_id)
	VALUES (2, True, 3, 1);

INSERT INTO public.descuento_empleado(
	id, activo, descuento_id, empleado_id)
	VALUES (3, True, 3, 2);
	
INSERT INTO public.descuento_empleado(
	id, activo, descuento_id, empleado_id)
	VALUES (4, True, 4, 2);
	


INSERT INTO public.ingreso_empleado(
	id, activo, empleado_id, ingreso_id)
	VALUES (1, True, 1, 1);
	
INSERT INTO public.ingreso_empleado(
	id, activo, empleado_id, ingreso_id)
	VALUES (2, True, 1, 2);
	
INSERT INTO public.ingreso_empleado(
	id, activo, empleado_id, ingreso_id)
	VALUES (3, True, 1, 3);
	
INSERT INTO public.ingreso_empleado(
	id, activo, empleado_id, ingreso_id)
	VALUES (4, True, 2, 1);
	
INSERT INTO public.ingreso_empleado(
	id, activo, empleado_id, ingreso_id)
	VALUES (5, True, 2, 3);


INSERT INTO public.salario_minimo(
	id, monto, activo)
	VALUES (1, 300, True);
	
INSERT INTO public.periodicidad(
	id, anio_periodo, quincenal, mensual)
	VALUES (1, 2020, False, True);
	
INSERT INTO public.descuento_general(
	id, nombre, porcentaje, activo)
	VALUES (1, 'ISSS', 0.03, True);
	

INSERT INTO public.descuento_general(
	id, nombre, porcentaje, activo)
	VALUES (2, 'AFP', 0.06, True);
	

