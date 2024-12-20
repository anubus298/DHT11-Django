from django.db import migrations

def create_default_parameters(apps, schema_editor):
    Parameter = apps.get_model("counter", "parameter")
    default_parameters = [
        {"type": "TEMP_MAX", "value": 35},
        {"type": "TEMP_MIN", "value": 20},
        {"type": "HUM_MAX", "value": 65},
        {"type": "HUM_MIN", "value": 45},
        {"type": "COUNTER_TRESHHOLD", "value": 20},

    ]
    for param in default_parameters:
        Parameter.objects.update_or_create(type=param["type"], defaults={"value": param["value"]})

class Migration(migrations.Migration):

    dependencies = [
        ("counter", "0002_parameter"),
    ]

    operations = [
        migrations.RunPython(create_default_parameters),
    ]
