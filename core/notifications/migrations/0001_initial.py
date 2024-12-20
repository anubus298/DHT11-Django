# Generated by Django 3.2.4 on 2024-12-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainResource', models.TextField()),
                ('type', models.CharField(choices=[('SMS', 'SMS'), ('TELEGRAM', 'TELEGRAM'), ('EMAIL', 'EMAIL'), ('WHATSAPP', 'WHATSAPP')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'notifications_parameters',
            },
        ),
    ]
