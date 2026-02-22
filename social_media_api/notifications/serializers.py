from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Notification
        fields = (
            "id",
            "actor",
            "verb",
            "timestamp",
            "is_read",
            "target_content_type",
            "target_object_id",
        )