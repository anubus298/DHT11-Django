# Generated by Django 3.2.4 on 2024-12-18 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationsparameters',
            name='mainResource',
            field=models.TextField(unique=True),
        ),
    ]
