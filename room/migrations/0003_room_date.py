# Generated by Django 5.1.2 on 2024-10-24 07:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]