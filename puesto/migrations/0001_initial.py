# Generated by Django 3.0.5 on 2020-04-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('minimo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('maximo', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'puestos',
            },
        ),
    ]