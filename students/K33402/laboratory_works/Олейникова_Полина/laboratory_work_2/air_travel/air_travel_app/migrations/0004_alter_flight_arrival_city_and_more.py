# Generated by Django 4.2.6 on 2023-10-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_travel_app', '0003_flight_arrival_city_flight_departure_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(max_length=100),
        ),
    ]
