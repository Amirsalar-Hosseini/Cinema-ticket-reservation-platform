from celery import shared_task
from .models import VerificationCode
from django.utils import timezone

@shared_task
def delete_old_codes():
    expiration_time = timezone.now() - timezone.timedelta(minutes=2)
    VerificationCode.objects.filter(created__lt=expiration_time).delete()

