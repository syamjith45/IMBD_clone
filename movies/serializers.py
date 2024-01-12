from rest_framework import serializers

from .models import Movies,Review
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    movie =MovieSerializer(many=False)
    class Meta:
        model = Review
        fields= ("id","movie","rating","review",)