from core.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_active",
            "created",
            "updated",
            "is_staff",
            "is_active"
        ]
        read_only_field = [ "created", "updated"]
