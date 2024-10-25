from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .custom_relational_fields import PhoneNumberRelatedField
from .models import Movie, Genre, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = SerializerMethodField()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_reviews(self, obj):
        result = obj.reviews.all()
        return ReviewSerializer(result, many=True).data


class ReviewSerializer(serializers.ModelSerializer):
    user = PhoneNumberRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


