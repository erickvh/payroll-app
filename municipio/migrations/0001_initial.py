# Generated by Django 3.0.5 on 2020-05-02 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamento.Departamento')),
            ],
            options={
                'db_table': 'municipios',
            },
        ),
    ]