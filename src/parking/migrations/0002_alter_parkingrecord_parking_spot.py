# Generated by Django 5.1.7 on 2025-05-01 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingrecord',
            name='parking_spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parking_records', to='parking.parkingspot', verbose_name='Vaga'),
        ),
    ]
