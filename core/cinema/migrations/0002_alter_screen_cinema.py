# Generated by Django 5.1.2 on 2024-10-26 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='cinema.cinema'),
        ),
    ]
