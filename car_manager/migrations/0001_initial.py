# Generated by Django 4.0.5 on 2022-06-08 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('type_of_fuel', models.CharField(blank=True, choices=[('1', 'Petrol'), ('2', 'Gasoline')], max_length=2, null=True)),
                ('inssurance_expired_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarProductionDetail',
            fields=[
                ('company', models.TextField(blank=True, null=True)),
                ('car_model_name', models.TextField(blank=True, null=True)),
                ('production_year', models.IntegerField(blank=True, null=True)),
                ('vin', models.IntegerField(blank=True, null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='car_manager.car')),
            ],
        ),
    ]
