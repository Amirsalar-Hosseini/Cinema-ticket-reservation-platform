# Generated by Django 5.1.2 on 2024-10-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_verificationcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
