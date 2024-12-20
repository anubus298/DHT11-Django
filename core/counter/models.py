from django.db import models

class Counter(models.Model):
    value = models.IntegerField(null=False, default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "counter"


class ParameterType(models.TextChoices):
    TEMP_MAX = "TEMP_MAX", "TEMP_MAX"
    TEMP_MIN = "TEMP_MIN", "TEMP_MIN"
    HUM_MAX = "HUM_MAX", "HUM_MAX"
    HUM_MIN = "HUM_MIN", "HUM_MIN"
    COUNTER_TRESHHOLD = "COUNTER_TRESHHOLD", "COUNTER_TRESHHOLD"

class Parameter(models.Model):
    value = models.FloatField(null=False)
    type = models.CharField(max_length=40, choices=ParameterType.choices, null=False, unique=True)    
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "parameters"        