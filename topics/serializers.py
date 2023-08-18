from rest_framework import serializers

from django.db.models import Sum
from .models import Topic
# from threads.serializers import ThreadSerializer
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model= Topic
        fields='__all__'

class TopicCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Topic
        fields=['id', 'title', 'created_at', 'slug']


