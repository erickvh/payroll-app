# Generated by Django 2.1.15 on 2020-06-14 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('municipio', '0001_initial'),
        ('estado_civil', '0001_initial'),
        ('puesto', '0001_initial'),
        ('genero', '0001_initial'),
        ('profesion', '0001_initial'),
        ('departamento_organizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=25)),
                ('segundo_nombre', models.CharField(max_length=25)),
                ('apellido_paterno', models.CharField(max_length=25)),
                ('apellido_materno', models.CharField(max_length=25)),
                ('apellido_casada', models.CharField(max_length=25, null=True)),
                ('direccion', models.CharField(max_length=50)),
                ('identificacion', models.CharField(max_length=30, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('isss', models.CharField(max_length=30, unique=True)),
                ('nup', models.CharField(max_length=30, unique=True)),
                ('nit', models.CharField(max_length=30, unique=True)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tipo_empleado', models.CharField(max_length=50)),
                ('tipo_identificacion', models.CharField(max_length=50)),
                ('departamento_organizacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento_organizacion.DepartamentoOrganizacion')),
                ('dirigido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empleados', related_query_name='empleado', to='empleado.Empleado')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estado_civil.EstadoCivil')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='genero.Genero')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='municipio.Municipio')),
                ('profesion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profesion.Profesion')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='puesto.Puesto')),
            ],
            options={
                'db_table': 'empleados',
            },
        ),
    ]
