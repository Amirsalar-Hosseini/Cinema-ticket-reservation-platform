# Generated by Django 5.1.2 on 2024-10-25 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together={('showtime', 'seat_number')},
        ),
    ]