# Generated by Django 4.0.5 on 2022-06-23 18:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('refueling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refueling',
            name='date_refueling',
            field=models.DateField(default=datetime.datetime(2022, 6, 23, 18, 8, 45, 169956, tzinfo=utc)),
        ),
    ]