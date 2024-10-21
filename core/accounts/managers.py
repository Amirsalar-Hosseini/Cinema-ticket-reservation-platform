from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Define user and superuser
    """
    def create_user(self, first_name, last_name, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('User must have a phone_number')

        if not first_name:
            raise ValueError('User must have a first_name')

        if not last_name:
            raise ValueError('User must have a last_name')

        user = self.model(first_name=first_name, last_name=last_name, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number, password):
        user = self.create_user(first_name, last_name, phone_number, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
