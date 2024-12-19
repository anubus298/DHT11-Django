from django.db import models


class NotificationType(models.TextChoices):
    SMS = "SMS", "SMS"
    TELEGRAM = "TELEGRAM", "TELEGRAM"
    EMAIL = "EMAIL", "EMAIL"
    WHATSAPP = "WHATSAPP", "WHATSAPP"


class NotificationsParameters(models.Model):
    mainResource = models.TextField(null=False)
    type = models.CharField(max_length=10, choices=NotificationType.choices, null=False)
    created_at = models.DateTimeField(auto_now_add=True, primary_key=False)

    class Meta:
        db_table = "notifications_parameters"
        constraints = [
            models.UniqueConstraint(
                fields=["type", "mainResource"], name="unique_type_resource"
            )
        ]
