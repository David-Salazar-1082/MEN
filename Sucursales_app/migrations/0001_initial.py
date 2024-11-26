# Generated by Django 5.1 on 2024-11-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('Id_Sucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=100)),
                ('tamaño', models.FloatField()),
                ('encargado', models.CharField(max_length=100)),
                ('horarios', models.TimeField()),
                ('capacidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Sucursale',
                'verbose_name_plural': 'Sucursales',
                'db_table': 'Sucursales',
            },
        ),
    ]