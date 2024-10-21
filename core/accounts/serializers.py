import string
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Registers a new user
    """

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters')
        if not any(char in string.ascii_uppercase for char in value):
            raise serializers.ValidationError('Password must contain at least one uppercase letter')
        if not any(char in string.ascii_lowercase for char in value):
            raise serializers.ValidationError('Password must contain at least one lowercase letter')
        if not any(char in string.digits for char in value):
            raise serializers.ValidationError('Password must contain at least one number')
        return value

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError('Phone number already exists')
        return value

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password or confirm_password:
            if password != confirm_password:
                raise serializers.ValidationError("Passwords do not match.")

        return data

    def validate_first_name(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('First name cannot be admin')
        return value

    def validate_last_name(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('Last name cannot be admin')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
