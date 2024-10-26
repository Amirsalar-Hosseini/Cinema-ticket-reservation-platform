from django.contrib import admin
from .models import User, VerificationCode


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'first_name', 'last_name']

@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'code', 'is_used']