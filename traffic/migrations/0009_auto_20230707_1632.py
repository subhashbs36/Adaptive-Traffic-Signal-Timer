# Generated by Django 2.1.15 on 2023-07-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0008_auto_20230707_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='lanedata',
            name='bus_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lanedata',
            name='rickshaw_count',
            field=models.IntegerField(default=0),
        ),
    ]
