from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Screen


@receiver(post_save, sender=Screen)
def update_cinema_capacity_on_save(sender, instance, **kwargs):
    cinema = instance.cinema
    cinema.total_capacity = sum(screen.capacity for screen in cinema.screens.all())
    cinema.num_of_screens = cinema.screens.count()
    cinema.save()

@receiver(post_delete, sender=Screen)
def update_cinema_capacity_on_delete(sender, instance, **kwargs):
    cinema = instance.cinema
    cinema.total_capacity = sum(screen.capacity for screen in cinema.screens.all())
    cinema.num_of_screens = cinema.screens.count()
    cinema.save()