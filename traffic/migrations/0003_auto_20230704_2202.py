# Generated by Django 3.2.20 on 2023-07-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0002_auto_20230704_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='lane',
            name='bike_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lane',
            name='car_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lane',
            name='vehicle_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='VehicleCount',
        ),
    ]
