# Generated by Django 5.1.2 on 2024-10-23 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='description',
        ),
    ]
