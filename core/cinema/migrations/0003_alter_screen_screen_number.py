# Generated by Django 5.1.2 on 2024-10-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_alter_screen_cinema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='screen_number',
            field=models.IntegerField(unique=True),
        ),
    ]
