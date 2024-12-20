# create a mpdel for incident table
from django.db import models
from core.user.models import User


class IncidentNote(models.Model):
    # class
    note = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(
        User,  # References the User model dynamically
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="notes_user",  # Optional: For reverse query
    )
    incident = models.ForeignKey(
        "Incident",  # References the Incident model dynamically
        on_delete=models.CASCADE,
        related_name="notes",  # Optional: For reverse query
        null=False,
    )

    def __str__(self):
        return self.note

    class Meta:
        db_table = "incident_notes"


class Incident(models.Model):
    # class
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    temperature = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    reported_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    closed_by = models.ForeignKey(
        User,  # References the User model dynamically
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="closed_incidents",  # Optional: For reverse query
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "incidents"
