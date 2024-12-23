# Generated by Django 5.1.2 on 2024-10-27 16:29

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_poster'),
        ('ticket', '0004_remove_ticket_num_of_tickets_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField()),
                ('max_usage', models.PositiveIntegerField()),
                ('times_used', models.PositiveIntegerField(default=0)),
                ('movies', models.ManyToManyField(blank=True, to='movie.movie')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
