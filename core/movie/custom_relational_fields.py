from rest_framework.serializers import RelatedField

class PhoneNumberRelatedField(RelatedField):
    def to_representation(self, value):
        return f'{value.phone_number} {value.first_name} {value.last_name}'