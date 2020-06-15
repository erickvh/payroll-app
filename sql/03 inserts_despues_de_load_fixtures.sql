INSERT INTO public.catalogo_descuento(
	id, nombre, fecha_inicio, fecha_fin, descuento_total, cantidad_descontada, descuento, fijo)
	VALUES (1,'manutencion del niño', '2015-05-07', '2020-09-09',2000, 20, 20, True);

INSERT INTO public.descuento_empleado(
	id,activo, descuento_id, empleado_id, planilla_id)
	VALUES (1,True, 1, 1, 1);
