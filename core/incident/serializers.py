from rest_framework import serializers
from .models import Incident, IncidentNote
from ..user.serializers import UserSerializer


class IncidentSerializer(serializers.ModelSerializer):
    closed_by = UserSerializer(read_only=True)

    class Meta:
        model = Incident
        fields = "__all__"


class IncidentNoteSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = IncidentNote
        fields = "__all__"
