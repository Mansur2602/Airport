# Generated by Django 5.1.3 on 2024-12-04 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(db_index=True, max_length=3, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
                ('capacity', models.IntegerField()),
                ('distance', models.FloatField()),
                ('consumtion', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='ФИО парссажира')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('passport', models.CharField(max_length=12, unique=True, verbose_name='Документ')),
            ],
            options={
                'ordering': ['fio', '-birth_date'],
            },
        ),
        migrations.CreateModel(
            name='Fligth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_depart', models.DateTimeField(auto_now=True, verbose_name='Дата и время вылета')),
                ('date_arrive', models.DateTimeField(verbose_name='Дата и время прилета')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_dest', to='Airport.airports', verbose_name='Аэропорт прилета')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_source', to='Airport.airports', verbose_name='Аэропорт вылета')),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Airport.travels', verbose_name='Пассажир')),
            ],
        ),
    ]
