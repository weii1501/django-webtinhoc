from rest_framework import serializers
from users.serializers import CustomUserRepliesSerializer
from .models import Notification
from threads.serializers import ThreadNotificationSerializer

class NotificationSerializer(serializers.ModelSerializer):
    thread= ThreadNotificationSerializer()
    sender= CustomUserRepliesSerializer()
    class Meta:
        model= Notification
        fields='__all__'

    