from rest_framework import serializers
from .models import NotificationsParameters


class NotificationsParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationsParameters
        fields = "__all__"
